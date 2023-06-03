# 3.ders
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
#! 2 Fonksiyonlarımız tek bir iş yapmalı ve sonucu bilinen bir türde dönmeli
# email_list=["a@b.com","b@c.com","c@d.com"]
# def Is_email_exist(email):
#     try:
#       result=email_list.index(email)
#       return True
#     except ValueError:
#        return False
#     # if result >=0:
#     #  return True
#     # return False

# def user_create(name,password,email):
#    user={"username":name,"password":password,"email":email}
#    return user
# def create_card(**kwargs):
#    return
  

# name=input("lütfen isminizi giriniz: ")
# password=input("lütfen şifrenizi giriniz: ")
# email=input("lütfen mail adresinizi giriniz: ")
# result=Is_email_exist(email)
# if result:
#    print("bu email adresi sistemde kayıtlıdır.")
# else:   
#   user=user_create(name,password,email)
# print(user)

# create_card(**user)
# try:
#    # işlem
# except ex:
#    print(ex)


# sayı1=int(input("lütfen bir sayı giriniz: "))
# sayı2=int(input("lütfen bir sayı giriniz: "))
# try:
#   sonuc=sayı1/sayı2
#   print(sonuc)
# except ZeroDivisionError:
#   print("herhangi bir sayı 0' a bölünemez")
# except NameError:
#   print("hatalı değişken")
# except ValueError:
#   print("lütfen sadece rakam giriniz")

# try:
#   sayı1=int(input("lütfen bir sayı giriniz: "))
#   sayı2=int(input("lütfen bir sayı giriniz: "))
#   sonuc=sayı1/sayı2
# except:  
#   print("something went wrong...")
 

#! Bir error üretmek
# sayı1=int(input("lütfen bir sayı giriniz: "))

# if not type(sayı1) is int:
#     raise TypeError("rakam girmeniz gerekir")

# import deneme
# sayı1=int(input("lütfen bir sayı giriniz: "))
# sayı2=int(input("lütfen bir sayı giriniz: "))
# operator=input("yapmak istediğiniz işlemi giriniz:")

# if operator=="+":
    #not--> import yaptığımız sayıfadaki fonksiyonlara ulaşıyoruz<---
#     print(deneme.Topla(sayı1,sayı2))
# elif operator=="-":
#     print(deneme.Cikar(sayı1,sayı2))
# elif operator=="/":
#     print(deneme.Bol(sayı1,sayı2))
# elif operator=="*":
#     print(deneme.Carp(sayı1,sayı2))
# else:
#     print("yanlış operator seçimi")

#not--> import yaptığımız sayıfadaki değişkene ulaşıyoruz<---
# print(deneme.hello)