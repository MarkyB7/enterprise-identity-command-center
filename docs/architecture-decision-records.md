# Architecture Decision Records

## ADR-001: Use Microsoft Entra ID as the Primary Identity Provider

### Decision

Microsoft Entra ID will serve as the primary identity provider for this project.

### Reasoning

Many enterprise organizations use Entra ID as their central identity platform for workforce identity, group management, authentication, SSO, and MFA. Using Entra ID allows this project to simulate a realistic enterprise identity architecture.

### Alternatives Considered

- Local IAM users only
- AWS IAM users only
- Okta
- Custom identity database

### Why This Decision Was Made

Using local AWS IAM users would not demonstrate modern enterprise identity architecture. A centralized identity provider allows stronger governance, easier lifecycle management, SSO integration, MFA enforcement, and better auditability.

### Security Benefit

Centralized identity reduces identity sprawl, improves control over authentication, and supports consistent policy enforcement across applications and cloud platforms.
