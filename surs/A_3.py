st=input("stroka 4erez probel  ").split()
print(st) # начальная строка
n=len(st)
w=0
for i in range(n):
    ob= False
    for j in range(n-i-1):#  убрали последний эдемент он уже на месте
        # ускаренее за счет того что не проходит последний элемент после прохождения по i
        if ((int(st[j])) > (int(st[j+1]))):
           # a=st[j]
           # st[j]=st[j+1]
            #st[j + 1]= a
            st[j],st[j+1] = st[j+1],st[j]
            ob= True
        print(i, " ", j, " ", st)
        w+=1
    if ob is False:
        break
print(st)# отсартированная строка
print(w)# количество проходов