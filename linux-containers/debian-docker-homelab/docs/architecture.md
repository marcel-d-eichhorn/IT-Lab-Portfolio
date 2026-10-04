# Architektur & Verzeichnisstruktur

## Host

Der Server basiert auf wiederverwendeter Business-Hardware und läuft mit Debian 13.

Die Wahl vorhandener Hardware verfolgt zwei Ziele:

1. geringe Einstiegskosten
2. praktische Erfahrung mit realer Linux- und Container-Administration

## Verzeichnisstrategie

Die Daten werden bewusst nach Funktion getrennt.

```text
/srv/
└── data/               # persistente Nutzdaten

/opt/
└── <stack>/            # Compose-Stack und anwendungsnahe Konfigurationen

/srv/docker/            # zusätzliche persistente Docker-Daten
```

Die Pfade in dieser öffentlichen Dokumentation sind abstrahiert und müssen nicht 1:1 der privaten Umgebung entsprechen.

Wichtig ist die Trennung zwischen:

- Container-Image
- Compose-Definition
- Konfiguration
- persistenten Daten
- Nutzdaten

Container können dadurch neu erstellt werden, ohne dass Anwendungsdaten verloren gehen.

## Docker-Netzwerk

Die Services kommunizieren über ein dediziertes Docker-Netzwerk.

Die öffentliche Dokumentation verzichtet bewusst auf tatsächliche Service-Namen, Ports und interne Adressierung. Für die Architektur relevant ist vor allem:

```text
Host
 │
 └── Docker Bridge Network
      ├── Application Service A
      ├── Application Service B
      ├── Application Service C
      ├── Management Service
      ├── Maintenance Service
      └── optionaler Network Service
```

## Persistenz

Beispielprinzip:

```yaml
volumes:
  - /path/on/host/config:/config
  - /path/on/host/data:/data
```

Das Beispiel zeigt nur das verwendete Muster. Produktive Pfade, Credentials, interne Service-Namen und Umgebungsvariablen werden nicht veröffentlicht.

## Hardwarebeschleunigung

Für einen dafür vorgesehenen Container wird das DRM-/GPU-Device des Linux-Hosts durchgereicht:

```yaml
devices:
  - /dev/dri:/dev/dri
```

Damit kann die integrierte Grafik für unterstützte Workloads genutzt werden.

## Administration

Die Umgebung wird auf mehreren Ebenen verwaltet:

```text
Debian Host
├── Shell / SSH
├── Web Administration
└── Docker
    ├── Compose
    └── Container Management
```

Die Weboberflächen sind eine Ergänzung, nicht die einzige Verwaltungsquelle. Die zugrunde liegende Konfiguration soll nachvollziehbar und reproduzierbar bleiben.
