# Architektur & Verzeichnisstruktur

## Host

Der Server basiert auf wiederverwendeter Business-Notebook-Hardware und läuft mit Debian 13.

Die Wahl vorhandener Hardware verfolgt zwei Ziele:

1. geringe Einstiegskosten
2. praktische Erfahrung mit realer Linux- und Container-Administration

## Verzeichnisstrategie

Die Daten werden bewusst nach Funktion getrennt.

```text
/srv/
└── media/              # Mediendaten

/opt/
└── <stack>/            # Compose-Stack und anwendungsnahe Konfigurationen

/srv/docker/            # zusätzliche persistente Docker-Daten
```

Wichtig ist die Trennung zwischen:

- Container-Image
- Compose-Definition
- Konfiguration
- persistenten Daten
- Mediendaten

Container können dadurch neu erstellt werden, ohne dass Anwendungsdaten verloren gehen.

## Docker-Netzwerk

Die Services kommunizieren über ein dediziertes Docker-Netzwerk.

Die öffentliche Dokumentation verzichtet bewusst auf die tatsächliche interne Adressierung. Für die Architektur relevant ist vor allem:

```text
Host
 │
 └── Docker Bridge Network
      ├── Jellyfin
      ├── Sonarr
      ├── Radarr
      ├── Lidarr
      ├── Prowlarr
      ├── Bazarr
      ├── qBittorrent
      ├── Portainer
      └── Watchtower
```

## Persistenz

Beispielprinzip:

```yaml
volumes:
  - /path/on/host/config:/config
  - /srv/media:/data
```

Das Beispiel zeigt nur das verwendete Muster. Produktive Pfade, Credentials und Umgebungsvariablen werden nicht ungeprüft veröffentlicht.

## Hardwarebeschleunigung

Für Jellyfin wird das DRM-/GPU-Device des Linux-Hosts durchgereicht:

```yaml
devices:
  - /dev/dri:/dev/dri
```

Damit kann der Container die integrierte Grafik für unterstützte Transcoding-Workloads verwenden.

## Administration

Die Umgebung wird auf mehreren Ebenen verwaltet:

```text
Debian Host
├── Shell / SSH
├── Cockpit
└── Docker
    ├── Compose
    └── Portainer
```

Dabei ist die Weboberfläche eine Ergänzung, nicht die einzige Verwaltungsquelle. Die zugrunde liegende Konfiguration soll nachvollziehbar und reproduzierbar bleiben.
