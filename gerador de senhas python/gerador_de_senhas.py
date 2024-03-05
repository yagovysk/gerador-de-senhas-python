import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Digite o tamanho que você queira que a senha tenha: "))
    password = generate_password(password_length)
    print("Senha gerada:", password)
