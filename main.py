import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

def main():
    print('gerador de senhas seguras')
    try:
        tamanho = int(input('Informe o tamanho da senha: '))
        if tamanho < 4:
            print('O tamanho minimo da senha é 4.')
        else:
            senha = gerar_senha(tamanho)
            print(f'sua senha é: {senha}')
    except ValueError:
        print('Por favor, insira um número válido.')


if __name__ == "__main__":
    main()