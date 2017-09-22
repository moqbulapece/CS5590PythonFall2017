def main():#create a function
    input_number= input("Sample input: ")#the target number
    d = {}#dictionary which contain the square value of each numner
    for x in range(1,input_number+1):#square the each value of the range and put
        #in the dictionary in K:K*K fromat here it start from 1 and finish to the pique
        #value of the range
        d[x] = x ** 2
    print(d)

main()