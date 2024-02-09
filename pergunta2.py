n = int(input("Digite um número"))
fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

aux = 0

#  Exibe a sequência de fibbonaci
# for i in range(0, len(fib)):
#     print(fib[i]);


for i in range(0, len(fib)):
    if fib[i] == n:
        aux =1;
        print("Seu número está na sequência")
        break

if aux == 0:
    print("Seu número não está na sequência")
