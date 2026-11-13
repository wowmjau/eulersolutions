number = int(input("Number: "))
answer = 0

while number % 2 == 0:
	number //= 2 
	answer = 2

i = 3

while i * i <= number:
	while number % i == 0: 
		number //= i
		answer = i
	i += 2

if number > 1:
	answer = number

print(answer)
