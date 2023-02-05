# Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.

A = [int(input("vvedi chislo 1: \n")),
     int(input("vvedi chislo 2: \n")),
     int(input("vvedi chislo 3: \n")),
     int(input("vvedi chislo 4: \n"))]

for i in range(len(A)):
     print(str(i+1) + "-e chislo: " + str(A[i]))

count = 0
for x in range(len(A)):
     if A[x] % 2:
          count +=1

print("kolichestvo nechetnych chisel: " + str(count))