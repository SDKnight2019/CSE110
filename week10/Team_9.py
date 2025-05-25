numbers = []
number = -1

while number !=0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

sum = 0

for number in numbers:
    sum += number

print(f"the sum is: {sum}")

count = len(numbers)
average = sum / count

print(f"the average is: {average}")

Best = -1

for number in numbers:
    if number > Best:
        Best = number

print(f"the largest number is: {Best}")