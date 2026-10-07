# Thermal Control & Fan Automation

## Ausgangslage

Enterprise-Server priorisieren standardmäßig Kühlreserve und Hardware-Sicherheit stärker als geringe Lautstärke.

Für den Betrieb in einer geräuschsensiblen Umgebung wurde deshalb untersucht, wie sich die Lüfterregelung des T420 kontrolliert reduzieren lässt, ohne die Temperaturen aus dem Blick zu verlieren.

## Vorgehen

### 1. iDRAC Thermal Settings

Zunächst wurden vorhandene Thermal-Optionen geprüft und auf eine möglichst zurückhaltende Herstellerkonfiguration eingestellt.

Dabei wurden unter anderem Einstellungen für:

- Thermal Profile
- Reaktion auf Drittanbieter-Hardware
- Lüfterverhalten

untersucht.

### 2. Manuelle PWM-Tests

Anschließend wurde die Lüftersteuerung mit `ipmitool` getestet.

Die Drehzahl wurde schrittweise reduziert, statt direkt einen sehr niedrigen Wert dauerhaft zu setzen.

Beispielprinzip:

```text
höherer PWM-Wert
      ↓
Temperatur beobachten
      ↓
PWM reduzieren
      ↓
Temperatur erneut beobachten
      ↓
stabilen Bereich bestimmen
```

Tests bis in den niedrigen PWM-Bereich zeigten einen deutlich leiseren Betrieb bei weiterhin stabilen Temperaturen und erhaltener Lüfterredundanz.

## Warum kein fixer Wert?

Ein dauerhaft fester PWM-Wert ist für wechselnde Lasten ungeeignet.

Deshalb wurde eine temperaturabhängige Regelung mit Hysterese umgesetzt.

```text
Temperatur niedrig
      ↓
niedrige Lüfterstufe

Temperatur steigt
      ↓
höhere Lüfterstufe

Temperatur fällt erst deutlich unter Schwellwert
      ↓
wieder reduzieren
```

Die Hysterese verhindert, dass die Lüfter ständig zwischen zwei Stufen wechseln.

## systemd-Service

Die getestete Regelung wurde anschließend als eigener systemd-Service eingebunden.

Dadurch startet die Steuerung automatisch mit dem System und läuft unabhängig von einer interaktiven Shell.

Technische Bausteine:

- Shell-/Control-Script
- `ipmitool`
- Temperaturabfrage
- PWM-Steuerung
- Hysterese
- systemd Unit
- regelmäßiges Prüfintervall

## Sicherheit

Die Automatisierung wurde erst nach manuellen Messungen aktiviert.

Wichtig:

- Temperaturwerte überwachen
- Lüfterredundanz nicht ignorieren
- bei Fehlern auf konservative Werte zurückfallen
- keine aggressiven Minimalwerte ohne Lasttests verwenden

## Lessons Learned

- Hardwaresteuerung sollte immer messwertbasiert erfolgen.
- Erst manuell testen, dann automatisieren.
- Hysterese ist bei temperaturabhängigen Regelungen essenziell.
- systemd eignet sich gut, um eigene Hardware-Automation zuverlässig in den Linux-Betrieb zu integrieren.
