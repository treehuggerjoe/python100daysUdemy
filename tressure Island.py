# 🚨 Don't change the code below 👇
from bokeh.layouts import row

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
split_row1 = list(str(position))
fill_culumn = int(split_row1[0])
fill_row = int(split_row1[1])


map[fill_row-1][fill_culumn-1] ="X"

print(f"{row1}\n{row2}\n{row3}")



