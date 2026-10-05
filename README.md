# 🛡️ Honeypot Lab

Cloud-native honeypot and security analytics platform built as a practical laboratory for **Cybersecurity, Cloud, DevOps and DevSecOps**.

The project will progressively evolve from a local SSH honeypot into a reproducible and secure AWS-based security platform capable of collecting, storing and analyzing real attack activity from the Internet.

---

## 🎯 Objectives

The main objectives of this project are:

* Build a functional SSH honeypot.
* Capture and analyze real-world attack attempts.
* Store security events in PostgreSQL.
* Develop a REST API with FastAPI.
* Containerize the platform with Docker.
* Deploy the infrastructure on AWS.
* Manage infrastructure using Terraform.
* Implement CI/CD with GitHub Actions.
* Apply security controls throughout the entire stack.
* Implement monitoring, logging and alerting.
* Practice scalable data storage and analysis.
* Build a reproducible CloudSec/DevSecOps laboratory.

The project is intentionally developed incrementally. Each phase introduces new technologies and responsibilities.

---

## 🏗️ Architecture

The final architecture is expected to evolve towards:

```text
                              INTERNET
                                  │
                                  ▼
                         ┌─────────────────┐
                         │    AWS VPC      │
                         │                 │
                         │  ┌───────────┐  │
                         │  │ Honeypot  │  │
                         │  │    EC2    │  │
                         │  └─────┬─────┘  │
                         │        │         │
                         │      Events      │
                         │        │         │
                         │  ┌─────▼─────┐   │
                         │  │ Collector │   │
                         │  │   Python  │   │
                         │  └─────┬─────┘   │
                         │        │         │
                         │  ┌─────▼─────┐   │
                         │  │ PostgreSQL│   │
                         │  │  Private  │   │
                         │  └───────────┘   │
                         │                 │
                         └─────────────────┘
                                  │
                                  ▼
                              FastAPI
                                  │
                         ┌────────┴────────┐
                         ▼                 ▼
                     Analysis          Dashboard


              GitHub
                 │
                 ▼
          GitHub Actions
                 │
          ┌──────┴──────┐
          ▼             ▼
         CI             CD
          │             │
          ▼             ▼
      Tests/SAST    Terraform
                        │
                        ▼
                       AWS
```

This is the **target architecture**. Components will be introduced progressively throughout the project.

---

# 🗺️ Roadmap

## Phase 0 — Design

* [ ] Define project architecture
* [ ] Define threat model
* [ ] Define security boundaries
* [ ] Design initial data model
* [ ] Define event format
* [ ] Define repository structure

---

## Phase 1 — Local Honeypot

Build the first functional SSH honeypot.

### Goals

* [ ] Implement SSH honeypot
* [ ] Capture connection attempts
* [ ] Capture source IP
* [ ] Capture timestamp
* [ ] Capture username
* [ ] Capture password attempts
* [ ] Capture session information
* [ ] Capture commands when possible
* [ ] Implement structured logging
* [ ] Create Bash setup scripts
* [ ] Create Python tests

Initial architecture:

```text
SSH connection
      │
      ▼
  Honeypot
      │
      ▼
   Event
      │
      ▼
 JSON / Log
```

---

## Phase 2 — PostgreSQL

Replace simple log storage with a structured database.

### Goals

* [ ] Design database schema
* [ ] Create tables and relationships
* [ ] Implement PostgreSQL integration
* [ ] Create indexes
* [ ] Implement migrations
* [ ] Create analytical queries
* [ ] Test query performance
* [ ] Learn `EXPLAIN ANALYZE`

Initial entities:

```text
attackers
sessions
events
credentials
commands
```

---

## Phase 3 — Python Collector

Separate event collection from the honeypot.

```text
Honeypot
    │
    ▼
   Logs
    │
    ▼
Collector
    │
    ▼
PostgreSQL
```

### Goals

* [ ] Parse logs
* [ ] Validate events
* [ ] Normalize data
* [ ] Handle malformed events
* [ ] Insert events into PostgreSQL
* [ ] Implement structured logging
* [ ] Add unit tests
* [ ] Implement configuration management

---

## Phase 4 — FastAPI

Expose the collected data through a REST API.

### Initial endpoints

```text
GET /health

GET /events
GET /events/{id}

GET /attackers
GET /attackers/{ip}

GET /stats
GET /stats/top-ips
GET /stats/top-usernames
GET /stats/events-per-day
```

### Goals

* [ ] FastAPI
* [ ] Pydantic
* [ ] SQLAlchemy
* [ ] PostgreSQL
* [ ] Pagination
* [ ] Filtering
* [ ] Sorting
* [ ] Error handling
* [ ] Authentication
* [ ] API documentation

---

## Phase 5 — Docker

Containerize the platform.

### Initial services

```text
honeypot
collector
api
postgres
```

### Goals

* [ ] Dockerfiles
* [ ] Docker Compose
* [ ] Healthchecks
* [ ] Non-root containers
* [ ] Minimal images
* [ ] Environment configuration
* [ ] Resource limits
* [ ] Container security

The entire development environment should be reproducible with:

```bash
docker compose up
```

---

## Phase 6 — AWS

Deploy the honeypot to AWS.

### Initial infrastructure

```text
AWS
└── VPC
    ├── Internet Gateway
    ├── Subnet
    ├── Route Table
    ├── Security Group
    └── EC2
```

### Goals

* [ ] VPC
* [ ] Subnets
* [ ] Routing
* [ ] Security Groups
* [ ] EC2
* [ ] IAM
* [ ] CloudWatch
* [ ] CloudTrail
* [ ] Secure administration
* [ ] Network isolation

The honeypot must be isolated from other infrastructure and must not expose PostgreSQL directly to the Internet.

---

## Phase 7 — Terraform

Convert the AWS infrastructure into Infrastructure as Code.

### Goals

* [ ] Terraform
* [ ] Modules
* [ ] Variables
* [ ] Outputs
* [ ] Remote state
* [ ] Development environment
* [ ] Production-like environment
* [ ] Reproducible deployments

Target:

```bash
terraform init
terraform validate
terraform plan
terraform apply
terraform destroy
```

---

## Phase 8 — Secrets Management

Remove secrets from source code and CI/CD configuration.

### Goals

* [ ] AWS Secrets Manager
* [ ] IAM roles
* [ ] Environment configuration
* [ ] Least privilege
* [ ] Secret rotation strategy
* [ ] Secret scanning

No credentials should be committed to Git.

---

## Phase 9 — Continuous Integration

Implement automated validation with GitHub Actions.

### Pull Request pipeline

```text
Pull Request
     │
     ├── pytest
     ├── Ruff
     ├── mypy
     ├── Terraform fmt
     ├── Terraform validate
     ├── Bandit
     ├── Trivy
     └── Secret scanning
```

### Goals

* [ ] Automated tests
* [ ] Linting
* [ ] Type checking
* [ ] SAST
* [ ] Dependency scanning
* [ ] Container scanning
* [ ] Terraform validation
* [ ] Security quality gates

---

## Phase 10 — Continuous Deployment

Automate deployments to AWS.

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
Tests
   │
   ▼
Security Scans
   │
   ▼
Terraform Plan
   │
   ▼
Approval
   │
   ▼
Terraform Apply
   │
   ▼
AWS
```

### Goals

* [ ] Automated deployment
* [ ] Environment separation
* [ ] Deployment approvals
* [ ] Terraform plan artifacts
* [ ] AWS OIDC
* [ ] No long-lived AWS credentials in GitHub

---

## Phase 11 — Observability

Monitor the infrastructure and application.

### Technologies

* Prometheus
* Grafana
* CloudWatch

### Metrics

* CPU
* Memory
* Disk
* Network
* API latency
* API errors
* Events
* Attack attempts
* Sessions
* Connections

### Goals

* [ ] Metrics collection
* [ ] Grafana dashboards
* [ ] Application logs
* [ ] Infrastructure logs
* [ ] Alerts
* [ ] Health checks

---

## Phase 12 — Security Hardening

Apply security controls across the entire stack.

### Linux

* [ ] SSH hardening
* [ ] Firewall
* [ ] User permissions
* [ ] Audit logging
* [ ] System updates
* [ ] Service isolation

### AWS

* [ ] IAM least privilege
* [ ] Security Groups
* [ ] CloudTrail
* [ ] CloudWatch
* [ ] Encryption
* [ ] Network isolation
* [ ] Resource policies

### Docker

* [ ] Non-root users
* [ ] Minimal images
* [ ] Capability reduction
* [ ] Read-only filesystem where possible
* [ ] Image scanning
* [ ] SBOM

### PostgreSQL

* [ ] Separate users
* [ ] Least privilege
* [ ] Network restrictions
* [ ] Encrypted connections
* [ ] Backups
* [ ] Secure configuration

---

## Phase 13 — Threat Detection

Turn collected events into security detections.

### Detect

* [ ] SSH brute force
* [ ] Credential stuffing
* [ ] Port scanning
* [ ] Suspicious commands
* [ ] Multiple usernames from one IP
* [ ] Abnormal activity
* [ ] Repeated attack patterns

Example:

```text
Attacker
   │
   ├── root
   ├── admin
   ├── ubuntu
   ├── test
   └── user
```

can be classified as suspicious authentication activity.

---

## Phase 14 — Threat Intelligence

Enrich collected events with external intelligence.

For each source IP:

```text
source_ip
    │
    ├── Country
    ├── ASN
    ├── Organization
    ├── Reputation
    └── Known indicators
```

### Goals

* [ ] IP enrichment
* [ ] ASN information
* [ ] Geolocation
* [ ] Reputation
* [ ] IOC management
* [ ] Threat classification

---

## Phase 15 — Scalability

Test PostgreSQL and the application with large datasets.

Target dataset sizes:

```text
1,000
10,000
100,000
1,000,000
10,000,000+
```

### Study

* [ ] Indexes
* [ ] Query optimization
* [ ] `EXPLAIN ANALYZE`
* [ ] Partitioning
* [ ] VACUUM
* [ ] ANALYZE
* [ ] Connection pooling
* [ ] Batch inserts
* [ ] Slow queries

Eventually:

```text
Hot Data
   │
   ▼
PostgreSQL

Cold Data
   │
   ▼
S3
```

---

## Phase 16 — Backup & Disaster Recovery

The infrastructure must be recoverable after a failure.

### Goals

* [ ] PostgreSQL backups
* [ ] S3 backups
* [ ] Encryption
* [ ] Retention policies
* [ ] Automated backups
* [ ] Restore procedure
* [ ] Disaster recovery test

A backup is not considered valid until it has been successfully restored.

---

## Phase 17 — Testing

Implement testing at multiple levels.

### Unit

```text
pytest
```

### Integration

```text
FastAPI + PostgreSQL
```

### API

```text
pytest + HTTP client
```

### Infrastructure

```text
Terraform validation
```

### Security

```text
Bandit
Trivy
Secret scanning
Dependency scanning
```

### Load testing

Test the system under increasing loads.

---

## Phase 18 — Documentation

Document the project as production-like infrastructure.

### Documentation

* [ ] README
* [ ] Architecture diagrams
* [ ] Network diagrams
* [ ] Data flow
* [ ] Security boundaries
* [ ] Deployment guide
* [ ] Development guide
* [ ] Troubleshooting guide
* [ ] Disaster recovery procedure

### Architecture Decision Records

```text
ADR-001 — PostgreSQL
ADR-002 — AWS
ADR-003 — Terraform
ADR-004 — Docker
ADR-005 — Secrets Manager
ADR-006 — Network Isolation
```

---

# 🏁 Phase 19 — v1.0

The final v1.0 should be fully reproducible.

Starting from an empty AWS account and following the documentation:

```text
Terraform
    │
    ▼
AWS Infrastructure
    │
    ▼
Honeypot
    │
    ▼
Collector
    │
    ▼
PostgreSQL
    │
    ▼
FastAPI
    │
    ▼
Monitoring
```

### v1.0 Checklist

* [ ] Honeypot functional
* [ ] Real attack events collected
* [ ] PostgreSQL
* [ ] FastAPI
* [ ] Docker
* [ ] AWS
* [ ] Terraform
* [ ] CI
* [ ] CD
* [ ] IAM properly configured
* [ ] Secrets protected
* [ ] Monitoring
* [ ] Logging
* [ ] Backups
* [ ] Disaster Recovery tested
* [ ] Security scanning
* [ ] Tests
* [ ] Documentation
* [ ] Reproducible infrastructure

---

# 🚀 Future Extensions

After v1.0, the project can be extended with:

* Additional honeypot protocols
* HTTP honeypot
* FTP honeypot
* SMTP honeypot
* DNS honeypot
* Additional AWS services
* SIEM functionality
* Advanced threat detection
* Machine Learning
* Anomaly detection
* Distributed honeypots
* Multiple AWS regions
* Data lake architecture

---

# 🧰 Technology Stack

| Area            | Technology                        |
| --------------- | --------------------------------- |
| Language        | Python                            |
| Scripting       | Bash                              |
| API             | FastAPI                           |
| Database        | PostgreSQL                        |
| Containers      | Docker                            |
| Cloud           | AWS                               |
| IaC             | Terraform                         |
| CI/CD           | GitHub Actions                    |
| Monitoring      | Prometheus / Grafana              |
| Security        | Bandit / Trivy / IAM / CloudTrail |
| Version Control | Git / GitHub                      |

---

# 🔐 Security Notice

This project intentionally exposes a honeypot to potentially malicious traffic.

The honeypot must be treated as **untrusted infrastructure**.

It should be:

* isolated from personal infrastructure
* isolated from production systems
* deployed with minimum privileges
* configured without unnecessary AWS permissions
* monitored
* regularly updated
* restricted from accessing sensitive resources

Never deploy the honeypot in an environment containing systems or credentials that you cannot afford to lose.

---

# 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.