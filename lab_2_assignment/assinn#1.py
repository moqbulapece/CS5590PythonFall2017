strin='My name is Md Moqbull hossen hossen'
z= strin.split()#make a list from the sgtring words
print z
list1=[]
list2=[]

for i in z: #list1 contain only  the unique elements of the z
    if i in list1:
        list2.append(i)
    else:
        list1.append(i)
print list1
#the following command convert the list1 elements into string
convert_string = "".join(str(x) for x in list1)
print convert_string
