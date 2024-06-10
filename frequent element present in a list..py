a = [4, 5, 6, 4, 6, 7, 4, 2, 4, 8, 4]
count_dict = {}
for num in a:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
most_frequent_element = max(count_dict, key=count_dict.get)
print("The most frequent element is:", most_frequent_element)
