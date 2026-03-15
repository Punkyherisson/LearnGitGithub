# git-all.ps1 - Simple et sûr
$root = "C:\Github.com\Punkyherisson"

Get-ChildItem $root -Directory | Where-Object { Test-Path "$($_.FullName)\.git" } | ForEach-Object {
    $repo = $_.Name
    Write-Host "=== $repo ===" -ForegroundColor Cyan
    Push-Location $_.FullName
    git status -s
    git log --oneline -3
    Pop-Location
    ""
}

Write-Host "Scan fini ! $(Get-ChildItem $root -Directory | Where-Object { Test-Path "$($_.FullName)\.git" } | Measure-Object).Count repos" -ForegroundColor Green
