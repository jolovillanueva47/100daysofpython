student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total=0
count=0
for height in student_heights:
    count+=1
    total+=height
avg=round(total/count)
print(avg)
