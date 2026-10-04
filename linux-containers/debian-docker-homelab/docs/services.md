# Services & Rollen

## Öffentliche Darstellung

Die konkrete Softwareauswahl des privaten Homelabs ist absichtlich nicht Bestandteil dieses Portfolios.

Für die technische Dokumentation reicht die Betrachtung der Rollen:

| Rolle | Aufgabe |
| --- | --- |
| Application Services | Bereitstellung der eigentlichen Anwendungsfunktionen |
| Management Service | Übersicht und Verwaltung der Container-Umgebung |
| Maintenance Service | unterstützende Wartungs- und Update-Aufgaben |
| Network Service | optionale netzwerkbezogene Funktionen |
| Host Administration | Verwaltung des Debian-Hosts außerhalb der Container |

## Application Services

Die Anwendungscontainer sind technisch nach demselben Grundprinzip aufgebaut:

- persistente Konfiguration
- getrennte Nutzdaten
- definierte Netzwerkanbindung
- reproduzierbare Compose-Konfiguration
- Container-Neuerstellung ohne Verlust persistenter Daten

Ein ausgewählter Workload verwendet zusätzlich GPU-Passthrough über `/dev/dri`.

## Management

Für die Administration existieren getrennte Ebenen:

### Host-Ebene

Auf Host-Ebene werden unter anderem verwaltet:

- Storage
- Systemdienste
- Logs
- Ressourcen
- Docker Runtime

### Container-Ebene

Auf Container-Ebene stehen insbesondere im Fokus:

- Container
- Images
- Volumes
- Netzwerke
- Logs

Die langfristige Zielsetzung bleibt eine nachvollziehbare Compose-basierte Konfiguration statt ausschließlich manueller GUI-Konfiguration.

## Update-Strategie

Für Teile des Stacks wurde Update-Automatisierung getestet.

Automatisierung reduziert Routinearbeit, bringt aber auch Risiken mit sich. Für wichtige Services bleiben daher entscheidend:

- persistente Konfigurationen
- nachvollziehbare Versionen
- Backups
- kontrollierte Wiederherstellung

## Instabiler optionaler Dienst

Ein optionaler Container lief zeitweise in einen Restart-Loop.

Statt einen instabilen Container dauerhaft neu starten zu lassen, wurde er zunächst deaktiviert. Die Fehleranalyse wird getrennt von den stabil laufenden Services behandelt.

Das ist im Homelab ein bewusstes Betriebsprinzip:

> Stabiler Grundbetrieb hat Vorrang vor einem zusätzlichen Feature, das die Fehlersuche unnötig erschwert.

## Privacy by Design

Nicht veröffentlicht werden:

- konkrete Produkt- und Service-Namen
- interne Ports
- interne IP-Adressen
- private DNS-Namen
- produktive Compose-Dateien
- Secrets und Umgebungsvariablen

Damit bleibt das Portfolio technisch aussagekräftig, ohne die private Homelab-Umgebung unnötig offenzulegen.
