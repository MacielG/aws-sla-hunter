@echo off
REM Initialize Git repository and create GitHub repo

cd /d "C:\Users\guilh\Documents\aws-sla-hunter"

echo Initializing Git repository...
git init

echo Configuring Git user...
git config user.name "MacielG"
git config user.email "guilhermecosmo@example.com"

echo Adding all files...
git add .

echo Creating initial commit...
git commit -m "Initial commit: AWS SLA Hunter CLI - Production ready"

echo Creating GitHub repository...
gh repo create aws-sla-hunter --public --source=. --remote=origin --push

echo.
echo ============================================
echo Repository created and published!
echo https://github.com/MacielG/aws-sla-hunter
echo ============================================
