
# IAM Standard

## Purpose

This standard defines how identities, roles, groups, privileged access, and cloud permissions are managed in the Enterprise Identity Command Center project.

## Core Rules

1. No direct user permissions are allowed.
2. Access must be assigned through groups, roles, or permission sets.
3. MFA is required for all cloud and privileged access.
4. Privileged access must be separated from standard access.
5. Contractor access must be time-bound and reviewed regularly.
6. Service account secrets must not be stored in plain text.
7. All privileged activity must be logged.
8. Access reviews must be performed regularly.
9. Deprovisioned users must lose access immediately.
10. Break-glass accounts must be monitored and used only for emergencies.

## Identity Types

| Identity Type | Description |
|---|---|
| Standard User | Normal employee account |
| Contractor | Temporary or vendor identity |
| Privileged Admin | Elevated administrative access |
| Break-Glass Admin | Emergency-only administrative account |
| Service Account | Non-human identity used by systems or applications |

## Access Model

Access is based on RBAC. Users are assigned to groups based on job function. Groups are mapped to cloud permission sets and application access.
