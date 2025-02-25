T = int(input())
new_score = []
score = list(map(int,input().split()))
max_score = max(score)
for i in range(len(score)):
    new_score.append(score[i]/max_score*100)
print(f"{sum(new_score)/T}")