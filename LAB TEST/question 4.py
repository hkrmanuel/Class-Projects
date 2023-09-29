discount =  60/100
list1 =[4.95, 9.95, 14.95, 19.95 , 24.95]
list2 = []
list3 = []

for i in range(len(list1)):
    dis_result = list1[i] * discount
    dis_amount = list1[i] - dis_result
    list2.append(dis_result)
    list3.append(dis_amount)

print("Original Price  | Discount Amount  | New Price")

for s in range(len(list2)): 
    print("         ",list1[s], " |  " , round(list2[s], 2) , "          |  ", list3[s])