# Services & Rollen

## Übersicht

| Service | Rolle im Homelab |
| --- | --- |
| Jellyfin | Medienserver und Streaming |
| Sonarr | Verwaltung serienbezogener Medien-Workflows |
| Radarr | Verwaltung filmbezogener Medien-Workflows |
| Lidarr | Verwaltung musikbezogener Medien-Workflows |
| Prowlarr | zentrale Indexer-Verwaltung |
| Bazarr | Untertitelverwaltung |
| qBittorrent | Download-Client |
| Portainer | zusätzliche Docker-Webadministration |
| Watchtower | Container-Update-Automatisierung |
| Cockpit | Administration des Debian-Hosts |

## Jellyfin

Jellyfin ist der zentrale Medienserver des Stacks.

Technisch besonders relevant:

- persistente Konfiguration
- getrennte Mediendaten
- GPU-Passthrough über `/dev/dri`
- Container-Neuerstellung ohne Verlust der Bibliothekskonfiguration

## Management

### Cockpit

Cockpit arbeitet auf Host-Ebene und ergänzt die klassische Shell-Administration.

### Portainer

Portainer bietet einen zusätzlichen Blick auf:

- Container
- Images
- Volumes
- Netzwerke
- Logs

Die langfristige Zielsetzung ist trotzdem eine nachvollziehbare Compose-basierte Konfiguration statt ausschließlich manueller GUI-Konfiguration.

## Update-Strategie

Watchtower wurde als Möglichkeit für automatisierte Container-Updates eingebunden.

Automatisierung reduziert Routinearbeit, bringt aber auch Risiken mit sich. Für kritische Services sind daher weiterhin wichtig:

- persistente Konfigurationen
- nachvollziehbare Versionen
- Backups
- kontrollierte Wiederherstellung

## VPN-Container

Ein VPN-Container wurde in der Umgebung getestet, lief jedoch in einen Restart-Loop.

Statt einen instabilen Container dauerhaft neu starten zu lassen, wurde er zunächst gestoppt. Die Fehleranalyse wird getrennt von den stabil laufenden Services behandelt.

Das ist im Homelab ein bewusstes Betriebsprinzip:

> Stabiler Grundbetrieb hat Vorrang vor einem zusätzlichen Feature, das die Fehlersuche unnötig erschwert.
