bin_data=['0000','0001','0010','0011','0100','0101','0110','0111','111']
choice=[i for i in range(4)]
user_data=[]
for i in choice:
    user_data.append(bin_data[i])
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
