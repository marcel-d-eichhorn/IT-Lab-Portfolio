# Troubleshooting Case Study – fehlerhafter externer Datenträger

## Ausgangslage

Ein externer Datenträger zeigte während des Betriebs wiederholt I/O-Probleme und auffällige mechanische Geräusche.

Da Anwendungen und Container nur Symptome eines Storage-Problems anzeigen können, wurde die Analyse auf Host-Ebene durchgeführt.

## Diagnose

Verwendete Werkzeuge:

```bash
lsblk
dmesg -T
journalctl
smartctl
```

Zur Eingrenzung der Kernel-Meldungen eignet sich beispielsweise:

```bash
sudo dmesg -T | grep -Ei 'sd[a-z]|usb|uas|reset|I/O error|EXT4|read error'
```

Relevante Kernel-Meldungen enthielten unter anderem:

```text
Unrecovered read error
I/O error
```

Zusätzlich schlug der SMART-Zugriff über die verwendete USB-Bridge teilweise fehl. Dadurch war ein vollständiger SMART-Report nicht zuverlässig verfügbar.

## Bewertung

Mehrere Indikatoren deuteten gemeinsam auf einen physischen Datenträgerfehler:

- nicht wiederherstellbare Lesefehler
- I/O-Fehler auf Betriebssystemebene
- auffällige mechanische Geräusche
- unzuverlässiger Zugriff auf den Datenträger

In so einem Fall ist weiteres „Reparieren“ des Dateisystems keine geeignete Lösung für einen produktiv genutzten Datenträger.

## Maßnahme

Der Datenträger wurde aus dem aktiven Storage entfernt und nicht weiter für wichtige Daten verwendet.

## Lessons Learned

- Storage-Probleme immer zuerst auf Host-/Kernel-Ebene prüfen.
- Ein Container-Restart behebt keinen defekten Datenträger.
- SMART ist hilfreich, aber USB-SATA-Bridges können die Diagnose erschweren.
- Mechanische Geräusche zusammen mit I/O-Fehlern sind ein starkes Warnsignal.
- Bei physischem Defekt hat Datensicherheit Vorrang vor dem Versuch, einen Datenträger weiterzubetreiben.

## Troubleshooting-Muster

Der Fall lässt sich als allgemeines Vorgehen zusammenfassen:

```text
Symptom
  ↓
Logs / Kernel prüfen
  ↓
betroffenes Gerät identifizieren
  ↓
Hardwarezustand prüfen
  ↓
Risiko bewerten
  ↓
defekte Komponente isolieren
  ↓
Dienst stabilisieren
```
