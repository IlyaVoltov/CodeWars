# put your python code here Вид треугольника
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
elif a == b != c:
    print("Равнобедренный")
elif a != b == c:
    print("Равнобедренный")
elif a == c != b:
    print("Равнобедренный")
else:
    print("Разносторонний")
