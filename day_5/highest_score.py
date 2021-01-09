student_scores = input("Input a list of student score ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
tmp=0
for score in student_scores:
    if score > tmp:
        tmp=score
print(f"The highest score in class is: {tmp}")