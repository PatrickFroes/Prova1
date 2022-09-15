import secrets
import string

letra = ()
escolha = ()
contador = 1

letra = secrets.choice(string.ascii_letters)

while contador <= 5:
    escolha = str(input("Escolha uma letra."))
    if escolha == letra:
        print("Parabens você acertou!!!")
        contador = 6
    elif contador<5:
        print("Tente novamente.")
    else:
        print("Você perdeu :(")
    contador = contador + 1