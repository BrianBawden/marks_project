
error_count = 0
warning_count = 0

error_list = []
warning_list = []

with open(r"C:\Users\brian\OneDrive\Desktop\marks_project\SAP20p1-Prelim_1.log", "r") as f:

    for line in f:
        if "WARNING -" in line:
            warning_count += 1
            warning_list.append(line)
        elif "ERROR -" in line:
            error_count += 1
            error_list.append(line)

print()
print("Number of warnings:", warning_count)
print(*warning_list, sep="\n")
print()

print("Number of errors:", error_count)
print(*error_list, sep="\n")
print()


print(input("Press enter to close."))