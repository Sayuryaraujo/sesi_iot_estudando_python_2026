a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Os lados devem ser positivos")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Os lados não formam um triângulo")
elif a == b and b == c:
    print("Triângulo equilátero")
elif a == b or a == c or b == c:
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")
