nome = input ("qual seu nome? ")
disciplina = input("qual a materia? ")
n1 = int(input("qual a primeira nota? "))
n2 = int(input("qual a segunda nota? "))
n3 = int(input("qual a terceira nota? "))

soma = n1 + n2 + n3;
media = soma / 3;

print(f"sua media è:{media:.2f}")

if media >= 6 :
  print("parabens voce foi aprovado!!!")
else: 
  print("que pena rapaz, voce foi reprovado")

print(f"teu nome: {nome}")
print("tua disciplina:" ,disciplina)
print("sua primeira nota" ,n1)
print("sua segunda nota:" ,n2)
print("sua terceira nota:" ,n3)
print("o valor da soma:" ,soma)
print(f"sua media:{media:.2f}")