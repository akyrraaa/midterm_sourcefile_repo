# Store the raw comma-separated records.
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,",
]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

# PART A: Parse and organize the records.
for record in raw_records:
    # Split the record into fields.
    fields = record.split(",")

    # Guardian condition: skip if not exactly 4 fields (name + 3 scores).
    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    # Store the student's name.
    name = fields[0]

    # Convert the score fields to numbers safely.
    try:
        scores = [int(score) for score in fields[1:]]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    # Add the name and scores to student_scores.
    student_scores[name] = scores


# PART B: Display records alphabetically.
print("\nORGANIZED STUDENT RECORDS")

for name in sorted(student_scores):
    print(f"{name}: {student_scores[name]}")


# Create a list for result tuples.
ranking = []

# Create counters for the class summary.
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate the student results.
for name, scores in student_scores.items():
    # Guard against an empty score list.
    if len(scores) == 0:
        continue

    # Calculate total, average, highest, and lowest.
    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    # Determine the student's remark.
    if average >= PASSING_GRADE:
        remark = "Passed"
    else:
        remark = "Failed"

    # Update the passed or failed counter.
    if remark == "Passed":
        passed_count += 1
    else:
        failed_count += 1

    # Add the average to sum_of_averages.
    sum_of_averages += average

    # Append the result tuple to ranking.
    ranking.append((average, name, highest_score, lowest_score, remark))


# PART D: Sort and display the ranking.
# Sort ranking from highest to lowest average.
ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

for rank, (average, name, highest_score, lowest_score, remark) in enumerate(ranking, start=1):
    print(f"{rank:<5} {name:<10} {average:<8.2f} {highest_score:<8} {lowest_score:<7} {remark}")


# PART E: Display the class summary.
# Calculate the class average safely.
if len(ranking) > 0:
    class_average = sum_of_averages / len(ranking)
else:
    class_average = 0

# Use ranking[0] and ranking[-1] safely.
print("\nCLASS SUMMARY")
print(f"Number of Students: {len(ranking)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")

if len(ranking) > 0:
    highest_student = ranking[0]
    lowest_student = ranking[-1]
    print(f"Highest: {highest_student[1]} - {highest_student[0]:.2f}")
    print(f"Lowest: {lowest_student[1]} - {lowest_student[0]:.2f}")