letter_grades = {
    "A":4,
    "B":3,
    "C":2,
    "D":1
}
letter_grades["F"] = 0  # square brackets are used when adding to dictionary
print(letter_grades)

# Updating/changing grade values
letter_grades.update({
    "A":4.0,
    "B":3.0,
    "C":2.0,
    "D":1.0,
    "F":0.0
})
print(letter_grades)

# Prints the letter grades
print(letter_grades.keys())

# To print each letter each on a new line
for i in letter_grades.keys():
    print(i)

# Prints the grade values
print(letter_grades.values())

# Prints the grade values on each on a new line
for i in letter_grades.values():
    print(i)

# Prints out the whole dictionary
print(letter_grades.items())

# Prints out each item in dictionary on new line
for i, j in letter_grades.items():
    print(i,j)

# Prints the value of letter grade "A"
print(letter_grades["A"])


def get_key(arg, dictionary):
    for key, value in dictionary.items():
        if value == arg:
            return key


x = get_key(2.0, letter_grades)
print(x)


grades = ["A","B","C","D","B","C","A","C","F"]

# Counts the amount of each item in grades <-(list)
count = {}
for i in grades:
    count[i] = count.get(i,0) + 1
print(count)