# Architektur

## Grundprinzip

Das Homelab-Netzwerk wird modular aufgebaut.

```text
┌──────────────┐
│   Internet   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  ISP Modem   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Sophos    │
│   Firewall   │
└──────┬───────┘
       │
       ├──────────────► kabelgebundene Clients
       │
       ├──────────────► Homelab / Server
       │
       └──────────────► WLAN Access Point
```

## Rollen

### ISP Modem

Das Modem stellt lediglich die Verbindung zum Provider her.

Es soll möglichst wenig zusätzliche Netzwerklogik übernehmen.

### Sophos Firewall

Die Firewall ist die zentrale Routing- und Security-Instanz.

Geplante bzw. schrittweise umgesetzte Aufgaben:

- WAN-/LAN-Trennung
- Routing
- Firewall-Regeln
- Logging
- Segmentierung
- VPN-Anbindung

### Access Point

Das WLAN wird über vorhandene Hardware bereitgestellt, die nur noch als Access Point arbeitet.

Damit bleiben WLAN und Firewall logisch getrennt.

## Warum diese Architektur?

Ein typischer Consumer-Router vereint:

- Modem
- Router
- Firewall
- Switch
- WLAN
- teilweise VPN

Für ein Lern- und Homelab ist die bewusste Trennung dieser Rollen interessanter, weil einzelne Komponenten gezielt administriert, ersetzt und analysiert werden können.

## Modularität

Die Architektur soll Änderungen erlauben, ohne das gesamte Netzwerk neu aufzubauen.

Beispiele:

- Access Point austauschen
- Modem wechseln
- zusätzliche Switches ergänzen
- weitere Netzwerksegmente hinzufügen
- VPN-Konzept ändern

## Datenschutz

Nicht öffentlich dokumentiert werden:

- interne IP-Netze
- reale SSIDs
- private DNS-Namen
- Provider-Zugangsdaten
- Firewall-Backups
- exportierte Konfigurationen
