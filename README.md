# Enterprise Identity Command Center

## Senior IAM Architecture, Governance, PAM, SSO, MFA, and Cloud Identity Project

Enterprise Identity Command Center is a senior-level IAM architecture project designed to simulate how an enterprise manages identity lifecycle, privileged access, access governance, cloud identity, SSO, MFA, and audit readiness across a hybrid environment.

This project demonstrates hands-on IAM engineering and architecture using Microsoft Entra ID, AWS IAM Identity Center, Terraform, Python automation, RBAC models, privileged access controls, access review workflows, and centralized audit evidence.

The goal of this project is to prove the ability to design, implement, document, and defend enterprise IAM decisions in a way that aligns with senior IAM engineer, IAM architect, and cloud identity leadership responsibilities.

## Methodology

This project follows an enterprise IAM architecture methodology based on identity lifecycle, least privilege, governance, and auditability.

### 1. Centralized Identity

Microsoft Entra ID serves as the central identity provider. Users and groups are managed from a single source of identity truth and federated into AWS IAM Identity Center.

### 2. Group-Based RBAC

Access is assigned through security groups and permission sets instead of direct user permissions. This supports least privilege, easier access reviews, and scalable administration.

### 3. Joiner, Mover, Leaver Lifecycle

Identity lifecycle workflows simulate how users are provisioned, modified, and deprovisioned based on business role changes.

### 4. Privileged Access Management

Administrative and privileged access is separated from standard access. Privileged roles require stronger controls, MFA, logging, and periodic review.

### 5. Governance and Audit Readiness

Access reviews, RBAC documentation, privileged access standards, and audit evidence are maintained to demonstrate compliance readiness.
