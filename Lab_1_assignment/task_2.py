import string # import the string module
set_alphabet = set(string.ascii_lowercase)#define the set of lowercase letters
first_string = 'They all people quickly visited this wonderfull BGJXM zoo' #check one string
print(set(first_string.lower()) >= set_alphabet)#check the letters of string either equal to set of lower case alphabets or not
#if they are same then the boolean output will be true otherwise it is false
second_string = 'They all people quickly visited this wonderfull BGJX zoo' #check another string
print(set(second_string.lower()) >= set_alphabet)