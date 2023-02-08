
from objectSample import Phone

phone_list=[]

phone1 = Phone("white",50,2,"realme",15000)

phone1.photography()

phone2 = Phone("black",100,1,"samsung",40000)

phone2.photography()

phone3 = Phone()

print('name of the phone 3 : '+phone3.name)

phone_list.append(phone1)
phone_list.append(phone2)

print('printing list')
