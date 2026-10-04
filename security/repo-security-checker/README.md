# Repo Security Checker

Dieses Mini-Tool scannt dein Repository vor jedem Commit nach typischen Geheimnissen (Secrets) und sensiblen Daten.
Es ist bewusst simpel gehalten und kann an deine Beduerfnisse angepasst werden.

## Installation (einmalig pro Repo)
1) Ordner `tools/` in dein Repo kopieren.
2) Git Hook installieren:
   - Windows (PowerShell):
     ```powershell
     mkdir -force .git/hooks
     Copy-Item tools\hooks\pre-commit.ps1 .git\hooks\pre-commit.ps1 -Force
     ```
     *Hinweis:* Git fuer Windows startet Hooks standardmaessig als Bash-Skripte. Wenn du PS nutzen willst, kannst du stattdessen die Bash-Version nehmen.
   - Bash (empfohlen, auch unter Windows mit Git Bash):
     ```bash
     mkdir -p .git/hooks
     cp tools/hooks/pre-commit .git/hooks/pre-commit
     chmod +x .git/hooks/pre-commit
     ```

3) Abhaengigkeit:
   - Python 3 und `pyyaml`:
     ```bash
     pip install pyyaml
     ```

## Nutzung
- Beim `git commit` startet der Scan automatisch.
- Bei Warnungen wird der Commit blockiert. Die Funde werden als JSON mit Dateinamen und Textauszug angezeigt.
- Passen dir die Regeln nicht? Passe `tools/patterns.yml` an.

## Konfigurationsdatei
Siehe `tools/patterns.yml`. Dort kannst du Regex-Regeln und Ausschluesse bearbeiten.

## Grenzen
- False Positives sind moeglich (z. B. E-Mail in README).
- Dieses Tool ersetzt keine professionelle Secret-Scanning-Loesung, hilft aber, typische Fehler zu vermeiden.
