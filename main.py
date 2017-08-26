'''
bin_data=['0000','0001','0010','0011','0100','0101','0110','0111','111']
choice=[i for i in range(4)]
print choice
user_data=[]
for i in choice:
    print i
    user_data.append(bin_data[i])
    print user_data
n_0=[]
n_1=[]
n_2=[]
n_3=[]
for i in range(len(user_data)):
    count=user_data[i].count('1')
    print count
    if count is 0:
        n_0.append(user_data[i])
    if count is 1:
        n_1.append(user_data[i])
    if count is 2:
        n_2.append(user_data[i])
    if count is 3:
        n_3.append(user_data[i])
print n_0,n_1,n_3,n_2
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

def combine_s1(x1,x2):  #for combining two minterms based on the no. ones present
     p=0

     while i <4 :
         if not (x1[i] = x2[i]) :
             similar_no
