import sys
item_list = sys.argv
item_list.pop(0)
i = len(item_list)
if i <= 2:
    print("none")
else:
    reversed_list = item_list[::-1]
for x in range(i):
    print(reversed_list[x])