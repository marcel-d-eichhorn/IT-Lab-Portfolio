# IT Lab Portfolio

Praxisorientiertes Portfolio rund um **Systemintegration, IT-Security, Linux, Networking, Cloud und Automation**.

Ich befinde mich in der Umschulung zum **Fachinformatiker für Systemintegration (FISI)** und dokumentiere hier ausgewählte Labs, Homelab-Projekte, Automatisierungen und Troubleshooting-Fälle. Im Fokus stehen nachvollziehbare technische Entscheidungen, saubere Dokumentation und praxisnahe Umsetzung.

## Schwerpunkte

- **IT-Security:** SIEM, Detection, Hardening, Secret Scanning
- **Linux & Container:** Debian, Docker, Compose, Services
- **Networking:** Routing, Firewalling, VPN, Segmentierung
- **Cloud:** Microsoft Azure, Ressourcen, Rollen, Kostenkontrolle
- **Infrastructure:** Server, RAID, Storage, Remote Administration
- **Automation:** PowerShell, Python, Git-basierte Workflows
- **Troubleshooting:** Fehleranalyse, Logs, Ursachenfindung und Dokumentation

## Featured Projects

### 🐧 Debian Docker Homelab
Containerisierter Homelab-Server auf Debian mit persistenten Daten, GPU-Passthrough und dokumentiertem Storage-Troubleshooting.

**Technologien:** Debian · Docker · Docker Compose · Linux Storage · /dev/dri

[Projekt öffnen →](linux-containers/debian-docker-homelab/)

### 🔐 Repo Security Checker
Python-basierter Pre-Commit-Scanner für typische Secrets und sensible Daten.

**Technologien:** Python · YAML · Regex · Git Hooks · Bash · PowerShell

[Projekt öffnen →](security/repo-security-checker/)

### ☁️ Azure Basics Lab
Grundlegendes Azure-Lab mit Resource Group, Storage Account, virtueller Maschine, Benutzer/Rollen und Budgetkontrolle.

**Technologien:** Microsoft Azure · RBAC · Ubuntu · SSH · Cost Management

[Projekt öffnen →](cloud/azure-basics/)

## In Arbeit / geplant

Folgende Projekte werden schrittweise dokumentiert und ergänzt:

- **Wazuh SIEM & Detection Engineering**
- **Sophos Firewall & Netzwerkarchitektur**
- **Docker Swarm & High Availability**
- **Dell PowerEdge / RAID / Serveradministration**
- **Sysadmin Troubleshooting Case Studies**
- **PowerShell- und Python-Automation**

## Repository-Struktur

```text
IT-Lab-Portfolio/
├── cloud/
│   └── azure-basics/
├── linux-containers/
│   └── debian-docker-homelab/
├── security/
│   └── repo-security-checker/
├── README.md
├── SECURITY.md
├── LICENSE
└── .gitignore
```

## Dokumentationsprinzipien

- keine produktiven Zugangsdaten oder Secrets
- interne Systeme und Umgebungen werden anonymisiert
- konkrete private Anwendungen werden nur abstrahiert dokumentiert
- Screenshots werden vor Veröffentlichung geprüft
- Entscheidungen und Troubleshooting werden nachvollziehbar dokumentiert
- Konfigurationen werden möglichst reproduzierbar beschrieben

---

Dieses Portfolio wächst mit meiner praktischen Erfahrung und wird fortlaufend um reale Labs und technische Projekte erweitert.
