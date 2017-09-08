target_numbers=[]   #blank list for the target numbers between 700 to 1700
for x in range(700, 1700): #define a range between 700 to 1700
    if (x%5==0) and (x%2==0): #the target numbers must fill up this two conditions
        target_numbers.append(x) #add the obtained numbers to the list
print target_numbers
