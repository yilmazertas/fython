# a=10 # a burada integer tipinde bir değeişkendir
# print(type(a))
# a = 'ali diyor ki:"ben geç kalacağım"'# burada string tipindedir
# print(a)
# print(type(a))

# a= 10.0 #nokta kullanırsak float ,nokta kullnamasak integer olor
# print(type(a))

# a=True
# b= False  #boolyım
# print(type(a))

# a=[1,2,"ahmet",10.5,"mehmet","cengiz"] # a burda list tipindedir
# print(type(a))
# print(a[-1])

# a={"key":"value","ikinci":2} #dictionary 
# print(a["key"])
# print(type(a))


# a=("a","b","c") #tuple cok hızlı ama değişime kapalı
# print(type(a))


# a={"a","b","b","b" ,"c"}  #"set" setleri genel anlamda çok kullanılanılmıyor 
# print(a)

# a=10
# print(type(a))
# a=str(a)
# print(type(a))
# #int,str,float

# #dönüşümler
# a="10"
# a=int(a)
# print(type(a))

# a="10"
# a=float(a)
# print(type(a))
# print(a)


####STRİNG METHODS

# a="yilmaz"
# print(a.capitalize()) #string ifadesinn ilk harfini büyük harf yapar."Yilmaz"
# print(a)


# a="yilmaz"
# print(a.endswith("mz")) #string ifadelerin hangi harflerle bittiğini kontrol eder doğru ifade ediyorsa "true" yanlış ise "false" olur.
# print(a)



# a="yilmaz"
# print(a.find("v")) # parentez içersinde yazılan haarfin indexini dödürür .Eğer harf string içerisinde yoksa -1 şeklinde döndürür


# a="gamer65"
# print(a.isalnum()) #string ifadenin harf ve rakamlardan oluşup oluşmadığını kontrol eder.Eğer harf ve rakam dışında başka bir ifade varsa "false" döner 
# a="gamer65?.."
# print(a.isalnum())


# a="gamer65"
# print(a.isalpha()) #string ifadenin harflerden oluşup oluşmadığını kontrol eder eğer harflerden başka rakamlar varsa false döner
# a="gamer"
# print(a.isalnum())


# a="65651265"
# print(a.isdigit()) #string ifadenin rakamlardan oluşup oluşmadığını kontrol eder eğer rakamdan başka karaekter varsa false döner
# a="van651265"
# print(a.isdigit())

# a="AhMET" 
# print(a.lower()) # sting ifadeleri küçük harflere dönderir


# a="   umutcan   "
# print(a.strip()) #string ifadenin sağında ve solunda olan boşluk ifadelerini kaldırır."rstrip" sadece sağdaki boşlukları kaldırır ve "lstrip" ise sadece soldaki boşlukları siler.
# txt = "     banana     "

# x = txt.rstrip()

# print("of all fruits", x, "is my favorite")

# txt = "     banana     "

# x = txt.lstrip()

# print("of all fruits", x, "is my favorite")




# a="python dersine hoş geldiniz"
# b=a.split() #split boşluklardan bölerek bir dizi haline getirir
# print(b[2])
# print(type(b))


#####LİST METHODS#######
 
# a=[1,2,"ahmet",10.5,"cengiz"]
# a.append("eklenen veri")  #parentezin sonuna ekleme yapar
# print(a)

# a=[1,2,"ahmet",10.5,"cengiz"]

# a.append("eklenen veri") 
# a[1] ="yeni" #listenin belirtilen indexteki değerleri değiştirir
# print(a)


# a=[1,2,"ahmet",10.5,"cengiz"]
# b=a.copy() # listeyi copyalar
# print(b)

# a=[1,2,"ahmet",10.5,"cengiz"]
# a.insert(2,"son")#listenin belirtilen indexine,verilen değeri ekler."2" indexine "son" değeri ile değiştirmiştir 
# a.index(10.5)  #belirtilen verinin kaçıncı indexte olduğunu belirtir
# print(a.index(10.5))

# a.pop(1) #belirtilen indexteki değeri siler
# print(a)
# a.remove("ahmet") #belirtilen değeri listeden siler
# print(a)

# a=["zeynep","zeynep","ali","cengiz","ahmet"]
# a.sort() #listeyi alfabetik veya rakamları küçükten büyüğe doğru  sıralar
# a.reverse() #listeyi alfabetik veya rakamları tersten   sıralar sayıları büyükten küçüğe vaya alfabetik olarak sondan başa doğru srlar
# a.reverse()
# a.count("zeynep")#belirten değerin listede kaç defa geçtiği bilgisini döner
# a.clear()#listenin tüm elemanlarını siler
# print(a)
# b=[1,"m.yusuf",3]
# a.extend(b) #iki listeyi birbirine ekler
# print(a)

#########OPERATORS########
# operators=["+","-","/","*","//","%","**"]
# print(2+4)
# print(4-2)
# print(6/2) #burdan gelecek sonuç flout olur
# print(5//2)
# print(5%2)
# print(5 **2)

#######ARİTMATİK OPERATORS#####
# print(2*5/(3+2)/3) #işlemin içerisinde bölme işlemi olduğu için float sonuç döner

# a=2

# a+=5#a+=5
# a-=5#a=a-5
# a/=5#a=a/5
# a*=5#a=a*5
# a**=5#a üssü 5 deemktir

######COMPARISON_OPERATORS####
# ["==","!=","<=",">=","<",">"]
# a=5
# b=6
# print(a==b)
# print(a!=b)#a b ye esit değil mi
# print(a<=b)
# print(a>=b)
# print(a<b)
# print(a>b)


# logic_operators=["and","not","or"]
# a=5
# b=6
# print(a>2 and b>2)
# print("fadfafas" not in logic_operators)


# identy_operators=["is","is not"]
# print(a is b)
# print(a is not b)

#########TUPLE METHODS####
# a=("ali",25,12,"sezgin","umutcan",22,15,19,"ayşe")
# print(a[2])
# print(a[1:7:2])
# a=(0,1,2,3,4,5,6,7,8,9)
# print(a.count("ali"))
# print(a.index("ali"))
# print(a[0:-1:2]) #ç.ftsayları dönder
# print(a[1::2]) #[başla :bitiş(dahil değil):adım sayısı]

######### DİCTİONARY METHODS  ######
# a={"birinci":1,"ikinci":2,"üçüncü":3}

# cars = {
#     "car1":{
#     "year":1984,
#     "model":"ford"
   
#     },
#     "car2": {
#     "year":2000,
#     "model":"bmw",
#     "customer":{
#     "name":"John",
#     "address":"Germany"
#     }
#     }
#   }
# print(cars["car1"]["year"])
# print(cars["car2"]["customer"]["address"])
# cars["car1"]["color"]="red" #dictionary değişkenine yeni veri ekleme yöntemi
# print(cars)
# cars["car2"].pop("model") #dictionary den bir veriryi silme yöntemi
# print(cars)

# customers ={"customer1":"John", "customer2":"Sam","customer3":"Felix"}
#customers["customer4"]="safiye"
#print(customers)
#customers.pop("customer2")
#print(customers)
#print(customers.keys())
#print(customers.values())
#print(customers.get("customer1"))
#print(customers.items())
# customers.update({"customer5":"adams"})
# print(customers)


##########  SET METHODS  ####### 
# set1={"a","b","c","d","e","f","g","a","b","b"}
# set2={"a","b","c","d","e","t"}  
#print(set1-set2)  iki küme arasındaki farklı elemanlar
# print(set1.union(set2)) #iki kümenin bileşimni verir
# set2.remove("a")
# print(set2.difference(set1))
# print(set2)
