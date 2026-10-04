# Debian Docker Homelab

Praxisprojekt zum Aufbau eines kompakten Linux-Servers für containerisierte Dienste, Medienverwaltung und zentrale Administration.

## Ziel

Ziel des Projekts ist ein wartbarer Homelab-Server auf wiederverwendeter Business-Hardware. Der Fokus liegt nicht nur auf dem Betrieb einzelner Anwendungen, sondern auf einer sauberen Basis für:

- Linux-Administration
- Docker und Docker Compose
- persistente Datenhaltung
- Storage- und Verzeichnisplanung
- Hardwarebeschleunigung
- Remote Administration
- Troubleshooting und Wartung

## Plattform

- **Betriebssystem:** Debian 13
- **Container Runtime:** Docker Engine
- **Orchestrierung:** Docker Compose
- **Remote Administration:** Cockpit
- **Host:** wiederverwendetes Business-Notebook
- **Hardwarebeschleunigung:** integrierte GPU über `/dev/dri`

## Architektur

```text
                         ┌──────────────────────┐
                         │     Debian Host      │
                         │                      │
                         │  Docker + Compose    │
                         └──────────┬───────────┘
                                    │
                  ┌─────────────────┴─────────────────┐
                  │                                   │
          persistente Daten                    Docker Netzwerk
                  │                                   │
          ┌───────┴────────┐            ┌─────────────┴─────────────┐
          │                │            │                           │
     Konfiguration      Medien      Media Services            Management
     /opt/...           /srv/...    + Indexer/Tools           + Updates
```

Interne IP-Adressen und Zugriffsdaten werden in der öffentlichen Dokumentation bewusst nicht veröffentlicht.

## Containerisierte Dienste

Der Stack umfasst unter anderem:

- Jellyfin
- Sonarr
- Radarr
- Lidarr
- Prowlarr
- Bazarr
- qBittorrent
- Portainer
- Watchtower

Ein VPN-Container wurde ebenfalls getestet, aufgrund eines Restart-Loops aber zunächst aus dem produktiven Stack genommen und als eigener Troubleshooting-Punkt behandelt.

## Technische Schwerpunkte

### Persistente Daten

Anwendungsdaten und Medien liegen getrennt vom Container-Lifecycle. Dadurch können Container aktualisiert oder ersetzt werden, ohne ihre Konfiguration oder Nutzdaten zu verlieren.

### Hardwarebeschleunigung

Jellyfin erhält Zugriff auf die integrierte GPU des Hosts:

```text
/dev/dri → Container
```

Damit kann Video-Transcoding hardwarebeschleunigt erfolgen, statt ausschließlich CPU-Ressourcen zu verwenden.

### Remote Administration

Cockpit dient als zusätzliche Weboberfläche für typische Host-Aufgaben wie:

- Systemstatus
- Storage
- Dienste
- Logs
- grundlegende Administration

Die eigentliche Container-Konfiguration bleibt Git-/Compose-orientiert.

## Dokumentation

- [Architektur & Verzeichnisstruktur](docs/architecture.md)
- [Services & Rollen](docs/services.md)
- [Troubleshooting Case Study](docs/troubleshooting.md)

## Lessons Learned

- Container sollten austauschbar sein, Daten dagegen persistent.
- Eine saubere Verzeichnisstruktur spart später enorm viel Aufwand.
- Hardwarebeschleunigung benötigt explizite Gerätefreigaben zum Container.
- Docker abstrahiert Anwendungen, ersetzt aber nicht die Administration des Hosts.
- Storage-Fehler müssen auf Host-Ebene diagnostiziert werden; Container sind dabei oft nur das erste sichtbare Symptom.
- Nicht jeder fehlerhafte Dienst sollte durch endlose Restarts „am Leben gehalten“ werden — manchmal ist gezieltes Deaktivieren die sauberere Zwischenlösung.

## Status

Das Homelab wird laufend erweitert. Compose-Dateien und Beispielkonfigurationen werden erst dann veröffentlicht, wenn sie aus der realen Umgebung übernommen, bereinigt und auf Secrets geprüft wurden.
