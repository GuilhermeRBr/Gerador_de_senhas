import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

def main():
    print('GERADOR DE SENHAS')
    while True:
        try:
            tamanho = int(input('Informe o tamanho da senha (Minimo de 8 digitos): '))
            if tamanho < 8:
                print('O tamanho minimo da senha é 8. TENTE NOVAMENTE...')
            else:
                senha = gerar_senha(tamanho)
                print(f'Sua senha é: {senha}')
                nova = str(input('Deseja gerar nova senha? [S/N]: '))
                if nova in 'Ss':
                     pass
                elif nova in 'Nn':
                    print('Obrigado por usar o gerador...')
                    break
        except ValueError:
            print('Por favor, insira um número válido. TENTE NOVAMENTE...')


if __name__ == "__main__":
    main()