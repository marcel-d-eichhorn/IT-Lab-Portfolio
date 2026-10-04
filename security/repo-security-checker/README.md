# Repo Security Checker

Ein leichtgewichtiger Python-Scanner, der ein Git-Repository vor dem Commit auf typische Secrets und sensible Inhalte prüft.

Das Projekt dient als einfache zusätzliche Schutzschicht im lokalen Git-Workflow und demonstriert die Kombination aus **Python, Regex, YAML-Konfiguration und Git Hooks**.

## Funktionsweise

```text
git commit
    │
    ▼
Pre-Commit Hook
    │
    ▼
scan_repo.py
    │
    ├── patterns.yml laden
    ├── Dateien prüfen
    ├── Ausschlüsse anwenden
    └── Treffer bewerten
            │
            ├── kein Treffer → Commit erlaubt
            └── Treffer      → Commit abgebrochen
```

## Erkannte Muster

Die mitgelieferte Konfiguration prüft unter anderem auf:

- Private-Key-Blöcke
- generische API Keys / Tokens
- Azure Connection Strings
- AWS Access Keys
- mögliche Passwörter im Code
- JWT-ähnliche Tokens
- E-Mail-Adressen
- IPv4-Adressen

Die Regeln befinden sich in `tools/patterns.yml` und können erweitert oder angepasst werden.

## Installation

### Bash / Git Bash

```bash
mkdir -p .git/hooks
cp tools/hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
pip install pyyaml
```

### PowerShell

```powershell
New-Item -ItemType Directory -Force .git/hooks
Copy-Item tools\hooks\pre-commit.ps1 .git\hooks\pre-commit.ps1 -Force
pip install pyyaml
```

> Git for Windows führt Hooks standardmäßig über eine Unix-kompatible Shell aus. Für einen möglichst portablen Workflow ist daher der Bash-Hook die unkompliziertere Variante.

## Nutzung

Beim nächsten `git commit` startet der Scanner automatisch.

Ohne Treffer:

```json
{
  "status": "OK",
  "message": "Keine potenziellen Secrets gefunden."
}
```

Bei einem Treffer wird der Commit mit Exit Code `1` blockiert und der Fund als JSON ausgegeben.

## Projektstruktur

```text
repo-security-checker/
├── README.md
└── tools/
    ├── scan_repo.py
    ├── patterns.yml
    └── hooks/
        ├── pre-commit
        └── pre-commit.ps1
```

## Grenzen

Das Tool ist bewusst einfach gehalten:

- Regex-basierte Erkennung kann False Positives erzeugen.
- Es ersetzt keine professionelle Secret-Scanning-Lösung.
- Bereits veröffentlichte Secrets werden dadurch nicht rückwirkend entfernt.
- Bei einem echten Leak müssen betroffene Zugangsdaten zusätzlich rotiert werden.

Für kleine Labs und persönliche Repositories ist es trotzdem ein sinnvoller zusätzlicher Sicherheitscheck.
