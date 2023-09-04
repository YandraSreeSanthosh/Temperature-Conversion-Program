Temperature=int(input("Enter the Temperature: "))
units=input("Enter the units of the temperature[Celsius/Kelvin/Fahrenheit]: ").lower()
f=(Temperature*9/5)+32
c=(f-32)*5/9
k=c+273.15
if units=="celsius":
    print("The temperature in Fahrenheit =",f)
    print("The temperature in Kelvin =",k)
elif units=='fahrenheit':
    print("The temperature in Celsius =",c)
    print("The temperature in Kelvin =",k)
elif units=="kelvin":
    k_c=k-273.15
    print("The temperature in Celsius =",k_c)
    k_f=(k-273.15)*9/5+32
    print("The temperature in Fahrenheit =",k_f)
else:
    print("Only Celsius/Fahrenheit/Kelvin units are accepted")