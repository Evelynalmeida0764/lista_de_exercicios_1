ano = int(input("digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano e bissexto")
else:
    print("O ano não e bissexto")