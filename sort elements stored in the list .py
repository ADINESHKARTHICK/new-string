numbers = [5, 3, 7, 9, 8, 4, 2]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
ascending_order = numbers
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
descending_order = numbers
print("Ascending Order:", ascending_order)
print("Descending Order:", descending_order)
