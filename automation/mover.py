import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_FILE = BASE_DIR / "evidence" / "audit-results" / "mover-audit-log.json"

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

user_change = {
    "name": "James Cloud",
    "email": "james.cloud@demo.local",
    "old_role": "Cloud Engineer",
    "new_role": "IAM Admin"
}

old_group = ROLE_TO_GROUP[user_change["old_role"]]
new_group = ROLE_TO_GROUP[user_change["new_role"]]

old_permission_set = ROLE_TO_PERMISSION_SET[user_change["old_role"]]
new_permission_set = ROLE_TO_PERMISSION_SET[user_change["new_role"]]

risk_level = "High"

audit_record = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "action": "ROLE_CHANGE",
    "name": user_change["name"],
    "email": user_change["email"],
    "old_role": user_change["old_role"],
    "new_role": user_change["new_role"],
    "removed_group": old_group,
    "assigned_group": new_group,
    "removed_permission_set": old_permission_set,
    "assigned_permission_set": new_permission_set,
    "risk_level": risk_level,
    "approval_required": True,
    "status": "Role Updated"
}

print(f"[INFO] Processing role change for {user_change['name']}")
print(f"[INFO] Removing group: {old_group}")
print(f"[INFO] Assigning group: {new_group}")
print(f"[INFO] Removing permission set: {old_permission_set}")
print(f"[INFO] Assigning permission set: {new_permission_set}")
print("[INFO] Approval required: True")
print(f"[SUCCESS] {user_change['email']} role updated successfully")

with open(LOG_FILE, mode="w") as log:
    json.dump(audit_record, log, indent=4)

print(f"[COMPLETE] Mover audit log written to: {LOG_FILE}")
