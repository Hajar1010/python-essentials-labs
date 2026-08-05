
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

list=[]
for i in my_list:
    if i not in list:
            list.append(i)
my_list=list
print("The list with unique elements only:")
print(my_list)

