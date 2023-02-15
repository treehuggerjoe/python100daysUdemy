
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
add_height = 0
for height in student_heights:
    add_height += height
average_height = add_height / len(student_heights)

print(" {:.0f}".format(average_height))

