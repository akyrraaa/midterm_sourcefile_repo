scores = [85, 72, 91, 64, 78]

print("Student Scores:")
for score in scores:
    print(score)

print()

total_score = 0
passed_count = 0
failed_count = 0
highest_score = scores[0]
lowest_score = scores[0]

for i, score in enumerate(scores, start=1):
    if score >= 90: remark = "Excellent"
    elif score >= 80: remark = "Very Good"
    elif score >= 75: remark = "Good"
    else: remark = None

    if score >= 75:
        status = "Passed"
        passed_count += 1
        print(f"Student {i}: {score} - {remark} - {status}")
    else:
        status = "Failed"
        failed_count += 1
        print(f"Student {i}: {score} - {status}")

    total_score += score
    if score > highest_score: highest_score = score
    if score < lowest_score: lowest_score = score

average_score = total_score / len(scores)

print()
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.0f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")