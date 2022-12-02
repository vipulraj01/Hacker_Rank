lists = []
a = int(input())
b = 1
while a>=b:
    b = b+1
    c = input()
    lists.append(c)
my_list = list(dict.fromkeys(lists))
print(len(my_list))