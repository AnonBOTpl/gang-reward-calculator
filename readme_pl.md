# 🏆 Kalkulator Podziału Nagród Gang

**Prosty i intuicyjny kalkulator do sprawiedliwego podziału nagród między członków gangu na podstawie ich wkładu.**

[![Licencja: MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platforma](https://img.shields.io/badge/platforma-Windows-blue.svg)](https://www.microsoft.com/windows)

[🇬🇧 English version](README.md) | [📥 Pobierz najnowszą wersję](../../releases/latest)

---

## ✨ Funkcje

- 🎯 **Sprawiedliwy podział** na podstawie wydobytych bloków
- ⭐ **Bonusy za wsparcie** dla pomocników (konfigurowalny %)
- 📊 **Wizualny ranking** z medalami (🥇🥈🥉)
- 💾 **Eksport wyników** do pliku tekstowego
- 🎨 **Nowoczesny interfejs** z ciemnym motywem
- 🌐 **Dostępny w języku angielskim i polskim**

## 🖼️ Podgląd

Kalkulator pozwala na:
- Wprowadzenie liczby graczy (2-20)
- Ustawienie puli nagród
- Śledzenie bloków wydobytych przez każdego gracza
- Dodawanie procentowych bonusów za wsparcie
- Przeglądanie szczegółowych wyników z rankingiem
- Zapisywanie wyników do pliku

## 📥 Instalacja i użytkowanie

### Opcja 1: Samodzielny .exe (Zalecane - nie wymaga Pythona!)

1. Przejdź do [Wydania](../../releases/latest)
2. Pobierz `GangRewardCalculator_PL.exe`
3. Kliknij dwukrotnie, aby uruchomić

**⚠️ Ostrzeżenie Windows SmartScreen:**
Jeśli Windows wyświetli ostrzeżenie:
1. Kliknij "Więcej informacji"
2. Kliknij "Uruchom mimo to"

To normalne dla aplikacji bez płatnego certyfikatu podpisu cyfrowego.

### Opcja 2: Uruchomienie z kodu źródłowego Python

**Wymagania:**
- Python 3.8 lub nowszy
- tkinter (zwykle dołączony do Pythona)

**Kroki:**
```bash
# Sklonuj repozytorium
git clone https://github.com/TWOJA_NAZWA/gang-reward-calculator.git
cd gang-reward-calculator

# Uruchom aplikację
python src/gang_calculatorPL.py
```

Lub użyj pliku batch (Windows):
```bash
src/gang_calculatorPL.bat
```

## 🎮 Jak używać

1. **Ustaw liczbę graczy** (domyślnie: 8)
2. **Wprowadź pulę nagród** w kredytach (domyślnie: 15 000)
3. **Wypełnij dane graczy:**
   - Nazwy graczy
   - Liczba wydobytych bloków
   - Opcjonalnie: Zaznacz bonus i ustaw procent (domyślnie: 3%)
4. Kliknij **🔢 OBLICZ**
5. Zobacz wyniki z rankingiem
6. Opcjonalnie zapisz wyniki przyciskiem **💾 ZAPISZ**

## 📊 Metoda obliczeń

**Podstawowy podział:**
```
Udział gracza = (Bloki gracza / Suma bloków) × Pula nagród
```

**Z bonusem za wsparcie:**
```
Końcowe kredyty = Podstawowe kredyty + (Podstawowe kredyty × Bonus %)
```

## 🛠️ Budowanie .exe ze źródła

Jeśli chcesz stworzyć własny .exe:

```bash
# Zainstaluj PyInstaller
pip install pyinstaller

# Zbuduj wersję polską
pyinstaller --onefile --windowed --name="GangRewardCalculator_PL" src/gang_calculatorPL.py

# Zbuduj wersję angielską
pyinstaller --onefile --windowed --name="GangRewardCalculator_EN" src/gang_calculatorEN.py

# Znajdź pliki .exe w folderze dist/
```

## 🔒 Bezpieczeństwo i prywatność

- ✅ **Nie wymaga połączenia z internetem** - działa 100% offline
- ✅ **Brak zbierania danych** - wszystko zostaje na Twoim komputerze
- ✅ **Otwarty kod źródłowy** - możesz przejrzeć cały kod
- ✅ **Nie wymaga instalacji** - przenośny plik .exe
- ✅ **Dostępne skanowanie wirusów** - [Sprawdź na VirusTotal](https://www.virustotal.com)

## 🐛 Rozwiązywanie problemów

**Aplikacja się nie uruchamia?**
- Upewnij się, że pobrałeś prawidłową wersję (EN/PL)
- Spróbuj uruchomić jako Administrator
- Sprawdź, czy antywirus nie blokuje pliku

**Błędy w obliczeniach?**
- Upewnij się, że wszystkie bloki to liczby dodatnie
- Sprawdź, czy pula nagród jest większa od 0
- Zweryfikuj, czy procenty bonusów są między 0-100%

## 📄 Licencja

Ten projekt jest licencjonowany na licencji MIT - szczegóły w pliku [LICENSE](LICENSE).

## 👤 Autor

**AnonBOT** - Stworzone z ❤️ dla sprawiedliwego podziału nagród w gangach

## 🤝 Współpraca

Wkład, zgłaszanie problemów i propozycje funkcji są mile widziane!

1. Sforkuj projekt
2. Stwórz swoją gałąź funkcji (`git checkout -b feature/NowaCecha`)
3. Zatwierdź swoje zmiany (`git commit -m 'Dodaj jakąś nową cechę'`)
4. Wypchnij do gałęzi (`git push origin feature/NowaCecha`)
5. Otwórz Pull Request

## ⭐ Wsparcie

Jeśli uznasz ten projekt za przydatny, zostaw gwiazdkę! ⭐

---

**Stworzone dla liderów gangów, którzy cenią sprawiedliwość** 🏆