@echo off
chcp 65001 >nul
cd /d "%~dp0"
where node >nul 2>nul
if errorlevel 1 (
  echo Node.js is not installed. Trying to install it with winget...
  winget install -e --id OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements
  echo.
  echo Close this window and double-click setup-windows.bat again so Node.js is found.
  pause
  exit /b
)
node setup\install.mjs
echo.
pause
