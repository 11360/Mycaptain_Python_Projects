list1=[12,-7,5,64,-14]
print("Input:list1 = {}".format(list1))
print("Output: ")
for i in list1:
     if i>0: k=print(i,end=",")
list2=[12,14,-95,3]
y=list(filter(lambda a:(a>0),list2))
print("\nInput:list2 = {} Output:{}".format(list2,y))
