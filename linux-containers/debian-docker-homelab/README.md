# Debian Docker Homelab

Praxisprojekt zum Aufbau eines kompakten Linux-Servers für containerisierte Dienste und zentrale Administration.

## Ziel

Ziel des Projekts ist ein wartbarer Homelab-Server auf wiederverwendeter Business-Hardware. Der Fokus liegt nicht auf einzelnen Anwendungen, sondern auf einer sauberen Basis für:

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
- **Remote Administration:** Web- und Shell-basierte Verwaltung
- **Host:** wiederverwendete Business-Hardware
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
     Konfiguration       Daten      Application Services       Management
     /opt/...           /srv/...    interne Container          Wartung
```

Interne IP-Adressen, konkrete Anwendungen und Zugriffsdaten werden in der öffentlichen Dokumentation bewusst nicht veröffentlicht.

## Containerisierte Dienste

Die produktiven Container werden in der öffentlichen Version nur nach technischen Rollen beschrieben:

- Application Services
- Management- und Monitoring-Komponenten
- Update-/Maintenance-Komponenten
- optionale Netzwerkdienste

Konkrete Produktnamen, interne Ports und private Service-Zuordnungen bleiben absichtlich außerhalb des öffentlichen Repositories.

## Technische Schwerpunkte

### Persistente Daten

Anwendungsdaten liegen getrennt vom Container-Lifecycle. Dadurch können Container aktualisiert oder ersetzt werden, ohne ihre Konfiguration oder Nutzdaten zu verlieren.

### Hardwarebeschleunigung

Ein dafür vorgesehener Container erhält Zugriff auf die integrierte GPU des Hosts:

```text
/dev/dri → Container
```

Damit können unterstützte Workloads hardwarebeschleunigt ausgeführt werden, statt ausschließlich CPU-Ressourcen zu verwenden.

### Remote Administration

Der Host wird sowohl per Shell als auch über eine zusätzliche Weboberfläche administriert.

Typische Aufgaben:

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

Das Homelab wird laufend erweitert. Compose-Dateien und Beispielkonfigurationen werden nur in bereinigter Form veröffentlicht. Private Service-Namen, interne Adressierung und Credentials bleiben bewusst außerhalb des öffentlichen Portfolios.
