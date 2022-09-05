# put your python code here
m = float(input())
h = float(input())
imt = m/(h*h)
if 25 >= imt >= 18.5:
    print("Оптимальная масса")
elif imt < 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")



