m = 50
tm = 50
price = 15
adm = 0.25
adtm = 0.15
adcharg = 0.44
total = 0
tax = 0.05

texts= int(input("Enter Number Of Texts:"))
minutes= int(input("Enter Number Of Minutes:"))

if texts <= tm  and minutes <= m:
    base_charge = price + adcharg 
    total = round(base_charge +((price + adcharg)* tax), 2)
    print(f"Base charge : {base_charge}\n  Tax: {tax} \n 911 fee: {adcharg} \n Total Bill Amount: {total}")
    
elif texts > tm and minutes > m:
    addminutes = minutes - m
    costmin = addminutes * adm
    addtexts = texts - tm
    costtxt = addtexts * adtm
    base_charge = price + costtxt + costmin + adcharg
    total = round(base_charge +((price + costtxt + costmin + adcharg)* tax), 2)
    print(f" Base Charge :{base_charge} \n Additional Text charge:{costtxt} \n Additional Minutes Charge: {costmin} \n Tax: {tax} \n 911 fee: {adcharg} \n Total Bill Amount: {total}")
