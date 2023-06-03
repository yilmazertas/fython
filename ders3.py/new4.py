class Insan():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def yemek(self,saat,menu):
        print(f"{self.name} {saat}'te {menu} yiyecek")

class Calisan(Insan):
    def __init__(self,name,age,title,department,salary):
        self.title=title
        self.department=department
        self.salery=salary
        super().__init__(name,age)

    def mesai_saatleri(self,saat,gün):
        print(f"{self.name}  {gün}  {saat} çalışacaktır.")
    def izin(self,gün,ay):
        print(f"{self.name}  {ay}  {gün} izin yapacaktır.")
    

    def calis(self):
        print("çalışma")

class Insan_kaynakları(Calisan):

    def calis(self,saat):
        print(f"{self.name} işe başlamıştır.Bugün işe alınacak personel mülakatını yapacak olup {saat} çalışacaktır")

    def mulakat(self,name,type):   
        print(f"{self.name} {name} ile {type} mülakat yapacaktır.")


class Muhasebe(Calisan):

    def calis(self):
        print(f"{self.name} bugün fatura kesecektir.")

    def fatura_kes(self,name,amount,fatura_no): 
        print(f"{self.name} bugün {name} şirketine {fatura_no} nolu {amount} miktarı kadar ftura kesilecektir.  ")  
    def yemek(self,saat,menu):
        print(f"{self.name} {saat}'te {menu} yiyecek")

class Developer(Calisan):

    def calis(self):
        print(f"{self.name} bugün hataları düzeltecektir.")

    def kod_yaz(self,name,func): 
        print(f"{self.name} bugün {name} şirketi için {func} yazacaktır.  ")  

    def yemek(self):
        print(f"developer yemek yemek fokksiyonu...")

calışan1=Insan_kaynakları("ayşe",24 ,"insan kaynakları müdürü","insan kaynakları",1800)
calışan2=Muhasebe("fatma",34,"muhasebe müdürü","muhaseba",16000)
calışan3=Developer("zeynep",28,"software enginar","developer",25000)
# calışan1.calis(10)
# calışan2.calis()
# calışan3.calis()
# calışan3.kod_yaz("akbank","para gönder")
# calışan2.fatura_kes("iş bankası",40000,5433345)
# calışan1.mulakat("Aysel","teknik mülakat")
calışan3.yemek()
calışan2.yemek(12,"pizza")

class Araba():
    def hıızlan(self,hız):
        self.hız += hız

    def hıızlan(self,hız):
        self.hız -= hız

class wolskvagen(Araba):
    def airbag(self):
        print("airbag")


class Passat(wolskvagen):
    def sunroof(self):
        print("sunroof")

class Mercedes(Araba):

    pass

class Aseries(Mercedes):
    
    pass

class Cseries(Mercedes):
    
    pass
    
    
araba={
    "sunroof":"var",
    "gaz":"var"
 }   
