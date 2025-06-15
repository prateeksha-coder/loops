num = 23
print("Table of 23")
for i in range(1,11):
  mul = num*i
  print(f"23 x {i} = {mul}")

n = int(input("enter number of rows"))

for i in range(0, n):

	for j in range(0, i+1):
		print("*", end=" ")

	print("\n")

num = int(input("Enter number to be checked :"))

flag = False

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

num = 1
sum = 0
while(num<=10):
  sum = sum+num
  num = num+1

print("Sum of First 10 Natural Numbers :", sum)
