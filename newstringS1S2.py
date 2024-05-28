s1 = "Abc"
s2 = "Xyz"

s3 = ""
len_s1 = len(s1)
len_s2 = len(s2)
min_length = min(len_s1, len_s2)

for i in range(min_length):
    s3 += s1[i] + s2[-(i+1)]

if len_s1 > min_length:
    s3 += s1[min_length:]

if len_s2 > min_length:
    s3 += s2[:-(min_length+1):-1]

print("New string:", s3)
