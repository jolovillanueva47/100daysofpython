print("Treasure Map")
row1 = ["📦","📦","📦"]
row2 = ["📦","📦","📦"]
row3 = ["📦","📦","📦"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
x_coordinate=int(position[1])-1
y_coordinate=int(position[0])-1
map[x_coordinate][y_coordinate]="💎"
print(f"{row1}\n{row2}\n{row3}")