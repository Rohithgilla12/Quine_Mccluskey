
bin_data=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1111']#Binary_data
list_len=int(input("enter no. of minterms"))
l=list_len-1
result=[]
choice=[] #userinput (like 1,4,5,6)
ll=0
while ll<=l :
    mn=int(input("enter your minterm"))
    choice.append(mn)
    ll=ll+1


user_binary_data=[] #list of user choosn terms converted to binary
user_decimal_data=[] #list of user choosn terms in decimal form

for i in choice:

    user_binary_data.append(bin_data[i])
    user_decimal_data.append(i)


# print user_binary_data
# print user_decimal_data



''' STEP-1 combining based on no. of ones present '''

n_0=[] #List of all 0 no.of '1'
n_d_0=[] #list of decimal no. with 0 no. of ones
n_1=[]#List of all 1 no.of '1'
n_d_1=[]
n_2=[]#List of all 2 no.of '1'
n_d_2=[]
n_3=[]#List of all 3 no.of '1'# print temp1
                    # print temp2
n_d_3=[]
n_4=[]
n_d_4=[]
for i in range(len(user_binary_data)): #This loops checks how many '1's are there in user inputted minterms like 1101 has 3 ones
    count=user_binary_data[i].count('1') #'1100'.count('1') returns u 2  i.e,no of repeted terms

    if count is 0:
        n_0.append(user_binary_data[i])
        n_d_0.append(user_decimal_data[i])
    if count is 1:
        n_1.append(user_binary_data[i])
        n_d_1.append(user_decimal_data[i])
    if count is 2:
        n_2.append(user_binary_data[i])
        n_d_2.append(user_decimal_data[i])
    if count is 3:
        n_3.append(user_binary_data[i])
        n_d_3.append(user_decimal_data[i])
    if count is 4:
        n_4.append(user_binary_data[i])
        n_d_4.append(user_decimal_data[i])

# print n_0,n_1,n_2,n_3,n_4 #just for debugging
# print n_d_0,n_d_1,n_d_2,n_d_3,n_d_4 #just for debugging


''' STEP-2 groping based on one diff term  '''

def combine_s2(x1,x2):  #x1,x2 are binary terms from lists n_0 etc
        cou=0
        x1l=list(x1)
        x2l=list(x2)
        for i in range(0,4):
             if not (x1l[i]==x2l[i]):
                 cou =cou+1
                 pos=i    #positio where the difference is , thiscan be dashed eg;0_11


        if (cou==1):
              return [True,pos]
        else :

            return [False,None]
implicants=[]
#Add a try block if n_1 has no elements it gives out a error

# print'----------------For lists n_0,n_1 -------------------'
if(len (n_0)>=1 and len(n_1)>=1):
        for i1 in n_0: #For each element in n_1

            for i2 in n_1: #Comparing with each element in n_2
                temp=combine_s2(i1,i2)
                if temp[0] is True:
                    temp1=i1
                    temp2=i2
                    i1=list(i1)
                    i1[temp[1]]='_' #Postion to be daashed

                    # print temp1
                    # print temp2
                    implicants.append([bin_data.index(temp1),bin_data.index(temp2),''.join(i1)])
# print '-----------------For lists n_1,n_2 -------------------'

if(len(n_1)>=1 and len(n_2)>=1):
        for i1 in n_1: #For each element in n_1
            for i2 in n_2: #Comparing with each element in n_2
                temp=combine_s2(i1,i2)
                if temp[0] is True:
                    temp1=i1
                    temp2=i2
                    i1=list(i1)
                    i1[temp[1]]='_' #Postion to be daashed

                    # print temp1
                    # print temp2
                    implicants.append([bin_data.index(temp1),bin_data.index(temp2),''.join(i1)])
# print'-----------------For lists n_2,n_3 -------------------'

if(len(n_2)>=1 and len(n_3)>=1):
        for i1 in n_2: #For each element in n_ 1
            for i2 in n_3: #Comparing with each element in n_2
                temp=combine_s2(i1,i2)
                if temp[0] is True:
                    temp1=i1
                    temp2=i2
                    i1=list(i1)
                    i1[temp[1]]='_' #Postion to be daashed

                    # print temp1
                    # print temp2
                    implicants.append([bin_data.index(temp1),bin_data.index(temp2),''.join(i1)])

# print'-----------------For lists n_3,n_4 -------------------'

if(len(n_3)>=1 and len(n_4)>=1):
        for i1 in n_3: #For each element in n_1
            for i2 in n_4: #Comparing with each element in n_2
                temp=combine_s2(i1,i2)
                if temp[0] is True:
                    temp1=i1
                    temp2=i2
                    i1=list(i1)
                    i1[temp[1]]='_' #Postion to be daashed

                    # print temp1
                    # print temp2
                    implicants.append([bin_data.index(temp1),bin_data.index(temp2),''.join(i1)])

print implicants
rpi=[] #list that store no. that are not present in implicants

x=0
while x < 15 :
    c=0

    y=0
    while y <= len(implicants)-1:



        for z in range(0,len(implicants[y])-1):
            # print len(implicants)-1
            # print z
            # print x
            if x==implicants[y][z]:
                c=True
        y=y+1
    if c==True :
        ja="do nothing"
    else :
        # print x
        rpi.append(x)
    x=x+1

# print rpi
kpi=[] #list that stores inputted minterms that are not present in implicants
for x in rpi:
    for y in user_decimal_data:
        if x==y:
            # print x
            kpi.append(x)
e_prime_implicants=[]
for x in kpi:
    e_prime_implicants.append([x,bin_data[x]])
print e_prime_implicants

''' function for convrting binary numbers to texts '''
def bin_to_text_convert(s) : #s ia string containing 4 characters eg: '10_1'
       sc=["l","l","l","l"]
       sl=list(s)

       i=0
       while i<4:

           if i==0:
               if sl[i]=="1":
                   sc[i]="A"
               if sl[i]=="0":
                   sc[i]="A'"
               if sl[i]=="_":
                   sc[i]=""
           if i==1:
               if sl[i]=="1":
                   sc[i]="B"
               if sl[i]=="0":
                   sc[i]="B'"
               if sl[i]=="_":
                   sc[i]=""
           if i==2:
               if sl[i]=="1":
                   sc[i]="C"
               if sl[i]=="0":
                   sc[i]="C'"
               if sl[i]=="_" :
                   sc[i]=""
           if i==3:
               if sl[i]=="1":
                   sc[i]="D"
               if sl[i]=="0":
                   sc[i]="D'"
               if sl[i]=="_":
                   sc[i]=""
           i=i+1
       return "".join(sc)
for i in e_prime_implicants:
    result.append(bin_to_text_convert(i))
print result
some_list=[] #IDK the list name
for i in range(len(implicants)-1):
        temp=combine_s2(implicants[i][2],implicants[i+1][2])
        if temp[0] is True:
             k=implicants[i][2]
             k=list(k)
             k[temp[1]]='_'
             some_list.append(''.join(k))

#this above function works perfectly alright do not make any changes

# d="1_01"
# print bin_to_text_convert(d)



####----------Read this---------------------
#if a list is l=[1,2,3,4,5] we can get index value by using this l.index('2') gives 3 as answer i used that concept


# ''' rohith plz add code here such that x1 is selected from n_x and x2 is selected from n_x+1,and should cover all sets'''
#
# '''next step , using above function we should group based on one diff and dash the pos (10_1) '''
#
#
#
# '''
# #i did not understand your code check this version for converting minterms into binary strings
# def decimal_to_binary_converter(x) : # function for coverting decimal numbers into binary numbers
#     if x==0 :
#         return "0000"
#     if x==1 :
#         return "0001"
#     if x==2 :
#         return "0010"
#     if x==3 :
#         return "0011"
#     if x==4 :
#         return "0100"
#     if x==5 :
#         return "0101"
#     if x==6 :
#         return "0110"
#     if x==7 :
#         return "0111"
#
#
# list_len=int(input('enter the no. of minterms'))
# l=list_len-1 #first element of a list always has 0 assigned to it
# kk=0 #just a looping variable
# binary_terms=[] #list that stores the binary forms of inputted minterms
# minterms_decimal=[] #list that stores cooresponding decimals
# while (kk<=l):
#     k=int(input("enter  minterm"))
#     minterms_decimal.append(k)
#     kb=decimal_to_binary_converter(k) #decimal to binary converter
#     binary_terms.append(kb)
#     kk=kk+1
# print binary_terms
#
# # step 1 : grouping terms with same number of ones
#
# no_of_ones=[]
#
# for b in binary_terms:
#     bb=list(b) # bb is a list of digits if a binary number b eg: if b="0100" ,bb= [0,1,0,0]
#     ss=0
#     count=0
#     while ss<4 :
#         j= bb[ss]
#         if j=="1":
#             count=count+1
#         ss=ss+1
#
#     no_of_ones.append(count)
# print no_of_ones
# '''
