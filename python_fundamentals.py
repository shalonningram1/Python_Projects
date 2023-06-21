
sum_scores = []
total_sum = 0

for i in range(1, 6):
    scores = int(input("Enter test score: "))

    if scores > 100 or scores < 0:
                raise ValueError("Out of range")
    sum_scores.append(scores)
    

for score in sum_scores:
    total_sum += score

average_score = int(total_sum/len(sum_scores))

if average_score > 90:
    print("Your Average Score is: " + str(average_score) + ". " + "Your Final Grade is A.")
elif average_score <= 89 and average_score >= 80:
    print("Your Average Score is: " + str(average_score) + ". " + "Your Final Grade is B.")
elif average_score <= 79 and average_score >= 70:
    print("Your Average Score is: " + str(average_score) + ". " + "Your Final Grade is C.")
elif average_score <= 69 and average_score >= 60:
    print("Your Average Score is: " + str(average_score) + ". " + "Your Final Grade is D.")
else:
    print("Your Average Score is: " + str(average_score) + ". " + "Your Final Grade is F.")
