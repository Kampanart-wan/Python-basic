rabbit = int(input())
scores = []
for i in range(rabbit):
    score = int(input())
    scores.append(score)
max_score = max(scores)
top_count = scores.count(max_score)
print(max_score)
print(top_count)