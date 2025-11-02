# 🤖 Enhanced Python Automation Tool

A powerful yet beginner-friendly Python automation toolkit that combines file management, data analysis, and expense tracking into one comprehensive solution. Built with pandas and numpy for efficient data processing.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## ✨ Features

### 📊 Smart File Organizer
- Automatically categorizes files by type (Images, Documents, Videos, Music, Archives)
- Generates detailed Excel reports with statistics
- Shows largest files, oldest files, and total storage usage
- Visualizes data distribution by category

### 💰 Expense Tracker
- Track daily expenses with automatic date stamping
- Categorize spending (Food, Transport, Bills, Shopping, etc.)
- Monthly spending reports with trend analysis
- Calculate spending patterns using numpy
- Export comprehensive reports to Excel

### 🔍 Advanced Duplicate Finder
- Identifies duplicate files using pandas grouping
- Calculates wasted storage space
- Displays results in clean tabular format
- Helps optimize disk usage

### 📅 File Age Analyzer
- Analyzes files by modification date
- Categorizes by age groups (< 1 week, 1-4 weeks, 1-3 months, etc.)
- Provides statistical insights (mean, max, min ages)
- Suggests cleanup opportunities for old files

### ✏️ Smart Batch Rename
- Preview changes before applying
- Multiple renaming options:
  - Add prefix/suffix
  - Replace text
  - Sequential numbering
- Prevents accidental overwrites

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/python-automation-tool.git
cd python-automation-tool
```

2. Install required dependencies:
```bash
pip install pandas numpy openpyxl
```

3. Run the program:
```bash
python automation.py
```

## 📖 Usage

### Quick Start

Run the program and select from the interactive menu:

```
     ENHANCED PYTHON AUTOMATION TOOL
     (with pandas & numpy)
============================================================
1. Smart File Organizer (with Excel report)
2. Expense Tracker
3. Find Duplicate Files (Advanced)
4. Analyze File Ages
5. Smart Batch Rename
6. Exit
============================================================
```

### Example Workflows

#### Organizing Downloads Folder
1. Select option `1` from the menu
2. The tool will scan your Downloads folder
3. Review the generated statistics and Excel report
4. Choose to organize files into categorized folders

#### Tracking Expenses
1. Select option `2` from the menu
2. Add expenses with date, category, description, and amount
3. View summaries and monthly reports
4. Export data to Excel for further analysis

#### Finding Duplicates
1. Select option `3` from the menu
2. Enter the folder path to scan
3. Review duplicate files and wasted space
4. Manually delete duplicates as needed

## 📁 Project Structure

```
python-automation-tool/
│
├── automation.py          # Main program file
├── expenses.csv          # Generated expense data (created on first use)
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## 🛠️ Technologies Used

- **Python 3.7+**: Core programming language
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations and statistics
- **openpyxl**: Excel file generation
- **pathlib**: Modern file path handling

## 📊 Sample Output

### File Organization Report
```
FILE ANALYSIS REPORT
============================================================
Total Files: 156
Total Size: 2,458.32 MB

--- Files by Category ---
Category     Count  Size (MB)
Images          45     823.45
Documents       67     892.12
Videos          12   1,234.56
Music           28     456.78
Other            4      51.41
```

### Expense Summary
```
--- Expense Summary ---
Total Expenses: $1,234.56
Average Expense: $41.15
Number of Transactions: 30

--- By Category ---
Food: $456.78 (37.0%)
Transport: $234.56 (19.0%)
Bills: $345.67 (28.0%)
Shopping: $197.55 (16.0%)
```

## 🎓 Learning Outcomes

This project is perfect for learning:

- File system operations in Python
- Data analysis with pandas DataFrames
- Statistical calculations with numpy
- CSV and Excel file handling
- Creating interactive CLI applications
- Organizing and structuring Python projects

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- Expense tracker requires manual date entry (future: auto-complete)
- File organizer doesn't handle nested directories (planned feature)
- Large folders may take time to scan (optimization planned)

## 🔮 Future Enhancements

- [ ] Add GUI interface using tkinter
- [ ] Implement scheduled automation tasks
- [ ] Add cloud backup integration
- [ ] Create data visualization charts
- [ ] Add email notification support
- [ ] Implement file compression utilities
- [ ] Add regex support for advanced renaming

## 👨‍💻 Author

**Your Name**
- GitHub: [@MD-Farihan](https://github.com/MD-Farihan)
- Email: mdfarihan726@gmail.com

## 🙏 Acknowledgments

- Inspired by the need to automate repetitive tasks
- Built as a learning project for Python automation
- Thanks to the pandas and numpy communities

## 📞 Support

If you have any questions or run into issues:

1. Check the [Issues](https://github.com/yourusername/python-automation-tool/issues) page
2. Create a new issue with details
3. Reach out via email

---

⭐ **If you find this project helpful, please consider giving it a star!** ⭐

Made with ❤️ and Python
