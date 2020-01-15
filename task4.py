numbers = input("Enter numbers with spaces: ").split(" ")
for i in range(len(numbers)):
	numbers[i] = int(numbers[i])
numbers.sort()
print(numbers)

if max(numbers) <= 0:
	print(1)
else:
	for i in range(1,max(numbers)+2):
		if i > 0 and i not in numbers:
			print(i)
			break
		else:
			continue