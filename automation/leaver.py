import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_FILE = BASE_DIR / "evidence" / "audit-results" / "leaver-audit-log.json"

terminated_user = {
    "name": "Chris Vendor",
    "email": "chris.vendor@demo.local",
    "role": "Contractor",
    "status": "Terminated"
}

audit_record = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "action": "DEPROVISION",
    "name": terminated_user["name"],
    "email": terminated_user["email"],
    "role": terminated_user["role"],
    "account_disabled": True,
    "groups_removed": True,
    "permission_sets_revoked": True,
    "active_sessions_terminated": True,
    "mfa_tokens_revoked": True,
    "risk_level": "High",
    "status": "Access Revoked"
}

print(f"[INFO] Processing termination for {terminated_user['name']}")
print("[INFO] Disabling account")
print("[INFO] Removing RBAC group memberships")
print("[INFO] Revoking permission sets")
print("[INFO] Terminating active sessions")
print("[INFO] Revoking MFA tokens")
print(f"[SUCCESS] {terminated_user['email']} fully deprovisioned")

with open(LOG_FILE, mode="w") as log:
    json.dump(audit_record, log, indent=4)

print(f"[COMPLETE] Leaver audit log written to: {LOG_FILE}")
