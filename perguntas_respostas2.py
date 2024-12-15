perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
# 1. Imprimir as "perguntas" do dicionário;
# 2. Imprimir as "opções" do dict c/ os "números" dos índices das opções (0, 1, 2 e 3);
# 3. Criar input; verificar se o número é dígito ; transformá-lo em inteiro;
# 4. Este input deve estar dentro das possibilidades (opções 0, 1, 2 ou 3); verificar se a resposta está correta (resposta/indice);
# 5. Informar(printar) se acertou/errou a pergunta ; armazena o total de acertos; comparar c/ total de perguntas no último print.

hd_acertos = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])

    for indice, valor in enumerate(pergunta['Opções']):
        print(f'{indice}) {valor}')
    print()

    entrada_int = None
    entrada = input('Digite um número: ')
    if entrada.isdigit() is True:
        entrada_int = int(entrada)

    acertou = False
    if entrada_int is not None:
        if entrada_int >= 0 and entrada_int < len(pergunta['Opções']):
            if pergunta['Opções'][entrada_int] == pergunta['Resposta']:
                acertou = True

        if acertou is True:
            hd_acertos += 1
            print('Acertou')
        else:
            print('Errou')

print(f'Você acertou {hd_acertos} de {len(perguntas)}.')


# Edson Copque | https://linktr.ee/edsoncopque
