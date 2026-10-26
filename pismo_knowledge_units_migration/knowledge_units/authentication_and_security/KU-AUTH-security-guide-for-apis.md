---
ku_id: KU-AUTH-security-guide-for-apis
title: Security guide for APIs
category: authentication_and_security
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/security-guide-for-apis.md
  sha256: 8c52e5f7e5f46c930e33d7a4198073127f5fc9216bf6bb108bd9faa2e6552980
  url: https://developers.pismo.io/pismo-docs/docs/security-guide-for-apis
  role: primary_guide
  updated_at: '2026-06-16T14:28:40.000Z'
operations: []
related_kus:
- KU-AUTH-authentication-methods
grouping_rationale: single source page
---

# Security guide for APIs

**KU ID:** `KU-AUTH-security-guide-for-apis` · **Category:** Authentication and security · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/get-started/security-guide-for-apis.md`:

> Pismo is committed to providing you with a trusted set of financial services. We have used our cloud industry experience building enterprise software and running some of the world’s largest online services to create and implement a robust set of security technologies and practices. These practices help reduce the cost, complexity, and risk associated with security in the financial services cloud. Our mission is to deliver the highest levels of security, privacy, compliance, and availability to the financial sector and help you protect your business assets. Pismo invests annually in cybersecurity and employs dedicated cybersecurity professionals. We take a defense-in-depth approach to security on the Pismo platform, helping you strengthen your security posture, streamline your compliance efforts, and enable digital transformation.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/security-guide-for-apis.md`: Security guide for APIs; API access control; API permission groups; API authentication; Server-to-server authentication; PingID security for Pismo Control Center; Security profiles; Identity and access management; Encryption management; Transport encryption; Encryption at rest; Security incident management; Security log management; Vulnerability assessment; Vulnerability management; Penetration testing; Pismo Secure Software Development Lifecycle (SSDLC) process; Core principles; Key components of the SSDLC; Benefits of Pismo's SSDLC; Pismo Business Continuity and Disaster Recovery (BCP/DR); Key components; Customer benefits; Security certifications and compliance; Governance, Risk, and Compliance (GRC); Certifications; Compliance; Pismo security teams; Pismo Blue Team—defensive security excellence; Roles and responsibilities; Pismo Red Team—offensive security excellence; Core services; Methodology; Why choose the Pismo Red Team?; Pismo Security Architecture Team—defense-in-depth; Core Principles; Key responsibilities; Advanced practices inspired by Visa; Customer benefits

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/security-guide-for-apis.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/security-guide-for-apis · updatedAt: 2026-06-16T14:28:40.000Z

<!-- source:begin path=docs/get-started/security-guide-for-apis.md part=0-end -->

# Security guide for APIs

Pismo is committed to providing you with a trusted set of financial services. We have used our cloud industry experience building enterprise software and running some of the world’s largest online services to create and implement a robust set of security technologies and practices. These practices help reduce the cost, complexity, and risk associated with security in the financial services cloud. Our mission is to deliver the highest levels of security, privacy, compliance, and availability to the financial sector and help you protect your business assets. Pismo invests annually in cybersecurity and employs dedicated cybersecurity professionals. We take a defense-in-depth approach to security on the Pismo platform, helping you strengthen your security posture, streamline your compliance efforts, and enable digital transformation.

The Pismo platform follows an API-driven architecture. This design allows for seamless integration with various systems and services that you may have. Many of our customers chose to build their own UI on top of the Pismo platform. This method allows you to control all access and authentication to the Pismo platform, including single sign-on (SSO) and multi-factor authentication (MFA) policies. You can also access the Pismo platform through Pismo Control Center.

# API access control

Pismo supports OpenID Connect (OIDC) for servers which enables you to give a third party access to a restricted set of Pismo endpoints that they can use within your organization.

For more details, refer to the [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid#server-authentication)  and the [Third-party authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/third-party-authentication-with-openid) guide.

## API permission groups

When using OIDC, you must also include a permission group that controls whether the token can access an endpoint. For example, you could use the group `pismo-v2:bankaccounts:rw`.

From Control Center, you can access the list of permission groups and identify which groups have access to each endpoint.

## API authentication

Authentication validates the identity of a user. It is typically handled by checking credentials, such as usernames and passwords, against an established database of credentials within an identity and access management (IAM) service. It also includes multi-factor authentication (MFA).

In-app, SMS OTP, Email OTP, or call center step-up authentication options can all be configured on the Pismo platform. Pismo offers non-mobile based authentication options via our partnership with solutions like Entersekt which support FIDO security keys.

### Server-to-server authentication

Current server-to-server authentications that the Pismo platform supports:

* Authentication with OpenID connect (recommended option)
* Basic authentication with customer credentials (key/secret)
* Authentication with OAuth2

From a connectivity point of view, the Pismo platform supports mTLS or PrivateLink for customers on AWS.

Pismo’s specialized partners support document verification. Each partner is selected to provide fast decisions and offer a failover approach, if needed. Fully automated routes are also available for verification.

# PingID security for Pismo Control Center

PingID federation in Pismo Control Center enables organizations to integrate their own Identity Provider (IdP) with the Pismo platform. This approach allows users to authenticate using their corporate credentials while leveraging the customer’s existing security policies and infrastructure. By delegating identity management to the customer’s IdP, federation reduces the risk of credential exposure, supports compliance requirements, and provides flexibility for enforcing advanced security controls such as conditional access and device trust.

**Seamless Single Sign-On (SSO) integration**

PingID federation allows customers to connect their IdP to the Pismo platform, enabling users to log in with corporate credentials. This eliminates password fatigue and reduces the risk of credential compromise.

**Strong Multi-Factor Authentication (MFA)**

PingID supports multiple MFA options:

* Email-based MFA (default for all users)
* Authenticator Apps (Google Authenticator, Microsoft Authenticator, and so on)
* FIDO2 and Passkey for advanced security

This layered approach ensures robust protection against unauthorized access.

**Security advantages of Federation**

* **Customer-managed access**—Full control over authorization and user/group management via the customer’s IdP
* **Reduced attack surface**—Credentials never reside in Pismo systems
* **Context-aware policies**—Enforce conditional access and device trust through the customer’s IdP
* **Scalability**—Ideal for multi-customer environments and organizations with multiple subsidiaries

**Compliance and audit readiness**

Federation supports audit-ready identity flows and clear role ownership, helping meet regulatory requirements such as PCI DSS and SOC 2.

**Continuous security hygiene**

We monitor the user lists for inactive users. Recently, we removed over 300 inactive users from the Control Center, reducing risk and improving operational hygiene.

# Security profiles

Restrictions can be added at the account level using account status and flex controls.

All Pismo features are accessible via APIs. You can integrate Pismo APIs to your back-office tools to extend a modern banking stack to your existing interfaces. Pismo also provides a hosted interface to handle these aspects:

* Create/manage/configure products
* Customer service portal to lookup account details and transactions, and manage account/card lifecycle

## Identity and access management

Identity and access management (IAM) is a framework of business processes, policies, and technologies that are used for the management of digital identities at Pismo. Through the IAM system, the Pismo platform manages access to databases, storage, and other application services.

# Encryption management

## Transport encryption

The Pismo platform enforces HTTPS connections using the TLS v1.2 protocol for all connections to internet-facing websites/services. We configure a secure SSL/TLS configuration and cipher suite to maintain an A+ rating on Qualys’s SSL Labs scanner.

## Encryption at rest

All customer data stored on AWS EBS volumes, S3 buckets, RDS volumes, and Redshift is encrypted using AWS Key Management Service (KMS). AWS KMS utilizes AES-256 encryption in GCM mode to encrypt data. Pismo uses KMS to generate and manage cryptographic keys and operates as a cryptographic service provider for protecting data.

Pismo encrypted database (DB) instances use the industry standard AES-256 encryption algorithm to encrypt data on the DB instances. After data is encrypted, the Pismo platform handles authentication of access and decryption of data transparently with minimal impact on performance. In addition, all logs, backups, and snapshots are encrypted.

# Security incident management

Pismo has Information Security policies and guidelines in place for stringent data security measures. There is a 24x7x365 Security Operation Center (SOC) in charge of threat monitoring and incident response. The SOC operates with the IBM QRADAR SIEM Solution for log aggregation and retention.

As preventive controls, Pismo has AWS Config for compliance monitoring, AWS GuardDuty for IDS, CloudTrail for auditing, AWS WAF, Trend Micro Deep Security for anti-virus, and FIM monitoring. Information from these tools is integrated with Pismo’s Security Information and Event Management (SIEM) tool for alerting, and there are playbooks for incident response.

## Security log management

Pismo has a security log management process to monitor the environment's health and maintain logging mechanisms to track user activities.

# Vulnerability assessment

Pismo’s comprehensive vulnerability assessment program plays a vital role in strengthening our overall vulnerability management strategy. Pismo conducts regular, in-depth security evaluations across all applications—including APIs and web portals—using industry-standard methodologies such as OWASP and NIST. This proactive approach enables us to identify, assess, and mitigate potential security risks before they can be exploited.

The vulnerability assessments occur during the development lifecycle because of the Shift Left approach implemented by the DevSecOps  practice as part of our SSDLC. Unlike static analysis, these assessments are performed manually by our analysts, who put effort into finding business logic flaws and other vulnerabilities that may bypass previous automated controls.

# Vulnerability management

Pismo’s vulnerability management program is a proactive security initiative designed to prevent the exploitation of IT vulnerabilities. It helps reduce the time and cost associated with identifying and addressing potential threats. As part of its commitment to secure development practices, the company adopts a Shift Left approach, integrating security early in the software development lifecycle to detect and remediate vulnerabilities before they progress to later stages.

## Penetration testing

Pismo performs internal and external penetration tests at least twice a year, one conducted by our internal Red Team and the second by an external company that specializes in penetration testing.

# Pismo Secure Software Development Lifecycle (SSDLC) process

At Pismo, security is embedded into every stage of the software development lifecycle. Our Secure Software Development Lifecycle (SSDLC) ensures that security is not an afterthought but a core component of our engineering culture. This approach enables us to deliver innovative solutions while maintaining compliance with global standards such as ISO 27001, PCI DSS, and SOC 2.

### Core principles

* **Security by design**—Every system, project, or application begins with defined security requirements. Threat modeling is mandatory during repository creation, ensuring risks are identified early.
* **Continuous integration of security**—Automated pipelines enforce security checks at every stage. Vulnerable code cannot be merged into the main branch, thanks to tools like Checkmarx SAST, which provide real-time feedback to developers.
* **Early vulnerability detection**—Using a Shift Left approach, security scans and assessments occur during development, reducing remediation costs and improving efficiency.

### Key components of the SSDLC

* **Repository governance**—All new repositories require approval from the Red Team and completion of a threat modeling assessment before development begins.
* **Automated security pipeline**—Integrated tools perform static analysis (SAST), infrastructure-as-code (IaC) checks, and software composition analysis (SCA) to detect vulnerabilities early.
* **Infrastructure as Code (IaC) security**—IaC templates (Terraform, CloudFormation) are scanned for misconfigurations and compliance violations before deployment. This ensures secure cloud provisioning and prevents configuration drift.
* **Software Bill of Materials (SBOM)**—Every build generates an SBOM to provide full visibility into third-party components and dependencies. This enables rapid vulnerability identification and compliance with supply chain security requirements.
* **Penetration testing and vulnerability management**—Regular penetration tests and monthly vulnerability scans ensure continuous security posture improvement. Identified issues are remediated based on severity within defined SLAs.
* **Secure coding training**—All engineers undergo annual training based on OWASP guidelines, with content updated regularly to reflect emerging threats and KPIs.
* **Compliance and governance**—Processes are reviewed annually to align with evolving regulations and industry standards. Security logs are retained for 365 days for audit readiness.

### Benefits of Pismo's SSDLC

* **Proactive risk mitigation**—Vulnerabilities are addressed before deployment
* **Regulatory compliance**—Meets global standards for financial services security
* **Operational efficiency**—Reduces cost and time associated with late-stage fixes
* **Customer trust**—Demonstrates commitment to safeguarding sensitive data

# Pismo Business Continuity and Disaster Recovery (BCP/DR)

At Pismo, the safety and reliability of our services are paramount. Our BCP and DR programs are designed to ensure uninterrupted operations and compliance with global standards, even in the face of major disruptions. These plans cover platform resilience, operational readiness, and customer communication protocols. The core principals include:

* **Platform-Wide Resilience**—Pismo’s architecture supports multi-AZ active/active configurations to maintain operations even if an entire availability zone becomes unavailable.
* **Regulatory Alignment**—Our BCP/DR processes comply with PCI DSS, ISO 27001, SOC 2, and contractual obligations.

### Key components

**Preparedness for disruption**

* Plans ensure continuity during severe events, including geopolitical risks or natural disasters.
* Critical providers maintain their own BCP/DR strategies, aligned with Pismo’s standards.

**Multi-AZ architecture**

* Services run simultaneously across multiple availability zones.
* Traffic can be shifted between zones without service interruption, validating platform consistency.

**Backup strategy**

* **Point-in-time backups**—Continuous snapshots of critical data allow restoration to a specific moment, minimizing data loss during incidents.
* **Air-gapped storage**—Backups are stored in isolated environments, disconnected from production systems, to protect against ransomware and malicious attacks.

**Testing and validation**

* **Annual BCP/DR exercises**—Full-scale disaster simulations involving engineering and operations teams.
* **Monthly operational tests**—Load swings and failover drills, including taking down entire AZs and validating recovery
* **Canary deployments and traffic draining techniques**—To ensure safe updates before full load processing

**Playbooks and governance**

* Detailed playbooks guide operational and engineering teams during incidents.
* Reviewed and updated annually, used in all BCP/DR exercises and training sessions.

**Incident management**

* Oversight by the Information Security team.
* A rotating Incident Commander coordinates response actions with on-call personnel and predefined playbooks.

**Customer communication**

* Dedicated communication channels ensure timely updates during BCP activation.
* Customers receive advance notice of scheduled recovery tests and post-test reports.

### Customer benefits

* **Uninterrupted service**—Designed to maintain operations even during zone-level outages
* **Data integrity**—Point-in-time backups and air-gapped storage ensure secure recovery
* **Transparency**—Customers receive detailed reports and can request auditor-reviewed compliance documentation
* **Proactive risk management**—Regular testing and continuous improvement ensure readiness for any scenario

# Security certifications and compliance

Upon request, Pismo will provide all necessary information to demonstrate compliance with contractual obligations and Data Protection Laws. Customers may contribute to audits and inspections to verify Pismo’s compliance, provided reasonable notice is given. All audit participants must sign a non-disclosure agreement.

## Governance, Risk, and Compliance (GRC)

In the fast-evolving fintech landscape, Pismo understands that trust, resilience, and regulatory alignment are essential. Our Governance, Risk, and Compliance (GRC) program is designed to help financial technology providers operate securely and confidently, while meeting global standards and regional data protection laws.

**Governance**

Security and compliance are embedded into Pismo’s strategic and operational processes. Our policies are reviewed and approved by senior leadership and are continuously updated to reflect evolving regulatory expectations and industry best practices.

Pismo maintains a strong governance posture through:

* **A formal security program aligned with ISO/IEC 27001**—Supporting structured and accountable information security management
* **Independent audits and internal reviews**—To validate our controls and maintain transparency
* **Certification in SOC 2 Type II**—Demonstrating our commitment to safeguarding data across security, availability, and confidentiality dimensions
* **Cyber Essentials Plus certification**—Reinforcing our protection against common cyber threats.

**Risk management**

Pismo’s security maturity is reflected in our proactive and structured approach to risk management, aligned with the NIST Cybersecurity Framework (CSF). This includes:

* **Identify**—Continuous asset and risk identification across our infrastructure and services
* **Protect**—Implementation of layered security controls to safeguard data and systems
* **Detect**—Real-time monitoring and alerting to identify potential threats
* **Respond**—Documented incident response procedures to contain and mitigate risks
* **Recover**—Business continuity and recovery plans to ensure service resilience.

Pismo also maintains:

* **PCI DSS compliance**—Ensuring secure handling of cardholder data
* **PCI PIN Security certification**—Validating our secure management of PIN data in payment environments

In addition, Pismo aligns its internal risk practices with the Visa Enterprise Risk Management Program, which promotes a structured approach to identifying, assessing, and mitigating risks across the payment ecosystem. This includes:

* Proactive vulnerability management and remediation
* Risk-based prioritization of security controls
* Ongoing collaboration with partners to strengthen the overall security posture

**Compliance**

Pismo’s platform is designed to support fintech customers in meeting their own regulatory obligations, including:

* **Lei Geral de Proteção de Dados (LGPD)**—Pismo ensures that personal data of Brazilian users is processed lawfully, transparently, and securely, with clear data subject rights and consent mechanisms.
* **General Data Protection Regulation (GDPR)**—For customers operating in or serving the EU, Pismo supports compliance with GDPR principles such as data minimization, purpose limitation, and lawful processing. We offer mechanisms for data subject access requests, consent management, and data breach notification.

Our data protection practices include:

* Encryption of sensitive data both at rest and in transit
* Tokenization of cardholder data to reduce exposure and simplify compliance
* Granular access controls to ensure that only authorized personnel can access sensitive information

These measures are part of a mature and continuously evolving security program that enables fintechs to innovate confidently, knowing their data and operations are protected by globally recognized standards.

## Certifications

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Certification
      </th>

      <th>
        Notes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ISO 27001
      </td>

      <td>
        ISO 27001 is a globally recognized independent security standard. Pismo has achieved certification for the systems, technology, and processes that support the Pismo platform.

        Our compliance with the international standard was certified by BSi, the United Kingdom's national standards organization and its representative in the European CEN and the international ISO and IEC.
      </td>
    </tr>

    <tr>
      <td>
        PCI-DSS Level 1
      </td>

      <td>
        PCI DSS applies to entities that store, process, or transmit cardholder data (CHD) or sensitive authentication data (SAD), including merchants, processors, acquirers, issuers, and service providers. The PCI DSS is mandated by the card brands and administered by the Payment Card Industry Security Standards Council.

        Pismo is certified as a PCI DSS Level 1 Service Provider, the highest level of assessment available.

        The compliance assessment was conducted by GM Sectec, an independent Qualified Security Assessor (QSA). The PCI DSS Attestation of Compliance (AOC) and Responsibility Summary are available to customers upon request to our Technical Account Team.
      </td>
    </tr>

    <tr>
      <td>
        PCI-PIN Security
      </td>

      <td>
        The Pismo platform has PCI PIN security certification.
      </td>
    </tr>

    <tr>
      <td>
        ISAE 3402 SOC1, SOC2 Type II
      </td>

      <td>
        The Pismo platform complies with SOC 1 and 2 standards.
      </td>
    </tr>

    <tr>
      <td>
        Cybersecurity Essentials
      </td>

      <td>
        The Pismo platform maintains this certification required by the UK government.
      </td>
    </tr>

    <tr>
      <td>
        SAR Data Localization
      </td>

      <td>
        The Pismo platform maintains this certification/audit required by the Reserve Bank of India (RBI).
      </td>
    </tr>
  </tbody>
</Table>

## Compliance

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Regulation
      </th>

      <th>
        Compliance notes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        European Banking Authority (EBA)
      </td>

      <td>
        Pismo complies with all the required guidelines set by the EBA and national European banking authorities as applicable to an issuing processing platform.
      </td>
    </tr>

    <tr>
      <td>
        General Data Protection Regulation (GDPR)
      </td>

      <td>
        The Pismo platform supports data retention policies and is designed to ensure GDPR compliance to address regulatory requirements. 

        Pismo’s robust privacy framework addresses any local regulations, demonstrating commitment to meeting global standards of data protection and financial security.

        The Pismo platform is built with security and data sharing controls considering data related regulations across the world including GDPR.
      </td>
    </tr>

    <tr>
      <td>
        Lei Geral de Proteção de Dados (LGPD)
      </td>

      <td>
        (General Personal Data Protection Law) The Pismo platform is built with security and data sharing controls considering data-related regulations across the world including LGPD in Brazil.
      </td>
    </tr>

    <tr>
      <td>
        Digital Personal Data Protection (DPDP)
      </td>

      <td>
        The Pismo platform is built with security and data sharing controls considering data-related regulations across the world including DPDP in India.
      </td>
    </tr>

    <tr>
      <td>
        Personal Data Protection Act (PDPA)
      </td>

      <td>
        The Pismo platform is built with security and data sharing controls considering data-related regulations across the world including PDPA in Singapore and the Philippines.
      </td>
    </tr>

    <tr>
      <td>
        Information Security Manual (ISM)
      </td>

      <td>
        Pismo complies with ISM, the Australian government’s primary Cloud compliance and security regulation. It is enforced through Infosec Registered Assessors Program (IRAP).
      </td>
    </tr>

    <tr>
      <td>
        Consumer Privacy Act (CCPA)
      </td>

      <td>
        Pismo complies with CCPA, the data privacy act for the state of California in the United States.
      </td>
    </tr>

    <tr>
      <td>
        MaRisk (German risk management)
      </td>

      <td>
        The Pismo platform is built with security and data sharing controls considering data related regulations across the world including MaRisk in Germany.

        Pismo always complies with all required guidelines set by the EBA and national European banking authorities as applicable to our platform and services alone.

        Given we are a technology business, we expect our customers to understand and adhere to all regulatory compliance and hold the relevant licenses required as part of their overall offering.
      </td>
    </tr>

    <tr>
      <td>
        Open banking
      </td>

      <td>
        In the context of Open Banking, Pismo provides the APIs that fetch the details of the transactions that would be required by an AI security platform (AISP). Standing orders, beneficiaries, direct debits are typically stored at the customer side. The API to initiate a payment on the account is held in the Pismo platform, which would be required for a payment initiation service provider (PISP).
      </td>
    </tr>

    <tr>
      <td>
        Revised Payment Services Directive (PSD2)
      </td>

      <td>
        Pismo supports PSD2 compliance requirements in relation to dynamic linking. A fraud detection engine monitors for signs of malware infection and SIM swap by analyzing data from multiple sources, such as mobile app activity and customer behavior across channels. Fraud technology partners are available to help you implement these protections.
      </td>
    </tr>

    <tr>
      <td>
        India Data Localization
      </td>

      <td>
        Pismo complies with applicable data localization requirements under Indian regulations, ensuring that payment-related and sensitive personal data is stored and processed within India when required. Our infrastructure and operational controls are designed to support region-specific data residency mandates, helping customers meet regulatory expectations without compromising performance or security.
      </td>
    </tr>
  </tbody>
</Table>

<br />

# Pismo security teams

## Pismo Blue Team—defensive security excellence

The Pismo Blue Team exists to safeguard the organization’s digital ecosystem by proactively defending against cyber threats and ensuring operational resilience. Its purpose extends beyond reactive incident handling—it is a strategic function designed to:

* **Protect customer trust**—Guarantee the confidentiality, integrity, and availability of customer data and financial transactions
* **Ensure regulatory compliance**—Maintain adherence to global standards such as PCI DSS, SOC 2, ISO 27001, and GDPR through robust security controls and documented processes
* **Enable business continuity**—Minimize downtime and financial impact by rapidly containing and mitigating security incidents
* **Drive security maturity**—Continuously improve detection, response, and prevention capabilities through automation, threat intelligence, and alignment with frameworks like MITRE ATT\&CK
* **Collaborate across teams**—Act as the central defensive hub, working with Red Team, DevSecOps, Governance, and Engineering to embed security into every layer of operations

### Roles and responsibilities

The Blue Team operates as a multi-disciplinary defense unit, covering several critical domains:

**Threat detection and monitoring**

* Operates advanced SIEM platforms to monitor billions of logs and events across cloud, application, and network layers
* Implements behavioral analytics and anomaly detection to identify suspicious activities early

**Incident response and containment**

* Executes predefined playbooks for rapid containment of threats such as credential compromise, fraud attempts, and cloud misconfiguration
* Coordinates with OpsGenie for automated escalation and task assignment during critical incidents

**Threat intelligence and analysis**

* Maps adversary behaviors to MITRE ATT\&CK tactics and techniques for structured threat hunting
* Analyzes indicators of compromise (IoCs) and shares intelligence internally to strengthen preventive measures

**Vulnerability management**

* Collaborates with DevSecOps to remediate vulnerabilities identified through AWS Security Hub, IaC scans, and SBOM analysis
* Participates in monthly Vulnerability Committee meetings to prioritize fixes based on risk and compliance impact

**Governance and communication**

* Maintains clear documentation for incident reporting and escalation via Jira and Service Desk
* Provides customer-facing guidelines for security incident handling and participates in tabletop exercises to validate readiness

**Automation and tooling**

* Leverages Cloudflare automation scripts for IP blocking and WAF rule updates
* Integrates IaC security checks and SBOM generation into CI/CD pipelines for proactive risk reduction

## Pismo Red Team—offensive security excellence

The Pismo Red Team is a specialized cybersecurity unit focused on simulating real-world attacks to identify weaknesses before adversaries do. Our mission is to strengthen your security posture by testing systems, processes, and people under realistic threat scenarios. The Red Team objectives include:

* **Validate security controls**—Ensure that implemented defenses work as intended
* **Measure organizational resilience**—Assess how fast and effective the team's response is to attacks
* **Expose hidden risks**—Identify vulnerabilities in applications, infrastructure, and operational workflows
* **Enhance Blue Team readiness**—Provide actionable insights to improve detection and response capabilities

### Core services

**Red Team engagements**

* Simulate advanced persistent threats (APTs) and targeted attacks
* Operate stealthily under predefined objectives (for example, data exfiltration, privilege escalation)
* Deliver comprehensive reports with remediation guidance

**Penetration testing**

* Exploit vulnerabilities to demonstrate real-world impact
* Assess technical and business risks across APIs, applications, and networks
* Use both manual and automated techniques for thorough coverage

**Development process assessments**

* Test security controls from API development to deployment
* Identify gaps such as protected branch bypass, pipeline enforcement failures, and Dockerfile manipulation risks
* Provide prioritized remediation plans for critical findings

### Methodology

* **Framework Alignment**—Exercises follow industry best practices and standards
* **Attack Narrative Simulation**—Realistic scenarios such as CI/CD pipeline bypass and container privilege escalation
* **Continuous Improvement**—Findings feed into SSDLC and DevSecOps processes for long-term resilience

### Why choose the Pismo Red Team?

* **Proactive Risk Reduction**—Identify and fix vulnerabilities before they become incidents
* **Regulatory Compliance Support**—Align with PCI DSS, SOC 2, and ISO 27001 requirements
* **Tailored Engagements**—Custom scenarios based on your business context and threat landscape
* **Collaboration with Blue Team**—Joint exercises to improve detection and response capabilities

## Pismo Security Architecture Team—defense-in-depth

The Pismo Security Architecture Team is a cornerstone of our defense-in-depth strategy, ensuring security is embedded into every layer of our platform. Similar to leading global payment networks, we combine multi-layered security, operational resilience, and ecosystem integrity to protect sensitive data and maintain trust.

The team’s mission is to design and maintain a secure, scalable, and resilient architecture that meets global compliance standards such as PCI DSS, ISO 27001, SOC 2, and GDPR, while enabling innovation and operational efficiency.

### Core Principles

* **Defense-in-depth**—Multiple layers of security controls across infrastructure, applications, and data
* **Zero trust**—Continuous identity validation and least-privilege access
* **Operational resilience**—Architected for high availability and disaster recovery
* **Continuous innovation**—Integration of AI-driven security solutions and proactive threat modeling

### Key responsibilities

**Security Architecture Reviews**

* Conduct in-depth assessments of applications, APIs, and cloud environments
* Perform threat modeling and design secure frameworks for new projects

**Identity and Access Management (IAM)**

Implement strong authentication flows, including mTLS, key rotation, and least-privilege design for APIs

**Reference Architecture Development**

* Maintain Security-by-Design blueprints aligned with compliance and industry standards
* Integrate security controls into CI/CD pipelines and IaC templates

**Cloud Security Posture Management**

* Monitor AWS multi-region environments for misconfigurations
* Validate compliance using automated IaC checks and CSPM tools

**Secure Development Lifecycle Support**

Enforce SSDLC practices:

* Static and dynamic code analysis (SAST/SCA)
* IaC security reviews
* SBOM generation for supply chain transparency

**Collaboration with Red Team and Governance**

* Support penetration testing and vulnerability remediation
* Align architecture decisions with risk management and compliance objectives

### Advanced practices inspired by Visa

* **AI-driven security**—Use machine learning for anomaly detection and fraud prevention
* **Dynamic risk assessment**—Apply real-time analytics to evaluate threats during transaction and API calls
* **Operational resilience**—Architect systems for 99.999% uptime, leveraging multi-region redundancy and chaos engineering tests

### Customer benefits

* **Proactive risk mitigation**—Vulnerabilities addressed before deployment
* **Regulatory assurance**—Architecture aligned with global compliance standards
* **Operational transparency**—Clear governance and documented processes
* **Resilience and scalability**—Secure design supports multi-region, high-availability architecture
<!-- source:end -->

## Lifecycle status

- `docs/get-started/security-guide-for-apis.md`: updatedAt 2026-06-16T14:28:40.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/security-guide-for-apis.md` | whole document | https://developers.pismo.io/pismo-docs/docs/security-guide-for-apis | `8c52e5f7e5f46c93…` | 2026-06-16T14:28:40.000Z |

## Related knowledge units

- `KU-AUTH-authentication-methods` — API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys
