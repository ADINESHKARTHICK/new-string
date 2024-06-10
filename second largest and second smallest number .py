numbers = [23, 45, 67, 12, 98, 34, 56, 21]
second_largest = None
second_smallest = None
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif second_largest is None or num > second_largest:
        second_largest = num
        
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif second_smallest is None or num < second_smallest:
        second_smallest = num
print("The second largest number is:", second_largest)
print("The second smallest number is:", second_smallest)
