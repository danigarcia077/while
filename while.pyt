x=1
sumNum=0
promedio=0
limCicWhi=int(input("digite el numero"))
while x <= limCicWhi:
    print(x)
    sumNum=sumNum+x
    x=x+1
    promedio=sumNum/limCicWhi
    print("llevo sumados:", sumNum)
    print("La suma total es:", sumNum)
    print("El promedio es:", promedio)
    