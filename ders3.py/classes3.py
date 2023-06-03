# class Insan():
#     def __init__(self,age,height):
#         self.age=age
#         self.height=height
#     def yemek(self):
#         print("yemek yenildi.")

#     def uyumak(self):
#         print("uyumak")


# class Calisan(Insan):
#     def calıs(self):
#         print("mesai başladı")
#     def mola(self):
#         print("mola")
#     def sigara(self):
#         print("sigara")


# class Doktor(Calisan):
#     def __init__(self, age, height,title,category):
#         super().__init__(age, height)
#         self.category=category
#         self.title=title
        
#     def calıs(self,saat,gün):
#         print(f"{saat} {gün}")
#         print(self.yemek)
#     pass


# doktor1=Doktor(36,186,"doçent","KBB")
# print(doktor1.height )       
# print(doktor1.age )     
# print(doktor1.title )     
# doktor1.calıs(20,"salı")    


# doktor1= Doktor()
# doktor1.calıs("2","salı")
# doktor1.yemek()


# insan1=Insan()    
# calisan1=Calisan()
# calisan1. 





# class Insan():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def yemek(self,saat,menu):
#         print(f"{self.name} {saat}'te {menu} yiyecek")

# class Calisan(Insan):
#     def __init__(self,name,age,title,department,salary):
#         self.title=title
#         self.department=department
#         self.salery=salary
#         super().__init__(name,age)

#     def mesai_saatleri(self,saat,gün):
#         print(f"{self.name}  {gün}  {saat} çalışacaktır.")
#     def izin(self,gün,ay):
#         print(f"{self.name}  {ay}  {gün} izin yapacaktır.")

# Calisan1=Calisan("ahmet",22,"officer","account",12000)  
# Calisan1.yemek(12,"tavuk")
# Calisan1.mesai_saatleri(8,"Çarşamba") 
# Calisan1.izin(10,"Haziran")     