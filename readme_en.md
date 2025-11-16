# 🏆 Gang Reward Split Calculator

**A simple and intuitive calculator for fair distribution of rewards among gang members based on their contribution.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)](https://www.microsoft.com/windows)

[🇵🇱 Wersja polska](README_PL.md) | [📥 Download Latest Release](../../releases/latest)

---

## ✨ Features

- 🎯 **Fair distribution** based on mined blocks
- ⭐ **Support bonuses** for helpers (configurable %)
- 📊 **Visual ranking** with medals (🥇🥈🥉)
- 💾 **Export results** to text file
- 🎨 **Modern GUI** with dark theme
- 🌐 **Available in English and Polish**

## 🖼️ Preview

The calculator allows you to:
- Enter the number of players (2-20)
- Set the total reward pool
- Track blocks mined by each player
- Add percentage bonuses for support
- View detailed results with ranking
- Save results to file

## 📥 Installation & Usage

### Option 1: Standalone .exe (Recommended - No Python required!)

1. Go to [Releases](../../releases/latest)
2. Download `GangRewardCalculator_EN.exe`
3. Double-click to run

**⚠️ Windows SmartScreen Warning:**
If Windows shows a warning:
1. Click "More info"
2. Click "Run anyway"

This is normal for apps without a paid code signing certificate.

### Option 2: Run from Python source

**Requirements:**
- Python 3.8 or newer
- tkinter (usually included with Python)

**Steps:**
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/gang-reward-calculator.git
cd gang-reward-calculator

# Run the application
python src/gang_calculatorEN.py
```

Or use the batch file (Windows):
```bash
src/gang_calculatorEN.bat
```

## 🎮 How to Use

1. **Set the number of players** (default: 8)
2. **Enter the reward pool** in credits (default: 15,000)
3. **Fill in player data:**
   - Player names
   - Number of blocks mined
   - Optional: Check bonus and set percentage (default: 3%)
4. Click **🔢 CALCULATE**
5. View results with ranking
6. Optionally save results with **💾 SAVE**

## 📊 Calculation Method

**Base distribution:**
```
Player Share = (Player Blocks / Total Blocks) × Reward Pool
```

**With support bonus:**
```
Final Credits = Base Credits + (Base Credits × Bonus %)
```

## 🛠️ Building .exe from source

If you want to create your own .exe:

```bash
# Install PyInstaller
pip install pyinstaller

# Build English version
pyinstaller --onefile --windowed --name="GangRewardCalculator_EN" src/gang_calculatorEN.py

# Build Polish version
pyinstaller --onefile --windowed --name="GangRewardCalculator_PL" src/gang_calculatorPL.py

# Find .exe files in dist/ folder
```

## 🔒 Security & Privacy

- ✅ **No internet connection required** - works 100% offline
- ✅ **No data collection** - everything stays on your computer
- ✅ **Open source** - you can review all code
- ✅ **No installation needed** - portable .exe file
- ✅ **Virus scan available** - [Check on VirusTotal](https://www.virustotal.com)

## 🐛 Troubleshooting

**App won't start?**
- Make sure you downloaded the correct version (EN/PL)
- Try running as Administrator
- Check if antivirus isn't blocking the file

**Calculation errors?**
- Ensure all blocks are positive numbers
- Check that reward pool is greater than 0
- Verify bonus percentages are between 0-100%

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Created with ❤️ for fair gang reward distribution

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⭐ Support

If you find this project useful, please give it a star! ⭐

---

**Made for gang leaders who value fairness** 🏆