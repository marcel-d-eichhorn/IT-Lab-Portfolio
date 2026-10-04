# Azure Basics Lab

Ein kompaktes Grundlagen-Lab zur praktischen Arbeit mit zentralen Microsoft-Azure-Diensten.

## Ziel

Ziel des Labs war es, typische Basisaufgaben eines Cloud-Administrators selbstständig umzusetzen und sauber zu dokumentieren:

- Resource Group erstellen
- Storage Account bereitstellen
- Linux-VM deployen
- SSH-basierte Administration vorbereiten
- Benutzer und Rollen verwalten
- Budget zur Kostenkontrolle einrichten
- Ressourcen anschließend wieder sauber entfernen

## Technologien

- Microsoft Azure
- Azure Portal
- Azure RBAC
- Ubuntu 22.04 LTS
- SSH
- Azure Cost Management

## Architektur

```text
Azure Subscription
└── Resource Group: rg-azure-basics
    ├── Storage Account
    ├── Ubuntu VM
    └── Rollen / Benutzer

Cost Management
└── Monatliches Budget
```

## Umsetzung

Die vollständige Durchführung mit Screenshots und Erläuterungen befindet sich im:

[→ Lab Report](docs/lab-report.md)

Enthalten sind unter anderem:

1. Orientierung im Azure Portal
2. Anlegen der Resource Group
3. Erstellen eines Storage Accounts
4. Bereitstellen einer Ubuntu-VM
5. Benutzer- und Rollenverwaltung
6. Kostenkontrolle mit Budget
7. Cleanup der erzeugten Ressourcen

## Ergebnis

Das Lab vermittelt praktische Grundlagen in den Bereichen **Azure-Ressourcenverwaltung, RBAC, virtuelle Maschinen, Storage und Kostenkontrolle**.

Besonderer Fokus lag darauf, die Umgebung nicht nur aufzubauen, sondern sie anschließend auch wieder vollständig zu bereinigen, um unnötige Cloud-Kosten zu vermeiden.

## Lessons Learned

- Resource Groups erleichtern Struktur, Lifecycle und Kostenübersicht.
- Rollen sollten nach dem Least-Privilege-Prinzip vergeben werden.
- Regionen und VM-Größen beeinflussen Kosten unmittelbar.
- Ein Budget ersetzt kein technisches Kostenlimit, hilft aber bei der Überwachung.
- Cleanup gehört bei temporären Cloud-Labs fest zum Ablauf.
