first_name = "Christina"
last_name = "Woodhams"

age = 26
age = 12
age = 15

# print(age)
# print(first_name, last_name)

# if age >= 18:
#     print("I am an adult.")
# elif age <13:
#     print("I am an infant.")
# else:
#     print("I am an alien.")

favorite_numbers = [1, 2, 3, 4, 5, 6, "hello", True, 2.0]
# print(favorite_numbers)

# for number in favorite_numbers:
#     print(number)


def sum(num1, num2):
    return (num1 + num2)

# print (sum(1, 2))

open_file = open("FinalGrades.csv")
total_a = 0
total_b = 0
total_c = 0

for line in open_file:
    line = line.strip()
    values = line.split(',')
    print(values)
    for value in values:
        if value == "A":
            total_a += 1
        elif value == "B":
            total_b += 1
        elif value == "C":
            total_c += 1
print("A's:", total_a, "B's:", total_b, "C's:", total_c)

for line in open_file:
    line = line.strip()
    values = line.split(",")
    print(values[2: 5])

open_file.close()

prime_number = float(1)