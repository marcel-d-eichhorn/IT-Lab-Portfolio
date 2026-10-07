# Remote Management mit iDRAC

## Ziel

Der Dell PowerEdge T420 verfügt mit iDRAC über ein unabhängiges Management-System.

Dadurch können wichtige Administrationsaufgaben auch dann durchgeführt werden, wenn:

- das Betriebssystem nicht läuft
- der Server noch nicht vollständig installiert ist
- ein Bootproblem vorliegt
- physischer Zugriff unpraktisch ist

## Genutzte Funktionen

### Hardwarestatus

Über iDRAC lassen sich unter anderem überwachen:

- Lüfter
- Temperaturen
- Netzteile
- Storage
- allgemeiner Hardwarezustand

Damit können Hardwareprobleme bereits unterhalb der Betriebssystemebene eingegrenzt werden.

### racadm

Zusätzlich zur Weboberfläche wurde `racadm` verwendet.

Beispiel zur Storage-Abfrage:

```bash
racadm storage get vdisks -o -p Name,State,OperationalState
```

Das ist besonders hilfreich für reproduzierbare Diagnose- und Administrationsschritte.

## Remote Recovery

Für Wartungs- und Recovery-Zwecke wurde ein ISO-Image remote eingebunden.

Verwendetes Prinzip:

```text
Management Client
      │
      ▼
Remote Image / Network Share
      │
      ▼
iDRAC
      │
      ▼
Server Boot
      │
      ▼
Recovery Environment
```

Damit kann ein Wartungssystem gestartet werden, ohne lokal ein USB-Medium oder optisches Laufwerk anzuschließen.

## Virtual Console

Die integrierte Virtual Console wurde ebenfalls untersucht.

Dabei zeigten sich typische Probleme älterer Serverplattformen:

- ältere Java-basierte Konsolen
- Kompatibilitätsprobleme moderner Clients
- alternative Remote-Console-Verfahren erforderlich

Der wichtigste praktische Punkt war daher nicht eine einzelne GUI-Funktion, sondern mehrere unabhängige Management-Wege zu verstehen.

## Lessons Learned

- Out-of-Band-Management sollte unabhängig vom normalen Netzwerk- und OS-Zugriff geplant werden.
- CLI-Werkzeuge wie racadm sind für wiederholbare Administration oft wertvoller als reine GUI-Schritte.
- Remote-ISO-Funktionen sind ein starkes Recovery-Werkzeug.
- Bei älteren Management-Plattformen muss mit Client-Kompatibilitätsproblemen gerechnet werden.
