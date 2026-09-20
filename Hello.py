name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))

total = maths + python + english
percentage = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")