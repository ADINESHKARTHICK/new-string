a = [45, 67, 83, 24, 55, 87, 77, 34]
number_to_find = 55
position = None
for index, value in enumerate(a):
    if value == number_to_find:
        position = index
        break
if position is not None:
    print("The position of", number_to_find, "is:", position)
else:
    print("The number", number_to_find, "is not present in the list.")
