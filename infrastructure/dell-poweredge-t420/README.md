# Dell PowerEdge T420 – Server Administration Lab

Praxisprojekt zur Administration eines Dell PowerEdge T420 mit Fokus auf **Remote Management, RAID/Storage, Linux-Betrieb und Hardware-Monitoring**.

## Ziel

Der Server dient als reale Infrastrukturplattform, um typische Aufgaben aus der Systemadministration praktisch umzusetzen:

- Out-of-Band-Management mit iDRAC
- Hardware- und Sensorüberwachung
- RAID-/Storage-Status prüfen
- Remote-Recovery und ISO-Boot
- Linux-Administration
- IPMI-basierte Lüftersteuerung
- systemd-Automatisierung

## Plattform

- **Server:** Dell PowerEdge T420
- **Remote Management:** Dell iDRAC
- **Betriebssystem:** Debian / Linux-basierte Wartungsumgebungen
- **Storage:** Hardware-RAID mit Enterprise-SAS-Datenträgern
- **Management-Tools:** racadm, ipmitool, systemd

## Architektur

```text
Management Client
      │
      ├── iDRAC Web Interface
      ├── racadm
      └── IPMI / ipmitool
              │
              ▼
      Dell PowerEdge T420
      ├── RAID Controller
      │   └── Virtual Disks
      ├── SAS Storage
      ├── Hardware Sensors
      ├── System Fans
      └── Debian / Recovery Environment
```

## Praktisch umgesetzt

### Remote Management

Der Server wird über iDRAC auch unabhängig vom Betriebssystem administriert.

Verwendete Funktionen:

- Hardwarestatus prüfen
- Sensorwerte auslesen
- Remote-Boot vorbereiten
- ISO-/Recovery-Medien remote bereitstellen
- Storage-Zustand kontrollieren

Mehr dazu: [Remote Management](docs/remote-management.md)

### RAID & Storage

Der RAID-Controller wurde per iDRAC/racadm geprüft und virtuelle Datenträger auf Zustand und Betriebsstatus kontrolliert.

Beispiel:

```bash
racadm storage get vdisks -o -p Name,State,OperationalState
```

Damit lassen sich virtuelle Disks unabhängig vom installierten Betriebssystem überprüfen.

Mehr dazu: [Storage & RAID](docs/storage-raid.md)

### Thermal Management

Da der Server in einer geräuschsensiblen Umgebung betrieben wird, wurde die Standard-Lüfterregelung untersucht und anschließend eine eigene, temperaturabhängige Steuerung getestet.

Verwendet wurden:

- iDRAC Thermal Settings
- `ipmitool`
- manuelle PWM-Tests
- Temperaturüberwachung
- systemd-Service
- Hysterese zur Vermeidung permanenter Drehzahlwechsel

Mehr dazu: [Thermal Control](docs/thermal-control.md)

## Troubleshooting-Ansatz

Das Projekt folgt bewusst einem reproduzierbaren Schema:

```text
Problem
  ↓
Hardware-/Sensorstatus prüfen
  ↓
Remote Management nutzen
  ↓
Änderung isolieren
  ↓
Messwerte vergleichen
  ↓
Automatisierung erst nach stabilem Test
```

## Lessons Learned

- Out-of-Band-Management ist bei Servern deutlich mehr als nur eine Remote-Konsole.
- RAID-Zustand sollte auf Controller-Ebene geprüft werden, nicht nur im Betriebssystem.
- Hardware-Monitoring und Betriebssystem-Monitoring ergänzen sich.
- Lüfterregelung sollte temperaturgeführt und nicht nur auf einen festen PWM-Wert gesetzt werden.
- Eine getestete manuelle Lösung sollte erst danach als systemd-Service automatisiert werden.
- Recovery-Zugriff ist besonders wertvoll, wenn das installierte Betriebssystem nicht startet oder noch nicht vorhanden ist.

## Status

Der Server wird laufend als Infrastruktur- und Storage-Lab weiterentwickelt. Nur bereits praktisch getestete Funktionen werden hier als umgesetzt dokumentiert.
