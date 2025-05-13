# 📊 Attendance Analyzer

A mini-project to practice **Linux I/O pipeline commands** and **Python scripting** using a virtual attendance log.  
This project was built on a work **MacBook Air** (macOS terminal + vim).

---

## 📂 Project Overview

This project:

- Reads attendance data from `attendance.txt`
- Analyzes the number of `Present`, `Absent`, and `Tardy` entries per student
- Applies the rule: **3 Tardies = 1 Absent**
- Prints a summary table using formatted output

---

## 🛠 Technologies Used

- Linux CLI: `cat`, `grep`, `sort`, `uniq`, `|`
- Python: file I/O, string manipulation, dictionaries, f-strings
- GitHub: project version control & portfolio visibility
- Terminal editor: `vim` on macOS

---

## 📁 Files

| File                  | Description                                  |
|-----------------------|----------------------------------------------|
| `attendance.txt`      | Sample attendance log (Jan 1–5, 2025)        |
| `attendance_summary.py` | Python script to summarize attendance     |
| `README.md`           | Project explanation & troubleshooting log    |

---

## 🧪 Sample Output

```
Name        Present  Absent  Tardy  Final Absents
-------------------------------------------------
Alpha       5        0       0      0
Beta        3        2       0      2
...
```

---

## 🧱 Linux CLI Practice

```bash
cat attendance.txt | grep "Absent" | sort | uniq
```

Used to filter and analyze the attendance log from the terminal.  
Great for learning I/O pipelines and basic log parsing.

---

## 🐍 Python Script

Run the script:

```bash
python3 attendance_summary.py
```

It calculates each student's summary and prints a formatted result.

---

## 🧰 Troubleshooting Experience

While building this, I encountered real beginner issues and solved them myself:

- ❌ **SyntaxError: EOL while scanning string literal**  
  → Fixed a rogue `"` after `for` loop

- ❌ **f-string: single '}' is not allowed**  
  → Corrected formatting: `<tardy:<6}` → `{tardy:<6}`

- ❌ **NameError: name 'attendance' is not defined**  
  → Added `attendance = {}` at the top

- ❌ **IndexError: list index out of range**  
  → Handled blank lines with `if len(parts) < 3: continue`

- ❌ **Only one student printed**  
  → Fixed logic where attendance wasn't updating correctly

These are all normal first-time mistakes — debugging them taught me a lot. 👍

---

## 🤔 Why I Made This

To combine:

- Practical Linux command usage  
- Beginner-friendly but real Python scripting with logic

This is one of my first hands-on IT learning repos, and more will follow.

