c=True
while c==True:
    try:
        ch=int(input("vedite naturalno 4islo  "))
        c = False
    except ValueError:
        print("4islo NE naturalnoe!!!")

st=str(ch)
print(st)
chet=0
nechet=0
chet_t=''
nechet_t=''
for i in range(len(st)):
    if int(st[i])%2==0:
        chet+=1
        chet_t=chet_t+st[i]
    else:
        nechet+=1
        nechet_t=nechet_t+st[i]
print('chet - ',chet, ' ito ',chet_t)
print('NEchet - ',nechet, ' ito ',nechet_t)


