# if "şart1":
#   print()
#   #1.satır
#   #2.satır
#   #3.satır
#     #şart oloşura yazılacak kodlar
# elif "şart2":
#    print()
#     #şart oluşura yapılacak kodlar
# else:
#     print()
#     #şart oluşura yapılacak kodlar
#  #burada if dışına çıktık


#iç içe if
# if "şart 1":
#    print()
#    # kodlar
#    if "şart 2":
#       print()
#       #kodlar

   
# a=40
# b=30
# if a>b:
#     print("a b' den büyüktür")
#     print("if çalıştı")
# elif a<b:
#     print("a b'den küçüktür")
#     print("elif çalıştı")
#     #devem eden codlar
# else:
#      print("a b'ye eşittir")
#      print("else çalıştı") 
# print("if şartı bitti...")
  
#kullanıcıdan aldığımız iki sayıyı karşılaştıran kodlar
# a=int(input("birinci sayıyı girniz: "))
# b=int(input("ikinci sayıyı girniz: "))
 
# if a>b:
#    print("birinci girdiğiniz sayı daha büyüktür")
# elif a<b:
#    print("ikinci girdiğiniz daha büyüktür")
# else:
#    print("girdiğiniz sayılar birbirine eşittir")    

 #kullanıcıdan aldığımız sayının pozitif negatif kontrol karşılaştırması  

# sayı = int(input("bir sayı giriniz:"))

# if sayı>0:
#    print("sayı pozitiftir")

# elif sayı<0:
#    print("sayı negatiftir")  

# else:
#    print("sayı sıfırdır")   


#kullanıcıdan password alıp içerisinde harf ve rakam birlikte kullanmış olarak kontrol edeleim

# password =input("Lütfen şifrenizi giriniz : ")

# if password.isalnum():
#     print("şifreniz geçerli")
# else:
#     print("lütfen şifrenizin içerisinde harf ve rakam kullanınız")   


# tiyatro bileti alirken bilet fiyatı yaşa göre değişmektedir.Yaşı 18'de küçük olanlar için bilet ücreti
#15 TL;yaşı 18'den büyük ve 65'ten küçük olanlar için 20 TL ve yaşı 65'ten büyük olanlar için 10TL olarak belirtilmiştir.Bu durumda tiyatro seyircilerinin yaşlarına göre bilet almalarına olanak sağlayan programın Python kodunu oluşturunuz.

# yas=int(input("lütfen yaşınızı giriniz: "))
# bilet=0

# if yas<=18:
#     bilet=15
# elif yas>18 and yas<65:
#     bilet=20 
# else:
#     bilet=10   

# print("bilet fiyatınız:",bilet)   


#Kullanıcıya Almanca ya da İngilizce ve ofis programları bilip bilmediğini soran,Almanca yada ingilizcede  birini biliyorsa ve ofis programları biliyorsa "işe başlayabilirsiniz",değilse "üzgünüz" mesajı veren Python kodunu yazınız

# ingilizce=input("ingilizce biliyor musunuz[E/H]:")
# almanca=input("almanca biliyor musunuz[E/H]:")
# ofis=input("ofis biliyor musunuz[E/H]:")

# if (almanca.upper() == "E" or ingilizce.upper() == "E") and ofis.upper() == "E":
#     print("işe başlayabilirsiniz")
# else:
#     print("üzgünüm")    


############# FOR LOOPS  ###########

# liste = ["elma", "armut","ayva","badem","ceviz","fıstık"]
#  # for iterasyonunda itere ettiği nesnenin içerisindeki elemanları itere eder
# for i in liste:
#     if i== "badem":
#       print(f"{i} fiyatı 200TL dir")
#     elif i== "fıstık":
#        print(f"{i} fiyatı 100TL dir")  

# eğer int değer döndürmek istiyorsak range() fonksiyonu kullanılır.
# 0 dan başlar yazılan rakama kadar döner (yazılan rakam dahil değil).
# for i in range(5):
#    print(i)     
#  
# for i in range(len(liste)):
#    print(i)      
#    print(liste[i])      


# for i in range(5,10):
#    print(i)      

# for i in range(5,20,3):
#    print(i)      
      

# 1den 20 ye kadar olan çift sayıları yazdıran kod
# *1.yöntem
# for i in range(0,20):
#     if (i % 2 == 0):
#         print(i)
# # 2. yöntem  

# for i in range(0,20,2):
#     print(i)       

#? break, continue
#break=bu keyword döngüyü bitirir
#contune=döngüde işlem yapmadan atlama keywordu

# for  i in range(5,10):
#     if (i % 2 ==1):
#         continue
#     print(i) 
#     print("çift sayı")

# for  i in range(5,100):
#     print(i)
#     if i  ==20:
#         break
#     print("break çalıştı") 

# kullanıcıdan alınan 5 sayının toplamını bulan python kodu:
# toplam=0
# for i in range(5):
#     sayı=int(input("bir sayı giriniz: "))
#     toplam +=sayı
# print(toplam)    



# 5 den  kullanıcının girdiği sayıya kadar (girilen sayı dahil) olan çift sayıların toplamı bulan python kodu yazınız
# sayı=int(input("bir sayı giriniz: "))
# toplam=0
# for  i in range(5,sayı+1):
    
#     if i % 2== 0:
#        toplam+=i
# print(toplam)      

# liste=["ayşe","fatma","hakan", "mustafa" ,"sencer"]
# for i in liste:
#     print(f"my name is {i}")   


#dictionary verileri
# mydictionary={"name1":"ayşe","name2":"fatma","name3":"hakan", "name4":"mustafa" ,"name5":"sencer"}
# for i in mydictionary.keys():
#     print(f"mydictionary key is {i}" )    
# for i in mydictionary.values():
#     print( "mydictionary value is {1}{0}".format(i,"yeni"))    


#kulanıcının girdiği 6 adet sayıdan tekler sayıları ve çift sayıları toplayıp teker teker ekranda gösteren python kodu
# tek_toplam=0
# çift_toplam=0
# for i in range(6):
#     sayı=int(input("bir sayı giriniz : "))
#     if sayı % 2==1:
#         tek_toplam+=sayı
#     else:
#         çift_toplam +=sayı    
# print(f"tek sayıların toplamı : {tek_toplam}")
# print("çift sayıların toplamı : {}".format(çift_toplam))

#! ########## FUNCTİONS  ##########
# def tek_bul(liste):
#     new_list=[]
#     for i in liste:
#         if i % 2 == 1:
#             new_list.append(i)
#     return new_list
# my_list=[2,5,6,4,13,21,22,77,88,83,97,7,61]
# tekler= tek_bul(my_list)
# print(tekler)


# def çift_bul(liste):
#     new_list=[]
#     for i in liste:
#         if i % 2 == 0:
#             new_list.append(i)
#     return new_list
# my_list=[2,5,6,4,13,21,22,77,88]
# çiftler=çift_bul(my_list)
# print(çiftler)


# def üçünkatı_bul(liste):
#     new_list=[]
#     for i in liste:
#         if i % 3 == 0:
#             new_list.append(i)
#     return new_list
# my_list=[2,5,6,4,13,21,22,77,88,87,90,93]
# üçünkatı=üçünkatı_bul(my_list)
# print(üçünkatı)


# # # Lambda function 
# my_list=[2,5,6,4,13,21,22,77,88]
# çiftler= (lambda x: x % 2==0,my_list)
# print(çiftler)

#?  filter,map
# my_list=[2,5,6,4,13,21,22,77,88]
# çiftler= list(filter(lambda x: x % 2==0,my_list))
# print(çiftler)
# katlar= list(map(lambda x: x * 2+3,my_list))
# print(katlar)

##### taş-kağıt-makas oyunu
# import random
# def oyna(secim1,secim2):
#     if secim1=="kağıt" and secim2== "taş":
#         return secim1
#     elif secim1 == "kağıt" and secim2 == "makas":
#         return secim2
#     elif secim1 == "makas"   and secim2 == "kağıt" :
#         return secim1
#     elif secim1 == "makas"   and secim2 == "taş" :
#         return secim2
#     elif secim1 == "taş" and secim2=="makas":
#         return secim1
#     elif secim1 == "taş" and secim2=="kağıt":
#         return secim2
#     elif (secim1== "taş" and secim2== "taş") or (secim1== "kağıt" and secim2== "kağıt") or(secim1== "makas" and secim2== "makas"):
#         return "beraberlik"
   
# # random.randint(100)
# # random.choice(my_list)

# game_list=["taş","kağıt","makas"]
# bilg_secim=random.choice(game_list)
# benim_secim=input("taş-kağıt-makas: ")

# kazanan=oyna(bilg_secim,benim_secim)
# print(f"bilgisayar secimi :{bilg_secim}")
# print(f"kazanan secim :{kazanan}")



#Kullanıcıdan üç kenar uzunluğunu alın ve kenar uzunluklarıyla oluşturulan üçgen türünü belirleyin.Eğer üçgen bir eşkenar üçgen ise"Eşkenar üçgen" ,eğer üçgen ikizkenar üçgen ise "ikizkenar üçgen", diğer durumlarda ise "Çeşitkenar üçgen" diye python kodunu yazalım 


# kenar1=int(input("birinci kenarı giriniz: "))
# kenar2=int(input("ikinci kenarı giriniz: "))
# kenar3=int(input("üçüncü kenarı giriniz: "))
# kenar4=int(input("dördüncü kenarı giriniz: "))

# def bul(kenar1,kenar2,kenar3,kenar4=0):
#     print(kenar4)
#     if kenar1==kenar2 and kenar1==kenar3:
#         return "eşkenar "
#     elif  kenar1==kenar2:
#         return "ikizkenar "
#     else:
#         return "çeşitkenar "
    

# sonuç  =bul(kenar1,kenar2,kenar3,kenar4) 
# print(f"üçgen {sonuç} üçgendir") 


#3.ders
# def fonksiyon(*args):
#     if len(args)==3:
#         print("üçgen")
#     elif len(args) ==4:
#         print("dörtgen")   
#         if args[0] ==args[1]==args[3]:
#             print("kare")
#     elif args[0] ==args[1]  and args[2]==args[3]:
#         print("dikdörtgen")      
#     return
# fonksiyon(12,12,13,13)

# def fonksiyon(**param):
#     return

# my_dictionary={"bir":1,"iki":2}
# fonksiyon(**my_dictionary)


#1 fonksiyon ve değişken isimleri yaptıkları işle ilgili olarak isimlendirmeli.Başka developerler isimlendirmeyi okuduğunda fonksiyonun ya da değişkenin ne iş yaptığın anlayabilmeli
email_list=["a@b.com","b@c.com","c@d.com"]
def user_create(*params):
    result=email_list.index(email):
    if result >=0:

    return

name=input("lütfen isminizi giriniz: ")
password=input("lütfen şifrenizi giriniz: ")
email=input("lütfen mail adresinizi giriniz: ")
user=user_create(name,password,email)
create_