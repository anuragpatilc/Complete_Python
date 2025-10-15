# Calculate total expenses
expenses = [50, 120, 30, 200, 75]
total = sum(expenses)
print(f"Total expenses: ${total}")  # Output: Total expenses: $475

# Calculate average
average = sum(expenses) / len(expenses)
print(f"Average expense: ${average:.2f}")  # Output: Average expense: $94.00

# Sum with conditional (using generator)
grades = [85, 92, 78, 88, 95]
passing_grades_sum = sum(g for g in grades if g >= 80)
print(f"Sum of passing grades: {passing_grades_sum}")  # Output: Sum of passing grades: 450