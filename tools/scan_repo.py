#!/usr/bin/env python3

import re, sys, json
from pathlib import Path
import fnmatch
import yaml

def load_config(cfg_path: Path):
    with cfg_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def should_exclude(path: Path, excludes):
    rel = str(path).replace("\\", "/")
    for pattern in excludes:
        if pattern.endswith("/") and rel.startswith(pattern):
            return True
        if fnmatch.fnmatch(rel, pattern):
            return True
    return False

def scan_file(path: Path, regexes):
    try:
        data = path.read_text(errors="ignore")
    except Exception:
        return []
    findings = []
    for rule in regexes:
        for m in re.finditer(rule["compiled"], data):
            # Show a short excerpt around match
            start = max(0, m.start() - 40)
            end = min(len(data), m.end() + 40)
            excerpt = data[start:end].replace("\n", "\\n")
            findings.append({
                "rule": rule["name"],
                "file": str(path),
                "span": [m.start(), m.end()],
                "excerpt": excerpt[:160]
            })
    return findings

def main():
    cfg_path = Path("tools/patterns.yml")
    if not cfg_path.exists():
        # fallback to current directory
        cfg_path = Path("patterns.yml")
    if not cfg_path.exists():
        print("Konfigurationsdatei patterns.yml nicht gefunden.", file=sys.stderr)
        sys.exit(2)
    cfg = load_config(cfg_path)
    excludes = cfg.get("exclude_paths", [])
    rules = []
    for r in cfg.get("secrets", []):
        try:
            c = re.compile(r["regex"])
            rules.append({"name": r["name"], "compiled": c})
        except re.error as e:
            print(f"Fehlerhaftes Regex in Regel '{r['name']}': {e}", file=sys.stderr)
    repo_root = Path(".")
    all_findings = []
    for p in repo_root.rglob("*"):
        if p.is_file():
            if should_exclude(p, excludes):
                continue
            # Skip our own tool files
            if "repo-security-checker" in str(p):
                continue
            # Reasonable size limit
            if p.stat().st_size > 2 * 1024 * 1024:
                continue
            findings = scan_file(p, rules)
            all_findings.extend(findings)
    if all_findings:
        print(json.dumps({"status":"WARN","findings":all_findings}, indent=2, ensure_ascii=False))
        sys.exit(1)
    else:
        print(json.dumps({"status":"OK","message":"Keine potenziellen Secrets gefunden."}, indent=2, ensure_ascii=False))
        sys.exit(0)

if __name__ == "__main__":
    main()
