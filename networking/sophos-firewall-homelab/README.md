# Sophos Firewall Homelab

Praxisprojekt zum Aufbau einer zentralen Firewall zwischen Internetzugang und internem Homelab.

## Ziel

Ziel ist eine saubere Trennung zwischen Internetzugang, Firewalling und internem Netzwerk. Die Firewall übernimmt dabei schrittweise Aufgaben, die in klassischen Heimnetzen oft direkt im Router gebündelt sind.

Im Fokus stehen:

- zentrale Firewall-Regeln
- Routing
- Netzwerksegmentierung
- kontrollierter Internetzugang
- VPN-Vorbereitung
- Logging und Troubleshooting
- Wiederverwendung vorhandener Hardware

## Architektur

### Zielbild

```text
Internet
   │
   ▼
ISP Modem
   │
   ▼
Sophos Firewall
   │
   ├── internes LAN
   ├── Server / Homelab
   └── WLAN Access Point
```

Der WLAN-Zugang wird dabei nicht von der Firewall selbst bereitgestellt. Ein vorhandenes Gerät wird ausschließlich als Access Point weiterverwendet.

Interne IP-Adressen, reale Gerätenamen und konkrete Providerdetails werden bewusst nicht veröffentlicht.

## Technische Schwerpunkte

### Firewall als zentrale Instanz

Die Sophos Firewall soll langfristig zentrale Aufgaben übernehmen:

- Paketfilterung
- Routing
- Netzwerkregeln
- Segmentierung
- Protokollierung
- optional VPN-Funktionen

Dadurch lassen sich Netzwerkpfade und Sicherheitsregeln kontrollierter verwalten als in einer vollständig kombinierten Router-/WLAN-Konfiguration.

### Modem- und Router-Rollen trennen

Der Internetzugang wird auf ein separates Modem reduziert.

Das Architekturprinzip lautet damit:

```text
Modem = Zugang zum Provider
Firewall = Routing + Security
Access Point = WLAN
```

Diese Aufgabentrennung erleichtert spätere Änderungen und macht die Infrastruktur modularer.

## Status

Das Projekt befindet sich im laufenden Ausbau.

Bereits praktisch bearbeitet wurden unter anderem:

- Firewall-Hardware in Betrieb nehmen
- Internetzugang über separates Modem vorbereiten
- Hardware-/RAM-Fehler an der Firewall diagnostizieren
- Zielarchitektur für Firewall und WLAN entwerfen

Weitere Schritte wie feinere Segmentierung und VPN-Integration werden erst dann als umgesetzt dokumentiert, wenn sie tatsächlich produktiv getestet wurden.

## Dokumentation

- [Architektur](docs/architecture.md)
- [Security Design](docs/security-design.md)
- [Troubleshooting Case Study](docs/troubleshooting.md)

## Lessons Learned

- Modem, Firewall und WLAN müssen nicht in einem einzigen Gerät stecken.
- Rollen sauber zu trennen verbessert Wartbarkeit und Austauschbarkeit.
- Netzwerkdesign sollte Ist-Zustand und Zielarchitektur klar unterscheiden.
- Firewall-Regeln sollten so spezifisch wie sinnvoll statt pauschal offen gestaltet werden.
- Hardwarefehler können wie Software- oder Konfigurationsprobleme wirken und müssen systematisch ausgeschlossen werden.
