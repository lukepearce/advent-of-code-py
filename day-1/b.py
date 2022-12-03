import numpy as np

file = open("day-1/input.txt", "r")

# Read the contents of the file
all_elves = file.read()

individual_elves = all_elves.split("\n\n")

all_elves_calories = []

for elf in individual_elves:
    calories_for_this_elf = []

    # elf here is a string of calories like '3435\n2334\n4354\n3243'
    calories = elf.split("\n")

    # for loop here to convert each string to an int
    for calorie in calories:
        calorieInt = int(calorie)
        # add the int to the array
        calories_for_this_elf.append(calorieInt)

    # add the array to the list of arrays
    all_elves_calories.append(calories_for_this_elf)


all_elves_totals = []
# now we have an array of arrays, where each array is the calories for one elf
for elf in all_elves_calories:
    # for each elf, we want to get the sum of each calorie
    total_for_elf = np.sum(elf)
    # add the total to the list of totals
    all_elves_totals.append(total_for_elf)

# sort the totals
sorted_totals = np.sort(all_elves_totals)

# print the max value in the totals (to check it's the same as part a)
print(sorted_totals[-1])

top_three = sorted_totals[-3:]

print(sum(top_three))

# Close the file
file.close()
