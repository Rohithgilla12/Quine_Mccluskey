'''
bin_data=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011',1100,1101,1111]#Binary_data
choice=[] #userinput (like 1,4,5,6)
print choice #for debugging
user_data=[] #list of user choosn terms converted to binary
for i in choice:
    print i
    user_data.append(bin_data[i])
    print user_data
n_0=[] #List of all 0 no.of '1' 
n_1=[]#List of all 1 no.of '1' 
n_2=[]#List of all 2 no.of '1' 
n_3=[]#List of all 3 no.of '1' 
for i in range(len(user_data)): #This loops checks how many '1's are there in user inputted minterms like 1101 has 3 ones
    count=user_data[i].count('1') #'1100'.count('1') returns u 2  i.e,no of repeted terms
    print count
    if count is 0:
        n_0.append(user_data[i])
    if count is 1:
        n_1.append(user_data[i])
    if count is 2:
        n_2.append(user_data[i])
    if count is 3:
        n_3.append(user_data[i])
print n_0,n_1,n_3,n_2 #just for debugging
'''
#i did not understand your code check this version for converting minterms into binary strings
def decimal_to_binary_converter(x) : # function for coverting decimal numbers into binary numbers
    if x==0 :
        return "0000"
    if x==1 :
        return "0001"
    if x==2 :
        return "0010"
    if x==3 :
        return "0011"
    if x==4 :
        return "0100"
    if x==5 :
        return "0101"
    if x==6 :
        return "0110"
    if x==7 :
        return "0111"


list_len=int(input('enter the no. of minterms'))
l=list_len-1 #first element of a list always has 0 assigned to it
kk=0 #just a looping variable
binary_terms=[] #list that stores the binary forms of inputted minterms
minterms_decimal=[] #list that stores cooresponding decimals
while (kk<=l):
    k=int(input("enter  minterm"))
    minterms_decimal.append(k)
    kb=decimal_to_binary_converter(k) #decimal to binary converter
    binary_terms.append(kb)
    kk=kk+1
print binary_terms

# step 1 : grouping terms with same number of ones

no_of_ones=[]

for b in binary_terms:
    bb=list(b) # bb is a list of digits if a binary number b eg: if b="0100" ,bb= [0,1,0,0]
    ss=0
    count=0
    while ss<4 :
        j= bb[ss]
        if j=="1":
            count=count+1
        ss=ss+1

    no_of_ones.append(count)
print no_of_ones
