# Storage & RAID

## Ziel

Der T420 wird als reale Plattform für Hardware-RAID und Enterprise-Storage genutzt.

Der Fokus liegt auf:

- Zustand virtueller Disks
- Controller-Sicht auf Storage
- physische vs. logische Datenträger
- sichere Erweiterungsplanung
- Fehlerdiagnose außerhalb des Betriebssystems

## RAID-Ebene

Ein Hardware-RAID-Controller abstrahiert mehrere physische Datenträger zu virtuellen Disks.

```text
Physical SAS Disks
       │
       ▼
Hardware RAID Controller
       │
       ▼
Virtual Disk
       │
       ▼
Operating System
```

Das Betriebssystem sieht daher primär die virtuellen Datenträger, nicht die komplette interne RAID-Logik.

## Statusprüfung

Verwendeter Befehl:

```bash
racadm storage get vdisks -o -p Name,State,OperationalState
```

Damit wurden unter anderem folgende Zustände geprüft:

- Name der virtuellen Disk
- State
- Operational State

Ein vorhandener OS-Datenträger wurde dabei als online und betriebsbereit erkannt.

## Physische Datenträger

Für das Storage-Lab stehen mehrere Enterprise-SAS-Datenträger zur Verfügung.

Bei Änderungen an einem bestehenden RAID-Verbund gilt:

> Neue physische Disks erweitern einen bestehenden Verbund nicht automatisch.

Vor Änderungen müssen immer geprüft werden:

- aktueller RAID-Level
- Controller-Funktionen
- vorhandene Virtual Disks
- Status aller Physical Disks
- Backup
- unterstützte Reconfigure-/Expansion-Funktionen

## Betriebssystem vs. Controller

Ein wichtiger Unterschied:

```text
Linux tools
   → Dateisysteme
   → Partitionen
   → sichtbare Block Devices

RAID Controller / iDRAC
   → Physical Disks
   → Virtual Disks
   → RAID State
   → Controller Health
```

Beide Ebenen sind notwendig, beantworten aber unterschiedliche Fragen.

## Lessons Learned

- Hardware-RAID sollte immer auch auf Controller-Ebene diagnostiziert werden.
- "Disk vorhanden" bedeutet nicht automatisch "Teil des RAID".
- RAID-Erweiterungen müssen geplant werden und sind keine Plug-and-Play-Aktion.
- Vor Storage-Änderungen sind Backup und Statusprüfung Pflicht.
- racadm eignet sich gut für nachvollziehbare und dokumentierbare Abfragen.
