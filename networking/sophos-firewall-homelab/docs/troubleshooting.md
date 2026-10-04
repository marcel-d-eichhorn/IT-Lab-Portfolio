# Troubleshooting Case Study – RAM-Upgrade der Firewall

## Ausgangslage

Die Firewall-Hardware sollte mit zusätzlichem Arbeitsspeicher erweitert werden.

Nach dem Einbau eines größeren DDR3L-Moduls startete das Gerät jedoch nicht mehr korrekt:

- kein Bild
- rote Statusanzeige
- Management-Oberfläche nicht erreichbar

## Eingrenzung

Da das Problem unmittelbar nach dem RAM-Tausch auftrat, wurde die Hardwareänderung als erste Fehlerquelle betrachtet.

Vorgehen:

1. Stromversorgung trennen
2. neuen RAM entfernen
3. ursprüngliches Modul wieder einsetzen
4. Gerät erneut starten
5. Management-Zugriff prüfen

## Ergebnis

Mit dem ursprünglichen Speicher startete die Firewall wieder normal und die Management-Oberfläche war erreichbar.

Damit ließ sich der Fehler auf das neu eingesetzte RAM-Modul bzw. dessen Funktionsfähigkeit eingrenzen.

## Bewertung

Der Fehler lag nicht an:

- Firewall-Konfiguration
- Netzwerkverkabelung
- Betriebssystem
- Management-Zugang

sondern an der unmittelbar zuvor geänderten Hardware.

## Lessons Learned

- Nach Hardwareänderungen immer zuerst die letzte Änderung rückgängig machen.
- Bei fehlendem POST oder Bild ist Software-Troubleshooting zunächst zweitrangig.
- Ein Rückbau auf den bekannten funktionierenden Zustand ist ein schneller A/B-Test.
- Kompatible Spezifikationen bedeuten nicht automatisch, dass ein konkretes Modul fehlerfrei ist.
- Infrastruktur-Troubleshooting beginnt oft mit sauberem Ausschlussverfahren statt mit komplexen Tools.

## Allgemeines Muster

```text
Änderung
   ↓
Fehler tritt auf
   ↓
letzte Änderung isolieren
   ↓
bekannten funktionierenden Zustand wiederherstellen
   ↓
Ergebnis vergleichen
   ↓
Ursache eingrenzen
```
