a = int(input("Digite o valor do lado A do triângulo: "))
b = int(input("Digite o valor do lado B do triângulo: "))
c = int(input("Digite o valor do lado C do triângulo: "))

if a == b == c: 
    print("Esse triângulo é Equilátero!")
elif a != b and b != c and a != c:
    print("Esse triângulo é Escaleno!")
else:
    print("Esse triângulo é Isóceles!")