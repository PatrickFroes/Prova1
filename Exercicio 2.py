idade = ()
tempo = ()

idade = float(input("digite sua idade"))
tempo = float(input("digite o seu tempo de serviço"))

if idade >= 65:
    print("Você já pode se aposentar.")
elif idade >= 60 and tempo>= 25:
    print("Você já pode se aposentar.")
elif tempo >= 30:
    print("Você já pode se aposentar.")
else:
    print("Voê ainda não pode se aposentar")
