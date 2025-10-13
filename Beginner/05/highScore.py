student_scores = [78, 65, 89, 86, 55, 91, 64, 89,23, 45, 67, 89, 90, 91, 92, 93, 34, 95,56, 97, 98, 93,90, 100, 45, 67, 89, 90, 91, 92, 93, 34, 95,56, 97, 98, 93]

max_score = 0
for score in student_scores:
  if score > max_score:
    max_score = score

print(max_score)

# intially
# maxscore = 0, score 78
# maxscore = 78, score 78
# maxscore = 78, score 65
# maxscore = 78, score 89
# maxscore = 89, score 55

# so it keeps on looping to find the max score till the list ends.