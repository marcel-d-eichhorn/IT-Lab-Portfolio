# Security Design

## Ziel

Die Firewall soll als zentraler Kontrollpunkt zwischen externem und internem Netzwerk dienen.

Das Sicherheitsmodell folgt dabei dem Prinzip:

> Nur Verkehr erlauben, der tatsächlich benötigt wird.

## Zonenmodell

Die öffentliche Dokumentation verwendet bewusst nur abstrakte Zonen:

```text
WAN
 │
 ▼
Firewall
 ├── Client Network
 ├── Server Network
 └── Management Network
```

Die tatsächliche Segmentierung wird erst dann dokumentiert, wenn sie vollständig umgesetzt und getestet ist.

## Regelprinzipien

Für Firewall-Regeln gelten folgende Grundsätze:

- möglichst spezifische Quelle und Ziel definieren
- nur benötigte Dienste freigeben
- Management-Zugriffe getrennt behandeln
- unnötige Any-to-Any-Regeln vermeiden
- Änderungen nachvollziehbar dokumentieren
- Logging für relevante Regeln aktivieren

## Management

Management-Zugriffe sollten nicht aus beliebigen Netzwerkbereichen möglich sein.

Langfristig ist vorgesehen, administrative Zugriffe stärker von normalen Client-Verbindungen zu trennen.

## VPN

Eine VPN-Integration ist Bestandteil der Zielarchitektur.

Da sie noch nicht vollständig produktiv umgesetzt und getestet ist, werden aktuell keine konkreten Provider-, Tunnel- oder Routingdetails veröffentlicht.

## Logging

Firewall-Logs sind bei Netzwerkproblemen ein zentraler Diagnosepunkt.

Typische Fragen:

- erreicht der Traffic die Firewall?
- welche Regel greift?
- wird der Verkehr verworfen oder weitergeleitet?
- stimmen Quelle, Ziel und Dienst?
- existiert ein Routingproblem?

## Dokumentationsregel

Geplante Funktionen werden im Portfolio ausdrücklich als **geplant** markiert.

Nur tatsächlich getestete Funktionen werden als **umgesetzt** beschrieben.
