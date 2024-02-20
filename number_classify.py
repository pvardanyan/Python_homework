print("Provide numbers with spaces: ")
string_numbers = input().split(" ")
numbers = [int(num) for num in string_numbers]

odd = []
even = []

def classify_numbers(numbers):
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

classify_numbers(numbers)
print("Odd numbers: ", odd)
print("Even numbers: ", even)
