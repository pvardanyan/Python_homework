print("Provide numbers with spaces: ")
string_numbers = input().split(" ")
numbers = [int(num) for num in string_numbers]

print("Do you want ot exclude the negative numbers? (y/n)")
exclude_negative = True if input() == 'y' else False

def sum_of_elements(numbers,exclude=False):
    sum = 0
    for i in numbers:
        if exclude and i > 0:
            sum += i
        elif not exclude:
            sum += i
    return sum
sum = sum_of_elements(numbers,exclude_negative)
print(sum)

