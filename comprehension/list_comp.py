#using list comprehension we can take these 4 lines of code to sthong looks likt this 
# new_list = [new_item for item in list]

# numbers = [1,2,3]
# # new_numbers = []
# # for num in numbers:
# #     num += 1 
# #     new_numbers.append(num)
# # print(new_numbers)

# new_numbers = [(num+1) for num in numbers]
# print(new_numbers)

# new_list = [num * num for num in range(0,10)]
# print(new_list)
# new_list2 = [num for num in range(0,21)  if num%2==0 ]
# print(new_list2)


# name = "ANGELA"
# letters_list = [letter for letter in name]
# print(letters_list)

new_list = [num + num for num in range(1,5)]
print(new_list)

# new_list = [new_item for item in list if test]


names = ["Alex","Beth","Dave","Eleanor","Freddie"]
short_names = [name.upper() for name in names if len(name) <= 4]
print(short_names)