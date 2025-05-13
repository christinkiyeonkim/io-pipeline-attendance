# attendance_summary.py
# Python script to summarize attendance from a virtual dataset.
# This was part of a practice combining Linux commands and Python scripting.
# 
# Troubleshooting log:
# - Fixed syntax error from accidental quote at end of for loop line.
# - Corrected variable name typo: 'presnet' -> 'present'.
# - Fixed f-string formatting error: malformed {tardy} field.
# - Added defensive check for empty lines to prevent IndexError.

# Open the attendance file
file = open("attendance.txt", "r")

# Dictionary to store each student's attendance counts
attendance = {}

# Read and parse each line
for line in file:
    parts = line.strip().split()
    if len(parts) < 3:
        continue  # Skip empty or malformed lines
    name = parts[1]
    status = parts[2]

    if name not in attendance:
        attendance[name] = {"Present": 0, "Absent": 0, "Tardy": 0}

    attendance[name][status] += 1

file.close()

# Display header
print("Name            Present      Absent   Tardy   Final Absents")
print("-----------------------------------------------------------")

# Summarize each student's final attendance
for name in sorted(attendance.keys()):
    present = attendance[name]["Present"]
    absent = attendance[name]["Absent"]
    tardy = attendance[name]["Tardy"]
    final_absents = absent + (tardy // 3)  # 3 Tardies count as 1 absence

    print(f"{name:<15}{present:<12}{absent:<8}{tardy:<8}{final_absents}")

