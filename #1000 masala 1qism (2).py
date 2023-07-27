"""Shart operatori"""

# if1
# a=int(input())
# if a>=0:
#     print(a+1)
# else:
#     print(a)

# if2
# a=int(input())
# if a>=0:
#     print(a+1)
# else:
#     print(a-2)

# if3
# a=int(input())
# if a>0:
#     print(a+1)
# elif a==0:
#     print("10")
# else:
#     print(a-2)

# if4
# a,b,c=map(int,input().split())
# h=0
# if a>0:
#     h=+1
# if b>0:
#     h+=1
# if c>0:
#     h+=1
# print(h)

# if5
# list1=list(map(int,input().split()))
# musbat=0
# manfiy=0
# for g in list1:
#     if g>0:
#         musbat+=1
#     if g<0:
#         manfiy+=1
# print(manfiy, "manfiy")
# print(musbat, "musbat")

# if6
# a,b=map(int,input().split())
# if a>b:
#     print("Birinchi son katta")
# elif b>a:
#     print("Ikkinchi son katta")

# if7
# a,b=map(int,input().split())
# if a<b:
#     print("Birinchi son kichik")
# else:
#     print("Ikkinchi son kichik")

# if8
# a,b=map(int,input().split())
# if a>b:
#     print(a,b)
# else:
#     print(b,a)

# if9
# a,b=map(int,input().split())


# if10
# a,b=map(int,input().split())
# if  a!=b:
#     print(a+b)
# elif a==b:
#     print(0)

# if11
# a,b=map(int,input().split())
# if a!=b:
#     if a>b:
#         print(a)
#     else:
#         print(b)
# elif a==b:
#     print(0)

# if12
# a,b,c=map(int,input().split())
# if a>b>c:
#     print(c)
# elif a>c>b:
#     print(b)
# else:
#     print(a)

# if13
# a,b,c=map(int,input().split())
# if a>b>c or c>b>a:
#     print(b)
# elif a>c>b or b>c>a:
#     print(c)
# elif c>a>b or b>a>c:
#     print(a)

# if14
# a,b,c=map(int,input().split())
# if a>b>c:
#     print(a,c)
# elif a>c>b:
#     print(a,b)
# elif b>a>c:
#     print(b,c)
# elif b>c>a:
#     print(b,a)
# elif c>a>b:
#     print(c,b)
# else:
#     print(c,a)

# if15
# a,b,c=map(int,input().split())
# if a>b>c:
#     print(a+b)
# elif a>c>b:
#     print(a+c)
# elif b>a>c:
#     print(b+a)
# elif b>c>a:
#     print(b+c)
# elif c>a>b:
#     print(c+a)
# else:
#     print(c+b)

# if16
# a,b,c=map(int,input().split())
# if a<b<c:
#     print(2*a, 2*b, 2*c)
# else:
#     print("a>b>c")

# if17
# a,b,c=map(int,input().split())
# if a>b>c or c<b<a:
#     print(2*a, 2*b, 2*c)
# else:
#     print(-a, -b, -c)

# if18
# a,b,c=map(int,input().split())
# if a==b:
#     print("Uchinchisi qolgan ikkitasiga teng emas")
# elif a==c:
#     print("Ikkinchisi qolgan ikkitasiga teng emas")
# elif a!=b or a!=c or b!=c:
#     print("Bu sonlarning ikkitasi teng bo'lishi kerak")
# else:
#     print("Birinchi qolgan ikkitasiga teng emas")

# if19
# a,b,c,d=map(int,input().split())
# if a==b==c:
#     print("To'rtinchisi qolgan uchtasiga teng emas")
# elif a==b==d:
#     print("Uchinchisi qolgan uchtasiga teng emas")
# elif a==c==d:
#     print("Ikkinchi son qolgan uchtasiga teng emas")
# elif a!=b or a!=c or a!=d or b!=c or b!=d or c!=d:
#     print("Bu sonlarning uchtasi teng bo'lishi kerak")
# else:
#     print("Birinchi qolgan uchtasiga teng emas")

# if20
# a,b,c=map(int,input().split())
# if a>b>c:
#     print(a-b)
# elif a>c>b:
#     print(a-c)
# elif b>a>c:
#     print(b-a)
# elif b>c>a:
#     print(b-c)
# elif c>a>b:
#     print(c-a)
# else:
#     print(c-b)

# if21
# a=int(input())
# if a==0:
#     print("0")

# if21
# a=int(input())
# if 0<a<90:
#     print("Birinchi chorak")
# elif 90<a<180:
#     print("Ikkinchi chorak")
# elif 180<a<270:
#     print("Uchinchi chorak")
# else:
#     print("To'rtinchi chorak")

# if23



# if24
# from math import*
# x=int(input())
# if x>0:
#     print(2*math.sin(x))
# else:
#     print(x-6)

# if25
# from math import*
# x=int(input())
# if x<-2 or x>2:
#     print(2*x)
# else:
#     print(-3*x)

# if26
# from math import*
# x=int(input())
# if x<=0:
#     print(-x)
# elif 0<x<2:
#     print(x**2)
# elif x>=2:
#     print("4")

# if27
# x=int(input())
# if x<0:
#     print("0")
# else:
#     if x%2==0:
#         print(1)
#     else:
#         print(-1)

# if28
# x=int(input())
# if x%4 or x%400:
#     print(366*x)
# else:
#     print(365*x)

# if29
# m=int(input())
# if m>0:
#     if m%2==0:
#         print("Musbat juft son")
#     else:
#         print("Musbat toq son")
# else:
#     if m%2==0:
#         print("Manfiy juft son")
#     else:
#         print("Manfiy toq son")

# if30
# n=int(input())
# if 0<=n<=9:
#     if n%2==0:
#         print("Bir xonali juft son")
#     else:
#         print("Bir xonali toq son")
# elif 10<=n<=99:
#     if n%2==0:
#         print("Ikki xonali juft son")
#     else:
#         print("Ikki xonali toq son")
# elif 100<=n<=999:
#     if n%2==0:
#         print("Uch xonali juft son")
#     else:
#         print("Uch xonali toq son") 
# elif n<0:
#     print("Musbat son kiriting")
# else:
#     print("999 dan kichik son kiriting")


"""Mantiqi amallarga oid masalalar: (Boolean(True or False))"""

# Boolean1
# a=int(input())
# if a>0: 
#     print(True)
# else:
#     print(False)

# Boolean2
# a=int(input())
# if a%2!=0:
#     print(True)
# else:
#     print(False)

# Boolean3
# a=int(input())
# if a%2==0:
#     print(1)
# else:
#     print(0)

# Boolean4
# a,b=map(int,input().split())
# if a>2 and b<=3:
#     print(1)
# else:
#     print(0)

# Boolean5
# a,b=map(int,input().split())
# if a>=0 and b<-2:
#     print(1)
# else:
#     print(0)

# Boolean6
# a,b,c=map(int,input().split())
# if a>=b>=c:
#     print(1)
# else:
#     print(0)

# Boolean7
# a,b,c=map(int,input().split())
# if a>b>c or C<b<a:
#     print(1)
# else:
#     print(0)

# Boolean8
# a,b=int(input().split())
# if a%2!=0 and b%!=0:
#     print(1)
# else:
#     print(0)

# Boolean9
# a,b=map(int,input().split())
# if a%2!=0 or b%2==0:
#     print(1)
# else:
#     print(0)

# Boolean11
# a,b=map(int,input().split())
# if a%2==0 and b%2==0 or a%2!=0 and b%2!=0:
#     print(1)
# else:
#     print(0)

# Boolean12
# a,b,c=map(int,input().split())
# if a>0 and b>0 and c>0:
#     print(1)
# else:
#     print(0)

# Boolean13
# a,b,c=map(int,input().split())
# if a>0 or b>0 or c>0:
#     print(1)
# else:
#     print(0)

# Boolean14


# Boolean15
# a,b,c=map(int,input().split())
# if a>0 and b>0:
#     print(1)
# elif a>0 and c>0:
#     print(1)
# elif b>0 and c>0:
#     print(1)
# else:
#     print(0)

# Boolean16
# n=int(input())
# if 10<=n<=99 and n%2==0:
#     print(1)
# else:
#     print(0)

# Boolean17
# n=int(input())
# if 99<n<1000 and n%2!=0:
#     print(1)
# else:
#     print(0)

# Boolean18
# a,b,c=map(int,input().split())
# if a==b or a==c or b==c:
#     print(1)
# else:
#     print(0)

# Boolean19
# a,b,c=map(int,input().split())
# if a==-b or a==-c or b==-c:
#     print(1)
# else:
#     print(0) 

# Boolean20
# a=int(input())
# b=a//100
# c=(a%100)//10
# d=a%10
# if b!=c and b!=d and c!=d and 99<a<1000:
#     print(1)
# else:
#     print(0)

# Boolean21
# a=int(input())
# b=a//100
# c=(a%100)//10
# d=a%10
# if b<c<d or 99<a<1000:
#     print(1)
# else:
#     print(0)

# Boolean22
# a=int(input())
# b=a//100
# c=(a%100)//10
# d=a%10
# if b<c<d or b>c>d or 99<a<1000:
#     print(1)
# else:
#     print(0)

# Boolean23
# a=int(input())
# b=a//100
# c=(a%100)//10
# d=a%10
# if b==d:
#     print(1)
# else:
#     print(0)

# Boolean24
# a,b,c=map(int,input().split())
# d=b**2-4*a*c
# if d>=0:
#     if a<0:
#         print(0)
#     else:
#         print(1)

# else:
#     print(0)

# Boolean25
# x,y=map(int,input().split())
# if x<0 and y>0:
#     print(1)
# else:
#     print(0)

# Boolean26
# x,y=map(int,input().split())
# if x>0 and y<0:
#     print(1)
# else:
#     print(0)

# Boolean27
# x,y=map(int,input().split())
# if x<0 and y>0 or x<0 and y<0:
#     print(1)
# else:
#     print(0)

# Boolean28
# x,y=map(int,input().split())
# if x>0 and y>0 or x<0 and y<0:
#     print(1)
# else:
#     print(0)

# Boolean29
# x,y=map(int,input().split())
# if x>0 and y>0:
#     print("I chorak")
#     print("S = ", x*y)
# elif x<0 and y<0:
#     print("IV chorak ")
#     print("S = ", x*y)
# else:
#     print(0)

# Boolean30
# a,b,c=map(int,input().split())
# if a==b==c:
#     print(1)
# else:
#     print(0)

# Boolean31
# a,b,c=map(int,input().split())
# if a==b or b==c or a==c:
#     print(1)
# else:
#     print(0)

# Boolean32
# a,b,c=map(int,input().split())
# c=a**2+b**2
# b=a**2+c**2
# a=b**+c**2
# if a or b or c:
#     print(1)
# else:
#     print(0)

# Boolean33
# a,b,c=map(int,input().split())
# d=a+b
# e=a+c
# f=b+c
# if a>f or b>e or c>d:
#     print(1)
# else:
    # print(0)

# Boolean34 - Boolean40

"""Tanlash operatoriga oid masalalar (Case)"""
# Case1
# hafta=int(input())
# match hafta:
#     case 1:
#         print("Dushanba")
#     case 2:
#         print("Seshanba")
#     case 3:
#         print("Chorshanba")
#     case 4:
#         print("Payshanba")
#     case 5:
#         print("Juma")
#     case 6:
#         print("Shanba")
#     case 7:
#         print("Yakshanba")

# Case2
# k=int(input())
# match k:
#     case 1:
#         print("Yomon")
#     case 2:
#         print("Qoniqarsiz")
#     case 3:
#         print("Qoniqarli")
#     case 4:
#         print("Yaxshi")
#     case 5:
#         print("A'lo")
#     case other:
#         print("Xato")

# Case3
# k=int(input())
# match k:
#     case 1:
#         print("Qish")
#     case 2:
#         print("Qish")
#     case 3:
#         print("Bahor")
#     case 4:
#         print("Bahor")
#     case 5:
#         print("Bahor")
#     case 6:
#         print("Yoz")
#     case 7:
#         print("Yoz")
#     case 8:
#         print("Yoz")
#     case 9:
#         print("Kuz")
#     case 10:
#         print("Kuz")
#     case 11:
#         print("Kuz")
#     case 12:
#         print("Qish")

# Case4
# n=int(input())
# match n:
#     case 1:
#         print(31)
#     case 2:
#         print(28)
#     case 3:
#         print(31)
#     case 4:
#         print(30)
#     case 5:
#         print(31)
#     case 6:
#         print(30)
#     case 7:
#         print(31)
#     case 8:
#         print(31)
#     case 9:
#         print(30)
#     case 10:
#         print(31)
#     case 11:
#         print(30)
#     case 12:
#         print(31)

# Case5
# a,b=map(int,input().split())
# n=int(input())
# match n:
#     case 1:
#         print(a+b)
#     case 2:
#         print(a-b)
#     case 3:
#         print(a/b)
#     case 4:
#         print(a*b)

# Case6
# n=int(input())
# match n:
#     case 1:
#         print(1//10)
#     case 2:
#         print(2*1000)
#     case 3:
#         print(3)
#     case 4:
#         print(4/1000)
#     case 5:
#         print(5/100)

# Case7
# n=int(input())
# match n:
#     case 1:
#         print(1*1)
#     case 2:
#         print(2/1000000)
#     case 3:
#         print(3/1000)
#     case 4:
#         pritn(4/100)
#     case 5:
#         print(5/10)

# Case8
# oy=int(input())
# kun=int(input())

# match oy:
#     case 1:
#         if 0<kun<=31:
#             print(kun,"-", "Yanvar")
#         else:
#             print("Kun 0 dan katta 31 dan kichik bo'lishi kerak!")
#     case 2:
#         if kun%4!=0 and 0<kun<=29:
#             print(kun,"-", "Fevral (Kabsa yili)")
#         elif kun%4==0 and 0<kun<=29:
#             print(kun,"-", "Fevral")
#         else:
#             print("Kun 0 dan katta 29 dan kichik bo'lishi kerak!")
#     case 3:
#         if 0<kun<=31:
#             print(kun, "-" , "Mart")
#         else:
#             print("Kun 0 dan katta 31 dan kichik bo'lishi kerak!")
#     case 4:
#         if 0<kun<30:
#             print(kun, "-" , "Mart")
#         else:
#             print("Kun 0 dan katta 30 dan kichikbo'lishi kerak!")
#     case 5:
#         if 0<kun<31:
#             print(kun, "-" , "May")
#         else:
#             print("Kun 0 dan katta 31 dan kichikbo'lishi kerak!")
#     case 6:
#         if 0<kun<30:
#             print(kun, "-" , "Iyun")
#         else:
#             print("Kun 0 dan katta 30 dan kichik bo'lishi kerak!")
#     case 7:
#         if 0<kun<31:
#              print(kun,"-", "Iyul")
#         else:
#             print("Kun 0 dan katta 31 dan kichik bo'lishi kerak!")
#     case 8:
#         if 0<kun<31:
#             print(kun,"-", "Avgust")
#         else:
#             print("Kun 0 dan katta 31 dan kichik bo'lishi kerak!")
#     case 9:
#         if 0<kun<30:
#             print(kun, "-" , "Sentyabr")
#         else:
#             print("Kun 0 dan katta 30 dan kichik bo'lishi kerak!")
#     case 10:
#         if 0<kun<31:
#             print(kun, "-" , "Oktabr")
#         else:
#             print("Kun 0 dan katta 31 dan kichik bo'lishi kerak!")
#     case 11:
#         if 0<kun<30:
#             print(kun, "-" , "Noyabr")
#         else:
#             print("Kun  0 dan katta 30 dan kichik bo'lishi kerak!")
#     case 12:
#         if 0<kun<31:
#             print(kun, "-" , "Dekabr")
#         else:
#              print("Kun 0 dan katta 31 dan kichik bo'lishi kerak!")
# if oy<0 or oy>12:
#     print(oy, "- oy mavjud emas")

# Case9
# d=int(input())
# m=int(input())
# match m:
#     case 1:
#         if 0<d<=31:
#             print()

# Case10
qutb=input()
komanda=int(input())
match komanda:
    case 1:
        if qutb=="Shimol" and komanda==0:
            print("Robot Shimolga tomon harakatda davom etmoqda")
        if qutb=="Shimol" and komanda==1:
            print("Robot G'arga tomon harakat qilyapti") 
        else:
            print("Robot Sharqga tomon harakat qilmoqda")
    case 2:
        if qutb=="Janub" and komanda==0:
            print("Robot Janubga tomon harakatda davom etmoqda")
        if qutb=="Janub" and komanda==1:
            print("Robot Sharqga tomon harakat qilmoqda")
        else:
            print("Robot G'arbga tomon harakat qilmoqda")
    case 3:
        if qutb=="Sharq" and komanda==0:
            print("Robot Sharqga tomon harakatni davom ettirmoqda")
        if qutb=="Sharq" and komanda==1:
            print("Robot Shimolga tomon harakat qilmoqda")
        elif qutb=="Sharq" and komanda==2:
            print("Robot Janubga tomon harakat qilmoqda")
    case 4:
        if qutb=="G'arb" and komanda==0:
            print("Robot G'arbga tomon harakatni davom ettirmoqda")
        if qutb=="G'arb" and komanda==1:
            print("Robot Janubga tomon harakat qilmoqda")
        else:
            print("Robot Shimolga tomon harakat qilmoqda")
if komanda<0 or komanda>=3:
    print("Komanda 0-3 oraliqda bo'lishi kerak")
    
# Case12




































# Case20
# d=int(input("Tug'ulgan sanani kiriting: "))
# m=int(input("Tug'ulgan yilni kiriting: "))
# match m:
#     case 1:
#         if m==1 and 20<=d<=31 or m==2 and 1<=d<=18:
#             print("Qovg'a")
#         elif d>=31:
#             print("Bu sana mavjud emas")
#     case 2:
#         if m==2 and 19<=d<=29 or m==3 and 1<=d<=20:
#             print("Baliq")
#     case 3:
#         if m==3 and 21<=d<=31 or m==4 and 1<=d<=19:
#             print("Qo'y")
#     case 4: 
#         if m==4 and 20<=d<=30 or m==5 and 1<=d<=20:
#             print("Buzoq")
#     case 5:
#          if m==5 and 21<=d<=31 or m==6 and 1<=d<=20:
#             print("Egizaklar")
#     case 6:
#         if m==6 and 22<=d<=30 or m==7 and 1<=d<=22:
#             print("Qisqichbaqa")
#     case 7:
#         if m==7 and 23<=d<=31 or m==8 and 1<=d<=22:
#             print("Arslon")
#     case 8:
#         if m==8 and 23<=d<=31 or m==9 and 1<=d<=22:
#             print("Parizod")
#     case 9: 
#         if m==9 and 23<=d<=30 or m==10 and 1<=d<=22:
#             print("Tarozi")
#     case 10:
#          if m==10 and 23<=d<=31 or m==11 and 1<=d<=22:
#             print("Chayon")
#     case 11:
#         if m==11 and 23<=d<=30 or m==12 and 1<=d<=21:
#             print("O'qotar")
#     case 12:
#         if m==12 and 22<=d<=31 or m==1 and 1<=d<=19:
#             print("Echki")
# if m<0 or m>12 or d<0 or d>31:
#     print("Bu sana mavjud emas")
































































