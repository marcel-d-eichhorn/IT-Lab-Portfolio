# Simple pre-commit hook: scan repo for secrets before committing
$toolsDir = "tools"
$scanner = Join-Path $toolsDir "scan_repo.py"

if (Test-Path $scanner) {
  Write-Host "[pre-commit] Running security scan..."
  python $scanner
  if ($LASTEXITCODE -ne 0) {
    Write-Error "[pre-commit] Security scan failed. Commit aborted."
    exit 1
  }
} else {
  Write-Host "[pre-commit] Scanner not found at $scanner (skipping)."
}
