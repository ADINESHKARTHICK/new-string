numbers = [23, 45, 67, 12, 98, 34, 56, 21]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
print("The largest number is:", largest)
print("The smallest number is:", smallest)
