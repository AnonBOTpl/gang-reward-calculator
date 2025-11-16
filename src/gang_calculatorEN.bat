@echo off
title Kalkulator Podzialu Nagrod - Gang
color 0A
echo.
echo ======================================
echo    KALKULATOR PODZIALU NAGROD GANG
echo ======================================
echo.
echo Uruchamianie aplikacji...
echo.

REM Sprawdz czy Python jest zainstalowany
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [BLAD] Python nie jest zainstalowany!
    echo.
    echo Pobierz Python z: https://www.python.org/downloads/
    echo Upewnij sie ze zaznaczyles "Add Python to PATH" podczas instalacji
    echo.
    pause
    exit /b 1
)

REM Sprawdz czy plik Python istnieje
if not exist "gang_calculatorEN.py" (
    echo [BLAD] Nie znaleziono pliku gang_calculator.py
    echo.
    echo Upewnij sie ze plik gang_calculator.py jest w tym samym folderze co uruchom_kalkulator.bat
    echo.
    pause
    exit /b 1
)

REM Uruchom aplikacje
echo Uruchamianie kalkulatora...
python gang_calculatorEN.py

REM Sprawdz czy aplikacja sie uruchomila prawidlowo
if %errorlevel% neq 0 (
    echo.
    echo [BLAD] Aplikacja zakonczyla sie z bledem!
    echo.
    echo Sprawdz czy:
    echo 1. Python jest poprawnie zainstalowany
    echo 2. Plik gang_calculator.py nie zawiera bledow
    echo.
    pause
)

echo.
echo Aplikacja zakonczona.
pause
