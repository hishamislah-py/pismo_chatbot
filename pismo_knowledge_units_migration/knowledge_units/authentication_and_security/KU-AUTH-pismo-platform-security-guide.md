---
ku_id: KU-AUTH-pismo-platform-security-guide
title: Security guide for Pismo platform
category: authentication_and_security
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/pismo-platform-security-guide.md
  sha256: b2d4194de59ac6dbe29b50e96c241e1badeacaac76ee1cea8b5a892df6b139c2
  url: https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide
  role: primary_guide
  updated_at: '2026-06-30T14:11:30.000Z'
operations:
- post-acquisitions-v3-s2s-applications
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-AUTH-authentication-methods
- KU-AUTH-identity-connectivity-with-mtls
- KU-AUTH-security-programme
- KU-EVT-catalogue-other-domains
- KU-EVT-verifying-webhook-requests
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Security guide for Pismo platform

**KU ID:** `KU-AUTH-pismo-platform-security-guide` · **Category:** Authentication and security · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/get-started/pismo-platform-security-guide.md`:

> Pismo is committed to providing you with a trusted set of financial services. We have used our cloud industry experience building enterprise software and running some of the world’s largest online services to create and implement a robust set of security technologies and practices. These practices help reduce the cost, complexity, and risk associated with security in the financial services cloud. Our mission is to deliver the highest levels of security, privacy, compliance, and availability to the financial sector and help you protect your business assets. Pismo invests annually in cybersecurity and employs dedicated cybersecurity professionals. We take a defense-in-depth approach to security on the Pismo platform, helping you strengthen your security posture, streamline your compliance efforts, and enable digital transformation.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/pismo-platform-security-guide.md`: Security guide for Pismo platform; General platform security; Security development process; Hardening process; Pismo platform’s custom management capabilities; Access management; Server authentication; Authentication with client credentials; Authentication with OpenID Connect; Authentication with OAuth2; Identity connectivity with mTLS; Encryption management; Transport Encryption; Encryption at Rest; Key management and rotation; PGP encryption for card embossing; Secrets management; Application and service secrets; Infrastructure secrets; Identity and access management; Privileged access management; Network access controls (NAC); Data and information management; Data rights management (DRM); Security information and event management tool (SIEM); Data classification and identity (with multiple layers); Defined ownership of data during partnership with customers; Customer data reporting types; Data retention policy; Data location to avoid crossing national or regional boundaries; Data privacy; Data backup and recovery; Business continuity plan and disaster recovery (BCP/DR); Data storage; Data leakage detection; Security architecture; Security management; Enterprise-wide risk management; Security logs and log management; Cloud security; Cloud failover; Web application firewall; Digital signatures; Web filtering controls; Cyber information security

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/pismo-platform-security-guide.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide · updatedAt: 2026-06-30T14:11:30.000Z

<!-- source:begin path=docs/get-started/pismo-platform-security-guide.md part=0-end -->

# Security guide for Pismo platform

Pismo is committed to providing you with a trusted set of financial services. We have used our cloud industry experience building enterprise software and running some of the world’s largest online services to create and implement a robust set of security technologies and practices. These practices help reduce the cost, complexity, and risk associated with security in the financial services cloud. Our mission is to deliver the highest levels of security, privacy, compliance, and availability to the financial sector and help you protect your business assets. Pismo invests annually in cybersecurity and employs dedicated cybersecurity professionals. We take a defense-in-depth approach to security on the Pismo platform, helping you strengthen your security posture, streamline your compliance efforts, and enable digital transformation.

The Pismo platform follows an API-driven architecture. This design allows for seamless integration with various systems and services that you may have. Many of our customers chose to build their own UI on top of the Pismo platform. This method allows you to control all access and authentication to the Pismo platform, including single sign-on (SSO) and multi-factor authentication (MFA) policies. You can also access the Pismo platform through Pismo Control Center.

This security guide for the Pismo platform covers the following topics:

* [General platform security](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide#general-platform-security)
* [Access management](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide#access-management)
* [Data and information management](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide#data-and-information-management)
* [Data backup and recovery](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide#data-backup-and-recovery)
* [Security architecture](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide#security-architecture)
* [Security management](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide#security-management)
* [Cloud security](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide#cloud-security)
* [Security audit, testing, and incident response](https://developers.pismo.io/pismo-docs/docs/security-audit-testing-and-incident-response) sub-guide
* [Compliance, certifications, and Pismo security teams](https://developers.pismo.io/pismo-docs/docs/certifications-compliance-and-security-teams) sub-guide

# General platform security

The Pismo platform is deployed in an Amazon Web Service (AWS) infrastructure, which has in place the following practices and controls:

* Secure design
* Business continuity and disaster recovery
* Monitoring and logging
* Surveillance and detections
* Operational support systems
* Infrastructure maintenance
* Governance and risk

The gremlin agent is installed in the Kubernetes cluster through a Helm chart and runs in a separate namespace. This agent only communicates outbound with the Gremlin platform to receive attack instructions and abort commands, so no extraneous incoming data ever gets in.

Pismo is a highly secured platform, and has ISO 27001, PCI DSS, and PCI PIN Security certifications in place to ensure greater control to the environment. Pismo has multi layered security mechanisms in place, including:

* Identity and access management (IAM)
* mTLS
* Encryption management
* Secrets management
* API gateways
* Cloud security controls

Pismo has several mechanisms to check the health of its tools. Monitoring takes place through logs, metrics, and monitoring tools. Customers can monitor Pismo platform status through the Status Page.

## Security development process

Pismo has a Secure Systems Development Life Cycle (SSDLC) in place to define security requirements and tasks that must be considered and addressed within every system, project, or application that is created or updated to address a business need. The SSDLC ensures that security is adequately considered and built into each phase of every System Development Life Cycle (SDLC).

## Hardening process

Pismo has a security baseline and hardening process in place based on the Center for Internet Security (CIS) benchmarks and best practices. This process intends to secure all technological resources that compose our environment to minimize its attack surface, or surface of vulnerability, and potential attack vectors. 

Our hardening involves securing not only a computer’s software applications, including the operating system, but also its firmware, databases, cloud, and other critical elements that an attacker could exploit.

There are currently six main types of hardening in place:

* Server hardening
* Software application hardening
* Operating system hardening
* Database hardening
* Network hardening
* Cloud environment

## Pismo platform’s custom management capabilities

The authentication between our platform and its clients uses layers of authentication, such as mTLS and JWT token parameterization at the API gateway.

# Access management

## Server authentication

There are multiple ways to perform server-to-server authentication for the Pismo platform.

* Authentication with client credentials
* Authentication with OpenID Connect
* Authentication with OAuth2

### Authentication with client credentials

The Pismo platform supports server-to-server (S2S) authentication using stored credentials. This is similar to a username/password system, except it uses a server\_key and a secret\_key.

The Pismo platform's Passport API allows server-to-server authentication, so a proxy server can execute some operations. For example, in the case of a person using an app on a mobile device or an operator using a CRM system, the authentication process should go through a proxy server.

For details, refer to the [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials) guide.

### Authentication with OpenID Connect

OpenID Connect for Servers is the preferred way to authenticate with the Pismo platform. It provides greater security guarantees in service communications than basic authentication using client credentials. In addition, OpenID Connect supports multi-tenancy. This means that, for example, you can give a third party access to only a specific set of endpoints within your organization.

For details on OpenID Connect authentication, refer to the [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid) guide.

For third-party access, refer to the [Third-party authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/third-party-authentication-with-openid) guide.

### Authentication with OAuth2

The Pismo platform supports OAuth2 authentication using stored credentials. Pismo's OAuth2 implementation follows the RFC 6749 specification, providing secure token-based authentication for API access.

For details on how to obtain access tokens using the Client Credentials grant type, refer to the [Authentication with OAuth2](https://developers.pismo.io/pismo-docs/docs/authentication-with-oauth2) guide.

## Identity connectivity with mTLS

Mutual Transport Layer Security (mTLS) is an end-to-end security protocol that verifies the identity of both sides of a communication stream—the client and the Pismo platform. It provides mutual authentication between client and server, ensuring that both parties verify each other's identities before establishing a secure connection.

mTLS is mandatory for all API calls to the Pismo platform. This protocol keeps the platform in compliance with legal requirements, such as the European Union's eIDAS regulation and the revised Payment Services Directive (PSD2).

To configure mTLS, contact your Pismo representative. For more details about mTLS and the Pismo platform, refer to the [Identity connectivity with mTLS](https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls) guide.

## Encryption management

Pismo is certified as a PCI DSS Level 1 Service Provider, the highest level of assessment available. Pismo uses data encryption and has multiple controls in place for data security.

### Transport Encryption

Pismo enforces HTTPS connections using the TLS v1.2 protocol for all connections to Internet-facing websites/services. Pismo provides a secure SSL/TLS configuration and cipher suite to maintain an A+ rating on Qualys’s SSL Labs scanner.

### Encryption at Rest

All customer data stored on Amazon Web Services (AWS) EBS volumes, S3 buckets, RDS buckets, and Redshift is encrypted using AWS Key Management Service (KMS). AWS KMS utilizes AES-256 encryption in GCM mode to encrypt data. Pismo uses KMS to generate and manage cryptographic keys and operates as a cryptographic service provider for protecting data.

Pismo encrypted database (DB) instances use the industry standard AES-256 encryption algorithm to encrypt data on the DB instances. After data is encrypted, Pismo handles authentication of access and decryption of data transparently with minimal impact on performance. In addition, all logs, backups, and snapshots are encrypted.

### Key management and rotation

The PCI PIN Security Standard is a set of requirements developed by the Payment Card Industry Security Standards Council (PCI SSC) to ensure the secure management, processing, and transmission of personal identification number (PIN) data during payment card transactions. The entire key management process at Pismo strictly follows all the requirements of the PCI PIN Security Standard and seeks to meet the objectives of the standard. PCI information is stored in a separate secure database.

Cryptographic keys for encrypting data on AWS are managed using the AWS KMS. AWS KMS does not provide the ability to recover/extract the keys. AWS KMS keys managed by Pismo (AWS Customer Managed Keys) are automatically rotated annually.

### PGP encryption for card embossing

Pretty Good Privacy (PGP) is an asymmetric encryption that uses public and private keys to encrypt and decrypt cipher text. All card embossing files are encrypted using PGP keys where the embossing partner creates and holds the key pair, and Pismo uses the public component of the key. Pismo uses an SFTP connection between itself and the embosser to ensure encrypted information exchange.

Note that the embossing process does not support PGP keys that use sub-keys. Therefore, the public key generated by the embosser must be able to perform all functions without using sub-keys. The public key must be a single key \[SCEA] (Sign, Certify, Encrypt, Authenticate) or \[SCE] (Sign, Certify, Encrypt), and the key must have the \[E] function to encrypt the files.

The PGP expiration is set during the creation of the primary, public key by the embosser and is typically set to 1-2 years. Card embossing flows rely on this PGP key to securely process files. An expired key will block embossing and may push messages to the Dead Letter Queue (DLQ) or require manual intervention.

When a PGP key is close to expiring, Pismo receives a `WorkerCardsEmbossingPgpKeys` alarm. The alarm is generated 30 days or less before the expiration date. Once this alarm is received, Pismo contacts the embossing partner for a new key before the expiration date. A timely response from the embosser is necessary because if the key expires, the embossing will not be processed correctly until the public PGP key is renewed. Note that only the public key content needs to be updated; the secret label does not need to be changed.

If, for any reason, the PGP key expires, the client must contact their Pismo representative as soon as possible to arrange for a new key exchange.

## Secrets management

Pismo uses two approaches for secret management across our infrastructure and application services: application and service secrets and infrastructure secrets. Both approaches are backed by AWS KMS for performing encryption and key management.

### Application and service secrets

For all services deployed on our Kubernetes cluster, Pismo passes secrets to underlying containers by using the Kubernetes Secrets API integrated with AWS Secrets Manager. Data stored as a Kubernetes secret is protected using Kubernetes’ Role-Based Access Control (RBAC) to ensure only authorized containers can read or write to the secret. 

Kubernetes treats secrets as sensitive data to ensure plaintext values are not accidentally included in logs. Every access to Kubernetes Secrets is logged via Pismo’s configured Kubernetes Audit policy, and all logs are forwarded to the Security Information and Event Management (SIEM) tool.

Kubernetes Secret data is encrypted before it is stored in the datastore with the AWS KMS as the encryption provider. This ensures that secret data can only be decrypted by the Kubernetes API service. Because Pismo uses AWS KMS for encryption, it inherits all the audit and security controls provided by AWS.

### Infrastructure secrets

For secrets that are used to build infrastructure components that do not run within the Kubernetes cluster, Pismo uses the AWS Secure Parameter Store. Secrets are stored in AWS Secrets Manager and are encrypted using AWS KMS.

AWS Secrets Manager data is protected with AWS IAM on the specific store object as well as the KMS keys. Every access is auditable using AWS Cloudtrail, which is forwarded to our SIEM. Additionally, all secrets are version controlled by the AWS Secrets Manager service.

## Identity and access management

Identity and access management (IAM) is a framework of business processes, policies, and technologies that is used for the management of electronic or digital identities at Pismo. Through the IAM system, Pismo manages access to databases, storage, and other application services. IAM's primary capability is access and permissions. 

## Privileged access management

The Pismo platform uses just-in-time (JIT) access to manage temporary elevated permissions. This is a way to request access for a specific time period, validate the need, and grant time-bound access. The platform monitors activity and revokes access if conditions change.

## Network access controls (NAC)

To guarantee secure access to our resources, Pismo internally uses a set of technologies and processes including:

**Single Sign-On**—Provides a seamless authentication experience for end users. After end users sign into our IAM system, they can launch any of their assigned application integrations to access external applications and services without re-entering their credentials. It also enables the Pismo Access Team to revoke all access privileges immediately after termination of an employment contract.

**MDM with Workspace One**—This simplified access management introduces policy enhancements such as the ability to apply policy-based rules to specific scenarios such as device compliance status and conditional access specific policies.

**Grant least privilege to AWS resources**—When Pismo creates IAM policies, it follows standard least privilege security directions by granting only the permissions required to perform a particular task. It is first determined exactly what users (and roles) need to do and then we craft policies that allow them to perform only those tasks. Pismo works with minimum permissions and grants additional permissions as necessary. This methodology  is more secure than starting with permissions too lenient and then trying to tighten them later.

# Data and information management

## Data rights management (DRM)

**Administrative access/RBAC**

To keep data private and secure, Pismo logically isolates each customer’s Platform data from that of other customers, even when it’s stored on the same physical server. Only a small group of Pismo employees have access to customer data (Engineers and DBAs). For Pismo employees, access rights and levels are based on their job function and role via role-based access control (RBAC), using the concepts of least-privilege and need-to-know to match access privileges to defined responsibilities.

Pismo employees are only granted a limited set of default permissions to access company resources, such as employee email and the internal employee portal. Requests for additional access follow a formal process that involves a request and an approval from a data or system owner, manager, or other executives, as dictated by Pismo security policies.

**Periodical user access review**

A user access review is a routine part of account management and access control. It ensures that all Pismo employees and service providers have appropriate access rights. A user access review includes re-evaluation of:

* User roles
* Access rights and privileges
* Credentials provided to users

## Security information and event management tool (SIEM)

Pismo maintains its own Security Operation Center (SOC) 7x24x365. The SOC operates with the  SIEM solution for log aggregation and retention (90 days for immediate availability and 365 archived). All stored logs are encrypted, and access to them is only allowed through the SIEM. The Pismo Security Operation Center team also supports and protects against cyber-attacks.

The SOC team is responsible for managing security incidents effectively, including:

* **Investigating potential incidents**—SIEM generates alerts based on use cases defined by Pismo (using its internal and external sources as references based on threat model standards such as MITRE ATT\&CK and PCI DSS). SOC analysts examine all potential incidents to determine if it is a real attack or a false positive.
* **Triaging and prioritizing detected incidents**—Once an incident has been identified, it is triaged and prioritized to optimize resource utilization and minimize enterprise risk.
* **Coordinating an incident response**—Responding to an incident requires engagement with multiple stakeholders and the use of a variety of tools. The SOC team orchestrates this process to ensure that oversights do not result in delayed or incomplete remediation. Playbooks support Pismo with a standard set of procedures to timely identify, coordinate, remediate, recover, and track successful mitigations from incidents and vulnerabilities affecting Pismo's systems, data, and networks.

## Data classification and identity (with multiple layers)

Pismo has a Data Protection Governance Policy and Process in place that drives how threat information is collected and how compliance with laws and regulations related to the protection of personal data is achieved. The essential principles related to the protection of personal data and how these principles should be implemented are explained throughout the Pismo Data Protection Governance Policy.

Pismo Data Protection Governance Policy covers all personal data collected, accessed, used, managed, stored, disclosed, transferred, or otherwise processed by Pismo. The Governance Policy applies to all directors, officers, managers, and employees (current and former, including candidates) of Pismo (collectively referred to as "Employees") and to third parties who collect and process personal data on behalf of Pismo.

## Defined ownership of data during partnership with customers

Our license is a limited, non-exclusive, revocable, and non-transferable license to use the Pismo platform in accordance with the terms and for the duration of the agreement. As a SaaS platform, Pismo offers a standard non-exclusive service throughout our client base. Any non-standard services or requests do not form part of our offering and would always be subject to a separate agreement and discussions.

Except as provided in the agreement, no intellectual property rights are assigned, licensed, or otherwise transferred from one party to the other. Pismo’s intellectual property remains with Pismo at all times and extends to any development, invention, or update made by Pismo or on our behalf. 

Pismo believes in our products and, as a result, Pismo offers an IP indemnity in line with market standards and allows clients to terminate the agreement for convenience (fees may apply).

## Customer data reporting types

The Pismo platform provides data streams for transactions, authorization, clearing files, interchange, and so on. It also supplies all necessary data to support report creation.

Clients can use our data streams to integrate with existing reporting systems or use our partner reporting solutions. Refer to the [Data and reporting overview ](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview)guide for more information on data events architecture.

Data stored includes customer name, address, DOB and contact details. Refer to the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint reference for data attributes. 

The Pismo platform publishes business events for customer and account updates. Refer to the [Account due date changed](https://developers.pismo.io/events/docs/account-due-date-update-1) event for details.

## Data retention policy

Pismo follows defined policies regarding retention of records and information,  summarized as follows:

* Records and information are retained and disposed of in accordance with a retention schedule.
* Records remain readable, immutable, retrievable, and accessible throughout their required retention period.
* Records are protected in safe and secure conditions.
* Once a record has been finalized, drafts and working copies become non-record information and are not retained as records unless instructed by the Legal Department that destruction has been suspended, such as for active or anticipated litigation, audit, or government investigation (“Legal Hold”).
* Records and information are kept for no longer than necessary for their identified business purpose unless subject to additional legal or regulatory requirements.
* Personal information that has been de-personalized or otherwise rendered unusable and unidentifiable pursuant to applicable privacy regulations is presumed to be compliant with the policy.
* All records and information created pursuant to our business activities are proprietary information and do not belong to an individual. All employees are required to return records and information upon request or when leaving the company. Staff also ensures that third parties return all records and information upon request or termination of contract.

## Data location to avoid crossing national or regional boundaries

When data is transferred across jurisdictions, the Pismo platform defines data sharing agreements that clarify the purpose, outline each stage of the data lifecycle, set standards, and specify the roles and responsibilities of all parties.

Data is stored in the same region as the running applications. Customers confirm this setup before production begins. Backup data can be stored in any available AWS region, based on customer preferences and applicable regulatory requirements.

## Data privacy

Pismo monitors and complies with all applicable data privacy legislation. For details, refer to the compliance and certifications lists.

# Data backup and recovery

## Business continuity plan and disaster recovery (BCP/DR)

Pismo Business Continuity Plan and Disaster Recovery (BCP/DR) is a platform-wide plan that contains detailed tasks. The platform is configured to process customer data requests regardless of disruptions and outages. The data will continue to flow even if an entire region is offline (Multi-Region Approach Active/Passive) or if an Availability Zone fails (Multi-AZ Approach Active/Active) with applications and their components configured to run simultaneously across these regions or availability zones. 

Customers select the hosting regions. To protect data location regulations or commitments regarding geographic locations of data, the platform does not automatically transfer services to other regions.

**Business Continuity Plan**

The AWS Business Continuity Plan (BCP) outlines measures to avoid and lessen environmental disruptions. It includes operational details about steps to take before, during, and after an event. The BCP is supported by scenario simulation testing. AWS tracks performance, corrective actions, and lessons learned to improve response and recovery.

**BCP/DR Management**

Pismo’s Information Security team is responsible for the oversight of the Business Resiliency program, while a rotating Incident Commander is responsible for the management and resolution of all incidents. The Incident Commander always has operational and engineering personnel on call, along with playbooks for all actions that may need to be taken.

**BCP/DR Testing**

Pismo performs operational processes that support BCP/DR testing of the platform on a more frequent basis than our full annual BCP/DR testing. Each month, Pismo performs load swings from the live environment while we perform updates to the systems running the service. This process involves taking down entire AZs while the load is handled by the other AZs. During this process, after any updates are performed, all AZs are brought back up, and all services go live again to verify that no issues were introduced.

Pismo uses tools and techniques to drain traffic and send a small percentage of traffic to recently updated services (canary deployments) to check for any issues or errors before going back to full load processing. In multi-region environments, traffic for one region is fully shifted to the other region, validating platform consistency.

In addition to the operational processes described above, Pismo conducts full BCP/DR exercises at least once annually, where engineering and operations team members test a real disaster scenario. This provides additional training and experience for our personnel on our larger BCP/DR plans for the enterprise besides the service itself.

Pismo maintains Playbooks for use by all operational and engineering teams. These playbooks are reviewed and updated at least annually and used in all BCP/DR testing and training exercises.

Customers can access annual BCP/DR test reports upon request. The results of our operational tasks and annual DR exercise test reports are also shared with Pismo’s third-party auditors. The annual reports form the basis for the auditor's review of our compliance with PCI, ISO, contractual, and other requirements.

## Data storage

Some key points of Pismo’s data storage:

* **Backup Policy**—Pismo has a strong and consistent backup policy in place to ensure adequate protection.
* **Offline Backups**—Offline backups are created and kept separate in a different location (backup vault).
* **Data Recovery**—Pismo has implemented appropriate backup mechanisms to ensure compliance with identified requirements for recovery of data created at the hosting/solution provider.

## Data leakage detection

Pismo uses a set of practices to detect, respond, and recover in case of incidents involving confidentiality. The process includes:

* Granular monitoring and auditing of all resources that have access to the environment
* A Data Loss Prevention (DLP) solution that monitors the entire platform and devices used by the company's professionals
* Sending the monitored logs to the Security Information and Event Management (SIEM) solution and storing it according to the defined security requirements
* A Security Operations Center (SOC) team that operates 24/7 to check alerts, identify incidents and trigger our incident response team to act on incidents according to the primers adopted in Pismo
* A Threat Intelligence process where we monitor the internet, dark and deep Web, for hacker attack campaigns, data leakage, and so on

**Data mingling**

In multi-tenant mode, the tenants are segregated by a partition key at the logical level. No data access is shared between tenants. The tenant ID is also used to separate data buckets and event streams.

**Data retention management**

Our platform supports data retention policies that are fully configurable and is designed to ensure GDPR compliance to address regulatory requirements.

The Pismo platform retains data indefinitely. Pismo offers tailored data archiving solutions that align with customer-specific business and compliance needs.

# Security architecture

Security architecture refers to the structured design and organization of a company’s security controls, policies, and technologies. Its primary purpose is to ensure that systems and data are protected against threats, vulnerabilities, and unauthorized access. Security architecture provides a framework for identifying potential risks, implementing safeguards, and establishing processes for detecting and responding to security incidents. It encompasses both technical elements, such as firewalls and encryption, and procedural aspects, such as access management and compliance with regulations. By taking a holistic approach, security architecture helps organizations to maintain the confidentiality, integrity, and availability of their information assets.  This includes:

* Assessing and analyzing risks to information systems 
* Designing secure network and system layouts 
* Implementing security controls like firewalls, intrusion detection, and encryption 
* Developing and enforcing access control policies 
* Monitoring systems for suspicious activities and potential breaches 
* Establishing incident response procedures and disaster recovery plans 
* Ensuring compliance with industry standards and regulations

# Security management

Pismo has a robust observability framework that gathers real-time statistics and issues alerts for various levels of monitoring including infrastructure, networks, applications, and business. Monitoring takes place through logs, metrics, and monitoring tools. Pismo uses tools for log aggregation and for observability metrics. Observability in all our services is enabled by collecting data from all requests performed inside the platform: latencies, endpoints, status code, IP, user agent, and more.

Pismo applies a DevSecOps approach early in our development life cycle. Security checks are applied into our development pipelines to guarantee that every new or modified code is inspected before being moved to the production environment. This includes a secure SDLC and thread modeling during the design phase, secure coding practices, code authentication and repository access control during development, IAST/SAST during build, IAST/DAST/Pentests during testing and monitoring through the deploy and operate phases. We use tools to ensure code quality and test coverage and to detect some security issues.

Our vulnerability assessment program is one source of input for our vulnerability management program. We periodically perform security tests in every single application, including APIs and web portals, based on OWASP and NIST methodologies. This practice aims to identify vulnerabilities mapping our attacking surface, besides supporting risk rating assessments and prioritizations.

The vulnerability assessments occur in the final stage of the development life cycle. Unlike static analysis, these are performed manually by our analysts, who put effort into finding business logic flaws and other vulnerabilities that may bypass previous automated controls.

Pismo performs internal and external penetration tests at least twice a year, one conducted by our internal Red Team and the second by an external company specialized in penetration testing.

## Enterprise-wide risk management

Pismo’s enterprise-wide risk management (ERM) approach involves identifying, assessing, managing, and monitoring risks across the organization. It aims to ensure the company's resilience and continued success by proactively addressing potential threats and opportunities. Pismo’s commitment to ERM ensures the organization remains resilient and adaptable in a dynamic risk landscape.

Key components of the ERM approach:

**Risk Identification**

* Identify potential risks that could impact the organization.
* Sources of risks include financial, operational, strategic, compliance, and reputational risks.

**Risk Assessment**

* Evaluate the likelihood and impact of identified risks.
* Prioritize risks based on their potential effect on the organization.

**Risk Management**

* Develop strategies to mitigate, transfer, accept, or avoid risks.
* Implement risk controls and response plans.

**Risk Monitoring**

* Continuously monitor risk environment and control effectiveness.
* Adjust risk management strategies as necessary.

**Risk Reporting**

* Regularly communicate risk status to stakeholders.
* Ensure transparency in risk management efforts.

**Risk Management Strategies**

* Mitigation—Implement measures to reduce the likelihood or impact of risks.
* Transfer—Shift risk to third parties (for example, through insurance).
* Acceptance—Acknowledge the risk and preparing to manage its impact.
* Avoidance—Eliminate activities that lead to risk.

**Benefits of ERM**

* Improved decision-making and resource allocation
* Enhanced ability to identify and capitalize on opportunities
* Stronger regulatory compliance and reduced legal liabilities
* Increased stakeholder confidence and trust

Pismo maintains a third-party management program to ensure an adequate level of protection for customer information and the environment. The program is composed of a rigorous evaluation process, where the controls/certifications of these service providers are analyzed based on criteria established by Pismo before contracting the service. In case the service provider does not comply with the standards accepted by Pismo, Pismo will not contract the provider. The security assessment is also carried out annually to ensure that there is no degradation in the quality-of-service providers.

## Security logs and log management

To monitor the environment's health, Pismo has a security log management process that provides practical, real-world guidance on developing, implementing, and maintaining effective log management practices throughout its operations. It not only serves security purposes but also optimizes system and network performance and auditing by recording user actions and providing useful data for investigating malicious activity.

 Pismo maintains logging mechanisms and the ability to track user activities critical in preventing, detecting, or minimizing the impact of a data compromise. Logs in all environments allow thorough tracking, alerting, and analysis when something goes wrong.

# Cloud security

Maintaining a safe and secure environment for customer data is Pismo Cloud’s highest priority. The Pismo platform secures customer data with an industry-leading information security operation that combines stringent processes, a world-class team, and multi-layered information security and privacy infrastructure. 

We have Information Security policies and guidelines in place for stringent data security measures. Pismo has a 24x7x365 Security Operations Center (SOC) in charge of threats monitoring and incident response. As preventive controls, we have AWS Config for compliance monitoring, AWS GuardDuty for IDS, CloudTrail for auditing, AWS WAF, and tools for anti-virus and FIM monitoring. Information from these tools is integrated with our SIEM tool for alerting and we have playbooks for incident response.

Security is implemented at multiple levels to ensure protection of customer data:

* **Administrative access / RBAC**—To keep data private and secure, Pismo logically isolates each customer’s Platform data from that of other customers, even when it’s stored on the same physical server. Only a small group of Pismo employees have access to customer data (Engineers and DBAs). For Pismo employees, access rights and levels are based on their job function and role (RBAC), using the concepts of least-privilege and need-to-know to match access privileges to defined responsibilities.\
  Pismo employees are only granted a limited set of default permissions to access company resources, such as employee email and internal employee portal. Requests for additional access follow a formal process that involves a request and an approval from a data or system owner, manager, or other executives, as dictated by Pismo security policies.
* **Periodical user access review**—User access review is part of the user account management and access control process, which involves a periodic review of access rights for all of Pismo’s employees and Service Providers. A user access review includes re-evaluation of:
  * User roles
  * Access rights and privileges
  * Credentials provided to users
* **Technical controls**—In cases where access to databases is required for troubleshooting reasons, users are not allowed to access, copy, or store sensitive data. Instead, they use an internal tool that allows an engineer to query some views that have access to the original tables. Once executed, those views don't expose sensitive data, as the data goes through a process of de-identification to minimize the privacy risk.  \
  We log all database activities as another security measure. Login activities are maintained for at least one year for security audits. Any account that exceeds the maximum number of failed login attempts is automatically reported to the information security operation team for investigation.
* **Identity and Access Management (IAM)**—IAM is a framework of business processes, policies and technologies that is used for the management of electronic or digital identities at Pismo. Its primary purpose is access and permission controls. With our IAM framework in place, we can control user access to critical information, access to databases, storage, and other application services.
* **Root credentials**—For root credentials, we established a “chain of custody” process where it is split among board members, and the use of these credentials are done only in strict situations. Moreover, we eliminate use of the 'root' user for administrative and daily tasks.

## Cloud failover

The Pismo platform typically across two regions with multiple availability zones within each region. There is at least one Read Replica database in each Availability Zone for disaster recovery purposes and scalability.

Failover typically completes within 30 minutes from start to finish, between the Primary instance and one Read Replica, in the event of the Primary instance failing. There is automatic failover and point-in-time recovery backup with 35 days retention and monthly backups with indefinite retention. 

Pismo restores tests quarterly audited by the ISO 27001 certification process. Pismo has worked with AWS to ensure the failover mechanism for business continuity is fully automated to eliminate human error.

## Web application firewall

Pismo’s SOC is responsible for threat monitoring and incident response. The Web Application Firewall (WAF) solution used has anti-DDoS, OWASP TOP 10, and other rules to filter and protect all internet requests. API Shield protects the APIs, enabling mTLS, and assures the advanced security protection.

Pismo’s WAFs, Cloudflare, and AWS API Shield provide protection against common and most frequently occurring infrastructure (layer 3 and 4) attacks such as SYN/UDP floods, reflection attacks, and others.

Through the stateful AWS Network Firewall, Pismo incorporates context from traffic flows, track connections, and protocol identification. It enforces policies such as preventing VPCs from accessing domains using an unauthorized protocol. Additionally,  with Network Firewall, Pismo has visibility and control of virtual private cloud traffic (VPC-to-VPC) between logically separate networks hosting sensitive applications or line-of-business resources. 

In addition, Pismo uses Cloudflare anti-DDoS to automatically detect and mitigate Distributed Denial of Service (DDoS) attacks using its Autonomous Edge.

## Digital signatures

Pismo fully supports digital signatures from an extensibility perspective. Digital signatures or certificates are supported for secure encrypted communication between application components. Webhook request payloads from Pismo are signed using Pismo's private key and customers can verify message integrity using our public keys. 

For more details on webhook requests, refer to the [Verifying webhook requests](https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests) guide.

## Web filtering controls

Pismo has adopted a defense-in-depth strategy that employs multiple, layered security controls to protect its assets against malware and other threats. If one layer is compromised, additional safeguards remain in place to intercept and contain the threat. This approach addresses vulnerabilities not only in hardware and software but also in human behavior, recognizing that negligence or error is a common cause of security breaches. 

In addition to the backups that are in place, the security controls have the following features:

* A strong and consistent backup policy is in place to assure the adequate level of protection.
* Offline backups are kept separate, in a different location (backup vault).
* Multiple copies of files are made using different backup solutions such snapshot and recovery point-in-time.
* Backups are only connected to known clean devices before starting recovery.
* Regularly patch products are used for backup, so attackers cannot exploit any known vulnerabilities they might contain.

**Malware Protection**

Controls are in place to prevent malware from being delivered to Pismo. These include:

* Filter to only allow expected file types
* Block websites that are known to be malicious
* Actively inspect content
* Use signatures to block known malicious code
* Use mail filtering in combination with spam filtering to block malicious emails and remove executable attachments
* Employ proxy and content filters to block known-malicious websites
* Maintain defined safe browsing lists which prevent access to sites known to be hosting malicious content
* Provide DNS Protection
* Ensure zero trust with MFA

## Cyber information security

Visa has a Chief Information Security Officer (CISO) and a dedicated Information Security function. The CSO oversees the company's overall security strategy, including information security, cybersecurity, and physical security. Cybersecurity measures include:

* Advanced measures to detect, prevent, and respond to cyber threats
* Regular vulnerability assessments, penetration testing, and security audits

Pismo considers an incident to be any failure or abnormal behavior of the service or system that meets at least one of the following conditions:

* Total or partial unavailability
* Impact on the use of products and services by the end customer
* Impact on the continuity of operations under the responsibility of the business areas 

The Pismo platform uses a log management process to monitor system health and security. This process records user actions and provides data that helps investigate malicious activity, improve auditing, and optimize system and network performance.

Pismo maintains logging mechanisms and can track user activities critical in preventing, detecting, or minimizing the impact of a data compromise. Logs in all environments allow thorough tracking, alerting, and analysis when something goes wrong.

Pismo maintains its own Security Operation Center (SOC) 7x24x365. The SOC operates with the SIEM solution for log aggregation and retention (90 days for immediate availability and 365 archived). All stored logs are encrypted, and access to them is only allowed through the SEIM's portal. The Pismo Security Operation Center team also supports and protects against cyber-attacks.

The SOC team effectively manages security incidents through the following:

* **Investigates potential incidents**—SIEM generates alerts based on use cases defined by Pismo (using its internal and external sources as references based on threat model standards such as MITRE ATT\&CK and PCI DSS). SOC analysts dig into all potential incidents to determine if it is a real attack or a false positive.
* **Triages and prioritizes detected incidents**—Once an incident has been identified, it is triaged and prioritized to optimize resource utilization and minimize enterprise risk.
* **Coordinates an incident response**—Responding to an incident requires engagement with multiple stakeholders and the use of a variety of different tools. The SOC team orchestrates this process to ensure that oversights do not result in delayed or incomplete remediation. Playbooks support Pismo with a standard set of procedures to timely identify, coordinate, remediate, recover, and track successful mitigations from incidents and vulnerabilities affecting Pismo's systems, data, and networks.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |

### Operation essentials

- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/get-started/pismo-platform-security-guide.md`: updatedAt 2026-06-30T14:11:30.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/pismo-platform-security-guide.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide | `b2d4194de59ac6db…` | 2026-06-30T14:11:30.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-AUTH-authentication-methods` — API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys
- `KU-AUTH-identity-connectivity-with-mtls` — Identity connectivity with mTLS
- `KU-AUTH-security-programme` — Security programme: compliance, certifications, audits and incident response
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-verifying-webhook-requests` — Verifying webhook requests
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
