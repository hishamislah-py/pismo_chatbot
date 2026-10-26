---
ku_id: KU-AUTH-security-programme
title: 'Security programme: compliance, certifications, audits and incident response'
category: authentication_and_security
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/security.md
  sha256: b0f81801fa15c9b2ed271e014d6bea83ddb63708e590ded751eb43c6368f102b
  url: https://developers.pismo.io/pismo-docs/docs/security
  role: primary_guide
  updated_at: '2026-06-16T14:28:40.000Z'
- path: docs/get-started/certifications-compliance-and-security-teams.md
  sha256: 0915767e175bb76d53bdbba7929a38c40466296fc460a33a42a5afc4b2b83ebe
  url: https://developers.pismo.io/pismo-docs/docs/certifications-compliance-and-security-teams
  role: primary_guide
  updated_at: '2026-06-16T14:28:40.000Z'
- path: docs/get-started/security-audit-testing-and-incident-response.md
  sha256: 716b9f082aeca48f8fc97d70914bb67a0a2f68edf1e68b2a0e62971ba5796914
  url: https://developers.pismo.io/pismo-docs/docs/security-audit-testing-and-incident-response
  role: primary_guide
  updated_at: '2026-06-16T14:28:40.000Z'
operations: []
related_kus:
- KU-AUTH-authentication-methods
- KU-AUTH-identity-connectivity-with-mtls
- KU-EVT-client-webhooks-part-01
- KU-EVT-client-webhooks-part-02
- KU-EVT-client-webhooks-part-03
- KU-EVT-client-webhooks-part-04
- KU-EVT-client-webhooks-part-05
- KU-EVT-client-webhooks-part-06
- KU-EVT-client-webhooks-part-07
- KU-EVT-client-webhooks-part-08
- KU-EVT-client-webhooks-part-09
- KU-EVT-client-webhooks-part-10
- KU-EVT-client-webhooks-part-11
- KU-EVT-client-webhooks-part-12
- KU-EVT-client-webhooks-part-13
- KU-EVT-client-webhooks-part-14
- KU-EVT-verifying-webhook-requests
grouping_rationale: Security landing page and its two organisational topics.
---

# Security programme: compliance, certifications, audits and incident response

**KU ID:** `KU-AUTH-security-programme` · **Category:** Authentication and security · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Security landing page and its two organisational topics.

Scope as stated in `docs/get-started/security.md`:

> The Pismo platform uses server-to-server authentication to maintain security. An initial request instructs Pismo to create an access token in the form of a JSON Web Token (JWT). You use this token to send subsequent requests to the platform.

Scope as stated in `docs/get-started/certifications-compliance-and-security-teams.md`:

> Upon request, Pismo will provide all necessary information to demonstrate compliance with contractual obligations and Data Protection Laws. Customers may contribute to  audits and inspections to verify Pismo’s compliance, provided reasonable notice is given. All audit participants must sign a non-disclosure agreement.

Scope as stated in `docs/get-started/security-audit-testing-and-incident-response.md`:

> Incident response is a key aspect of Pismo’s overall security and privacy program. We have a rigorous process for managing data incidents. This process specifies actions, escalations, mitigation, resolution, and notification of any potential incidents impacting the confidentiality, integrity, or availability of customer data.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/security.md`: Security
- `docs/get-started/certifications-compliance-and-security-teams.md`: Compliance, certifications, and security teams; Governance, Risk, and Compliance (GRC); Governance; Risk Management; Compliance; Regulations and regulatory groups compliance; Anti-fraud assessment and compliance; Fraud monitoring and risk assessment; Fraud detection; Anti-money laundering compliance; Fraud management services; Fraud data reports; Certifications; Pismo security teams; Pismo Blue Team – defensive security excellence; Pismo Red Team – offensive security excellence; Pismo Security Architecture team - Defense-in-depth
- `docs/get-started/security-audit-testing-and-incident-response.md`: Security audit, testing, and incident response; Security audits; Incident management, reporting, and response; Inspection rights; Security testing; Security penetration testing; Gap analysis of annual compliance; Risk controls self-assessment program; Content security policy; Vulnerability and incident management; Vulnerability assessment and management; Security incident and log management; Threat and vulnerability risk assessment; Application penetration testing

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/security.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/security · updatedAt: 2026-06-16T14:28:40.000Z

<!-- source:begin path=docs/get-started/security.md part=0-end -->

# Security

The Pismo platform uses server-to-server authentication to maintain security. An initial request instructs Pismo to create an access token in the form of a JSON Web Token (JWT). You use this token to send subsequent requests to the platform.

The server-to-server authentications Pismo supports are:

* [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials)
* [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid)
* [Authentication with OAuth2](https://developers.pismo.io/pismo-docs/docs/authentication-with-oauth2)

For more information on mTLS connectivity, refer to [Identity connectivity with mTLS](https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls).

For Zero balance or Full balance customers providing [antifraud webhooks](https://developers.pismo.io/pismo-docs/docs/client-webhooks), learn how Pismo [validates webhooks requests](https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests).
<!-- source:end -->

### Source 2: `docs/get-started/certifications-compliance-and-security-teams.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/certifications-compliance-and-security-teams · updatedAt: 2026-06-16T14:28:40.000Z

<!-- source:begin path=docs/get-started/certifications-compliance-and-security-teams.md part=0-end -->

# Compliance, certifications, and security teams

Upon request, Pismo will provide all necessary information to demonstrate compliance with contractual obligations and Data Protection Laws. Customers may contribute to  audits and inspections to verify Pismo’s compliance, provided reasonable notice is given. All audit participants must sign a non-disclosure agreement.

# Governance, Risk, and Compliance (GRC)

In the fast-evolving fintech landscape, Pismo understands that trust, resilience, and regulatory alignment are essential. Our Governance, Risk, and Compliance (GRC) program is designed to help financial technology providers operate securely and confidently, while meeting global standards and regional data protection laws.

## Governance

Security and compliance are embedded into Pismo’s strategic and operational processes. Our policies are reviewed and approved by senior leadership and are continuously updated to reflect evolving regulatory expectations and industry best practices.

Pismo maintains a strong governance posture through:

* A formal security program aligned with ISO/IEC 27001—Supporting structured and accountable information security management
* Independent audits and internal reviews—To validate our controls and maintain transparency
* Certification in SOC 2 Type II—Demonstrating our commitment to safeguarding data across security, availability, and confidentiality dimensions
* Cyber Essentials Plus certification—Reinforcing our protection against common cyber threats

## Risk Management

Pismo’s security maturity is reflected in our proactive and structured approach to risk management, aligned with the NIST Cybersecurity Framework (CSF). This includes:

* **Identify**—Continuous asset and risk identification across our infrastructure and services
* **Protect**—Implementation of layered security controls to safeguard data and systems
* **Detect**—Real-time monitoring and alerting to identify potential threats
* **Respond**—Documented incident response procedures to contain and mitigate risks
* **Recover**—Business continuity and recovery plans to ensure service resilience

Pismo also maintains:

* **PCI DSS compliance**—Ensuring secure handling of cardholder data
* **PCI PIN Security certification**—Validating our secure management of PIN data in payment environments

In addition, Pismo aligns its internal risk practices with the Visa Enterprise Risk Management Program, which promotes a structured approach to identifying, assessing, and mitigating risks across the payment ecosystem. This includes:

* Proactive vulnerability management and remediation
* Risk-based prioritization of security controls
* Ongoing collaboration with partners to strengthen the overall security posture

## Compliance

Pismo’s platform is designed to support fintech clients in meeting their own regulatory obligations, including:

* **LGPD (Lei Geral de Proteção de Dados)**—Pismo ensures that personal data of Brazilian users is processed lawfully, transparently, and securely, with clear data subject rights and consent mechanisms.
* **GDPR (General Data Protection Regulation)**—For clients operating in or serving the EU, Pismo supports compliance with GDPR principles such as data minimization, purpose limitation, and lawful processing. We offer mechanisms for data subject access requests, consent management, and data breach notification.

Our data protection practices include:

* Encryption of sensitive data both at rest and in transit
* Tokenization of cardholder data to reduce exposure and simplify compliance
* Granular access controls to ensure that only authorized personnel can access sensitive information

These measures are part of a mature and continuously evolving security program that enables fintechs to innovate confidently, knowing their data and operations are protected by globally recognized standards.

# Regulations and regulatory groups compliance

Pismo maintains compliance for the following regulations or regulatory groups.

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
  </tbody>
</Table>

# Anti-fraud assessment and compliance

## Fraud monitoring and risk assessment

Pismo has pre-integrated with some of the Fraud Risk Management (FRM) systems globally, such as FICO and Feedzai. Pismo can also integrate into a customer’s fraud-management tool, or other third-party tools for fraud monitoring service, upon request.

As part of FRM integration, Pismo will forward all the online authorization requests from Network / Scheme to the FRM tool using the anti-fraud webhook. The webhook request will consist of complete network ISO fields except the PAN and other sensitive data. PAN is replaced with a Pismo card ID when we route the transaction to an external anti-fraud system. Pismo also shares the status of card validation such as CAM, CVV2, PIN, etc., along with the rules’ validation pre-configured by the issuer at the product / account / card level. The anti-fraud system can then use the above information and scan the transaction against the fraud rules in the anti-fraud system and decide to approve or reject the transaction. Pismo host forwards the decision to the Network / Scheme with an appropriate response code.

As part of the product setup in the Pismo core, the issuer can use Pismo’s Flex Control and create rules such as restriction control or cumulative control. These rules are validated during the authorization stage (card validation and rules validation). The results are passed on to the Issuer’s anti-fraud system through the anti-fraud webhook for anti-fraud tool validation.

Pismo core is integrated into products and offerings owned by Visa (such as 3DS (ACS), authorization scoring, and VAAVRM), to automated rule writing and anti-enumeration software.

**Webhook authentication**

Pismo can connect to a customer’s webhook via mTLS connectivity or via PrivateLink if hosted on AWS. Pismo signs the payload using our private key and customers can ensure message integrity using our public keys. For details, refer to the [Verifying webhook requests](https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests) guide.

## Fraud detection

Rules can be configured on the anti-fraud partner systems or Visa VRM to decline transactions based on customers’ risk rules.

## Anti-money laundering compliance

Our platform integrates with any modern anti-money laundering (AML) platform via a real-time API call. We have pre-integrated AML, Anti-Fraud, and ID\&V partners.

Pismo has partnered with specialized vendors to service AML as well as ongoing transaction monitoring checks throughout the customer journey. These vendors can carry out Office of Foreign Assets Control (OFAC) checks.

## Fraud management services

Cards can be whitelisted to bypass authentication using rules configured on the anti-fraud systems. Pismo would invoke the anti-fraud integration for every authorization with the transaction context. Decisions from the anti-fraud layer is honored by Pismo's transaction authorization process.

## Fraud data reports

The Pismo platform offers a range of data events to support any reporting requirements of the bank. This can be supplied as raw data to the bank or a reporting partner to generate the appropriate reports, or we can curate the relevant data events in a pre-set format for the reports to be created.

Pismo triggers data events in real-time via data streams or as files. Customers consume this data and share it with their own applications as required.

Pismo's platform provides real-time alerts for potentially compromised cards based on our integration with an appropriate fraud monitoring solution. The data will be provided to the bank on a real-time basis via an event that can be consumed into an appropriate case management system.

# Certifications

Pismo maintains the following certifications.

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
        ISO27001
      </td>

      <td>
        ISO 27001 is a globally recognized independent security standard. Pismo has achieved certification for the systems, technology, and processes that support the Pismo platform.

        Our compliance with the international standard was certified by BSi, the United Kingdom's national standards organization and its representative in the European CEN and the international ISO and IEC.
      </td>
    </tr>

    <tr>
      <td>
        PCI-DSS\
        Level 1
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

# Pismo security teams

## Pismo Blue Team – defensive security excellence

The Pismo Blue Team exists to safeguard the organization’s digital ecosystem by proactively defending against cyber threats and ensuring operational resilience. Its purpose extends beyond reactive incident handling—it is a strategic function designed to:

* **Protect customer trust**—Guarantee the confidentiality, integrity, and availability of customer data and financial transactions
* **Ensure regulatory compliance**—Maintain adherence to global standards such as PCI DSS, SOC 2, ISO 27001, and GDPR through robust security controls and documented processes
* **Enable business continuity**—Minimize downtime and financial impact by rapidly containing and mitigating security incidents
* **Drive security maturity**—Continuously improve detection, response, and prevention capabilities through automation, threat intelligence, and alignment with frameworks like MITRE ATT\&CK
* **Collaborate across teams**—Act as the central defensive hub, working with Red Team, DevSecOps, Governance, and Engineering to embed security into every layer of operations

**Roles and responsibilities**

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
* Provides client-facing guidelines for security incident handling and participates in tabletop exercises to validate readiness

**Automation and tooling**

* Leverages Cloudflare automation scripts for IP blocking and WAF rule updates
* Integrates IaC security checks and SBOM generation into CI/CD pipelines for proactive risk reduction

## Pismo Red Team – offensive security excellence

The Pismo Red Team is a specialized cybersecurity unit focused on simulating real-world attacks to identify weaknesses before adversaries do. Our mission is to strengthen your security posture by testing systems, processes, and people under realistic threat scenarios. The Red Team objectives include:

* **Validate security controls**—Ensure that implemented defenses work as intended
* **Measure organizational resilience**—Assess how quickly and effectively teams respond to attacks
* **Expose hidden risks**—Identify vulnerabilities in applications, infrastructure, and operational workflows
* **Enhance Blue Team readiness**—Provide actionable insights to improve detection and response capabilities

Core services include:

**Red Team Engagements**

* Simulate advanced persistent threats (APTs) and targeted attacks
* Operate stealthily under predefined objectives (such as data exfiltration, privilege escalation)
* Deliver comprehensive reports with remediation guidance

**Penetration Testing**

* Exploit vulnerabilities to demonstrate real-world impact
* Assess technical and business risks across APIs, applications, and networks
* Use both manual and automated techniques for thorough coverage

**Development Process Assessments**

* Test security controls from API development to deployment
* Identify gaps such as protected branch bypass, pipeline enforcement failures, and Dockerfile manipulation risks
* Provide prioritized remediation plans for critical findings

**Methodology**

* **Framework Alignment**—Exercises follow industry best practices and standards
* **Attack Narrative Simulation**—Realistic scenarios such as CI/CD pipeline bypass and container privilege escalation
* **Continuous Improvement**—Findings feed into SSDLC and DevSecOps processes for long-term resilience.

**Customer benefits**

* **Proactive Risk Reduction**—Identify and fix vulnerabilities before they become incidents
* **Regulatory Compliance Support**—Align with PCI DSS, SOC 2, and ISO 27001 requirements
* **Tailored Engagements**—Custom scenarios based on your business context and threat landscape
* **Collaboration with Blue Team**—Joint exercises to improve detection and response capabilities

## Pismo Security Architecture team - Defense-in-depth

The Pismo Security Architecture Team is a cornerstone of our defense-in-depth strategy, ensuring security is embedded into every layer of our platform. Similar to leading global payment networks, we combine multi-layered security, operational resilience, and ecosystem integrity to protect sensitive data and maintain trust.

The team’s mission is to design and maintain a secure, scalable, and resilient architecture that meets global compliance standards such as PCI DSS, ISO 27001, SOC 2, and GDPR, while enabling innovation and operational efficiency.

**Core principles**

* **Defense-in-depth**—Multiple layers of security controls across infrastructure, applications, and data
* **Zero trust**—Continuous identity validation and least-privilege access
* **Operational resilience**—Architected for high availability and disaster recovery
* **Continuous innovation**—Integration of AI-driven security solutions and proactive threat modeling

**Key responsibilities**

Security Architecture Reviews

* Conduct in-depth assessments of applications, APIs, and cloud environments
* Perform threat modeling and design secure frameworks for new projects

Identity and Access Management (IAM)

* Implement strong authentication flows, including mTLS, key rotation, and least-privilege design for APIs

Reference Architecture Development

* Maintain Security-by-Design blueprints aligned with compliance and industry standards
* Integrate security controls into CI/CD pipelines and IaC templates

Cloud Security Posture Management

* Monitor AWS multi-region environments for misconfigurations
* Validate compliance using automated IaC checks and CSPM tools

Secure Development Lifecycle Support

Enforce SSDLC practices:

* Static and dynamic code analysis (SAST/SCA)
* IaC security reviews
* SBOM generation for supply chain transparency.

Collaboration with Red Team and Governance

* Support penetration testing and vulnerability remediation
* Align architecture decisions with risk management and compliance objectives

Advanced practices inspired by Visa

* AI-driven security—Use machine learning for anomaly detection and fraud prevention
* Dynamic risk assessment—Apply real-time analytics to evaluate threats during transaction and API calls
* Operational resilience—Architect systems for 99.999% uptime, leveraging multi-region redundancy and chaos engineering tests

Customer Benefits

* **Proactive risk mitigation**—Vulnerabilities addressed before deployment
* **Regulatory assurance**—Architecture aligned with global compliance standards
* **Operational transparency**—Clear governance and documented processes
* **Resilience and scalability**—Secure design supports multi-region, high-availability architecture
<!-- source:end -->

### Source 3: `docs/get-started/security-audit-testing-and-incident-response.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/security-audit-testing-and-incident-response · updatedAt: 2026-06-16T14:28:40.000Z

<!-- source:begin path=docs/get-started/security-audit-testing-and-incident-response.md part=0-end -->

# Security audit, testing, and incident response

# Security audits

## Incident management, reporting, and response

Incident response is a key aspect of Pismo’s overall security and privacy program. We have a rigorous process for managing data incidents. This process specifies actions, escalations, mitigation, resolution, and notification of any potential incidents impacting the confidentiality, integrity, or availability of customer data.

Pismo uses a security information and event management (SIEM) tool. Additionally, Pismo developed its incident management process based on ATT\&CK framework. This framework is the most suitable for our operating model and allows Pismo defenders to assess whether they can defend against specific Advanced Persistent Threats (APT) and common behaviors across multiple threat actors.

## Inspection rights

Upon customer request, we can make available all such information necessary to demonstrate compliance with the obligations laid down in the contract and Data Protection Laws and allow for and contribute to audits, including inspections conducted by the Customer for the purpose of verifying the platform's compliance, subject to the persons performing such audit being obliged to sign a non-disclosure agreement with us. We always require reasonable notice to be given for all audits.

# Security testing

## Security penetration testing

Pismo’s vulnerability assessment program is one source of input for our vulnerability management program. We periodically perform regular tests across all applications, including APIs and web portals—using industry-standard methodologies such as OWASP and NIST.

This practice aims to identify vulnerabilities mapping our attacking surface, besides supporting risk rating assessments and prioritizations.

The vulnerability assessments occur in the final stage of the development life cycle. Unlike static analysis, it is manually done by our analysts who put effort into finding business logic flaws and other vulnerabilities that may bypass previous automated controls.

Pismo performs internal and external penetration tests at least twice a year, one conducted by our internal Red Team and the second by an external company specialized in the activity.

## Gap analysis of annual compliance

Upon request, Pismo accommodates gap analysis with our customers to ensure compliance against their information security policies.

## Risk controls self-assessment program

To address risk controls self-assessment (RCSA), Pismo applies a DevSecOps approach early in the development life cycle. Security checks are applied into our development pipelines to guarantee that every new or modified code is inspected before being moved to production environment. This includes a secure SDLC and thread modeling during the design phase, secure coding practices, code authentication and repository access control during development, IAST/SAST during build, IAST/DAST/Pentests during testing and monitoring through the deploy and operate phases. We use tools for ensuring code quality and test coverage, along with detecting some security issues.

## Content security policy

Pismo’s content security policy (CSP) includes encrypted DB instances use the industry standard AES-256 encryption algorithm to encrypt data on the DB instances. After data is encrypted, Pismo handles authentication of access and decryption of data transparently with a minimal impact on performance. Beyond data, all logs, backups, and snapshots are encrypted.

Pismo uses Key Management Service (KMS) to generate and manage cryptographic keys and operates as a cryptographic service provider for protecting data.

For data in-transit, Pismo has in place OpenID Connect for Servers as the preferred way to authenticate with the Pismo platform. It provides greater security guarantees in service communications than basic authentication with client credentials. JSON Web Tokens (JWTs) are a critical part of connecting with OpenID. The Generating a JWT section of the [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid) guide explains how to generate and sign a JWT. Clients can use a mutual TLS (mTLS) structure available at Pismo platform to authentication.

# Vulnerability and incident management

## Vulnerability assessment and management

Pismo’s comprehensive vulnerability assessment program plays a vital role in strengthening our overall vulnerability management strategy. Pismo conducts regular, in-depth security evaluations across all applications—including APIs and web portals—using industry-standard methodologies such as OWASP and NIST. This proactive approach aims to identify, assess, and mitigate potential security risks before they can be exploited.

The vulnerability assessments occur in the final stage of the development life cycle. Unlike static analysis, these assessments are performed manually by our analysts, who put effort into finding business logic flaws and other vulnerabilities that may bypass previous automated controls.

Pismo’s vulnerability management program is a proactive security initiative designed to prevent the exploitation of IT vulnerabilities. It helps reduce the time and cost associated with identifying and addressing potential threats.

## Security incident and log management

Pismo has Information Security policies and guidelines in place for stringent data security measures. Pismo’s SOC is in charge of threat monitoring and incident response. The SOC operates with our SIEM solution for log aggregation and retention. There are playbooks in place for incident response.

Pismo has a security log management process to monitor the environment's health and maintain logging mechanisms to track user activities.

## Threat and vulnerability risk assessment

For threat and vulnerability risk assessment (TVRA), Pismo follows COSO-ERM methodology that analyzes assets, the likelihood of the threat, vulnerabilities, and its defined as a risk score. A risk management policy is in place and every quarter a Risk Committee discusses risks with the board and takes action against these risks.

## Application penetration testing

Pismo performs internal and external penetration tests (TVM013) at least twice a year, one conducted by our internal Red Team and the second by an external company specialized in penetration testing.
<!-- source:end -->

## Lifecycle status

- `docs/get-started/security.md`: updatedAt 2026-06-16T14:28:40.000Z.
- `docs/get-started/certifications-compliance-and-security-teams.md`: updatedAt 2026-06-16T14:28:40.000Z.
- `docs/get-started/security-audit-testing-and-incident-response.md`: updatedAt 2026-06-16T14:28:40.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/security.md` | whole document | https://developers.pismo.io/pismo-docs/docs/security | `b0f81801fa15c9b2…` | 2026-06-16T14:28:40.000Z |
| `docs/get-started/certifications-compliance-and-security-teams.md` | whole document | https://developers.pismo.io/pismo-docs/docs/certifications-compliance-and-security-teams | `0915767e175bb76d…` | 2026-06-16T14:28:40.000Z |
| `docs/get-started/security-audit-testing-and-incident-response.md` | whole document | https://developers.pismo.io/pismo-docs/docs/security-audit-testing-and-incident-response | `716b9f082aeca48f…` | 2026-06-16T14:28:40.000Z |

## Related knowledge units

- `KU-AUTH-authentication-methods` — API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys
- `KU-AUTH-identity-connectivity-with-mtls` — Identity connectivity with mTLS
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-EVT-client-webhooks-part-02` — Client webhooks (part 2 of 14)
- `KU-EVT-client-webhooks-part-03` — Client webhooks (part 3 of 14)
- `KU-EVT-client-webhooks-part-04` — Client webhooks (part 4 of 14)
- `KU-EVT-client-webhooks-part-05` — Client webhooks (part 5 of 14)
- `KU-EVT-client-webhooks-part-06` — Client webhooks (part 6 of 14)
- `KU-EVT-client-webhooks-part-07` — Client webhooks (part 7 of 14)
- `KU-EVT-client-webhooks-part-08` — Client webhooks (part 8 of 14)
- `KU-EVT-client-webhooks-part-09` — Client webhooks (part 9 of 14)
- `KU-EVT-client-webhooks-part-10` — Client webhooks (part 10 of 14)
- `KU-EVT-client-webhooks-part-11` — Client webhooks (part 11 of 14)
- `KU-EVT-client-webhooks-part-12` — Client webhooks (part 12 of 14)
- `KU-EVT-client-webhooks-part-13` — Client webhooks (part 13 of 14)
- `KU-EVT-client-webhooks-part-14` — Client webhooks (part 14 of 14)
- `KU-EVT-verifying-webhook-requests` — Verifying webhook requests
