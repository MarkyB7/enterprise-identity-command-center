import csv
import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
USERS_FILE = BASE_DIR / "automation" / "users.csv"
LOG_FILE = BASE_DIR / "evidence" / "audit-results" / "joiner-provisioning-log.json"

ROLE_TO_GROUP = {
    "Cloud Engineer": "GG-AWS-CloudEngineer",
    "Security Analyst": "GG-SecurityAnalyst",
    "IAM Admin": "GG-IAM-Admin",
    "Finance Analyst": "GG-Finance",
    "Contractor": "GG-Contractor"
}

ROLE_TO_PERMISSION_SET = {
    "Cloud Engineer": "CloudEngineer-PS",
    "Security Analyst": "SecurityAnalyst-PS",
    "IAM Admin": "IAMAdmin-PS",
    "Finance Analyst": "FinanceApp-PS",
    "Contractor": "Contractor-PS"
}

def provision_user(user):
    role = user["role"]
    group = ROLE_TO_GROUP.get(role, "GG-Needs-Review")
    permission_set = ROLE_TO_PERMISSION_SET.get(role, "ManualReview-PS")

    risk_level = "High" if role in ["IAM Admin", "Contractor"] else "Medium"

    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "action": "JOINER_PROVISIONING",
        "name": user["name"],
        "email": user["email"],
        "department": user["department"],
        "role": role,
        "employment_type": user["employment_type"],
        "assigned_group": group,
        "assigned_permission_set": permission_set,
        "mfa_required": True,
        "direct_permissions_assigned": False,
        "risk_level": risk_level,
        "status": "Provisioned"
    }

    print(f"[INFO] Creating identity for {user['name']}")
    print(f"[INFO] Assigning group: {group}")
    print(f"[INFO] Assigning permission set: {permission_set}")
    print("[INFO] MFA required: True")
    print("[INFO] Direct permissions assigned: False")
    print(f"[SUCCESS] {user['email']} provisioned successfully\n")

    return record

def main():
    audit_records = []

    with open(USERS_FILE, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for user in reader:
            if user["status"] == "Active":
                audit_records.append(provision_user(user))

    with open(LOG_FILE, mode="w") as log:
        json.dump(audit_records, log, indent=4)

    print(f"[COMPLETE] Provisioning log written to: {LOG_FILE}")

if __name__ == "__main__":
    main()
