waves = int(input("Enter Frequency:"))
 
if waves < 3 * 10**9:
    print ("RadioWaves")
elif 3 * 10**9 < waves < 3 * 10**12:
    print(" Microwaves")
elif 3 * 10**12 < waves < 4.3 * 10**14:
    print("Infrared Light")
elif 4.3 * 10**14 < waves < 7.5 * 10**14:
    print('Visible Light')
elif 7.5 * 10**14 < waves < 3 * 10 **17:
    print("UtraViolet Rays")
elif 3 * 10 **17 < waves < 3 * 10**19:
    print("X-Rays")
elif waves > 3 * 10**19:
    print('Gamma Rays')
    