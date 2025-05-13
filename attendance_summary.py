file = open("attendance.txt", "r")
attendance = {}

for line in file:
    parts = line.strip().split()
    if len(parts) < 3:
        continue
    name = parts[1]
    status = parts[2]

    if name not in attendance:
        attendance[name] = {"Present": 0, "Absent": 0, "Tardy": 0}

    attendance[name][status] += 1

file.close()

print("Name            Present      Absent   Tardy   Final Absents")
print("-----------------------------------------------------------")

for name in sorted(attendance.keys()):
    present = attendance[name]["Present"]
    absent = attendance[name]["Absent"]
    tardy = attendance[name]["Tardy"]
    final_absents = absent + (tardy // 3)

    print(f"{name:<15}{present:<12}{absent:<8}{tardy:<8}{final_absents}")

