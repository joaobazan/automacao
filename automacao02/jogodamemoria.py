from random import randint
DEBUG = False
TENTATIVAS = 6
TOTAL_RODADAS = TENTATIVAS - 1
PONTUACAO_MAXIMA = 100
MENSAGENS = {
    'DEFAULT': {
        'SAUDACAO': 'Escolhi um número entre 0 a 10. Tente adivinhar',
        'VITORIA': 'Parabéns!! Você acertou',
        'DERROTA': 'Que pena!! Você não acertou',
        'INPUT_JOG': 'Digite um número entre 0 e 10: ',
        'NOVA_PARTIDA': 'Gostaria de jogar novamente? (1-Sim; 2:Não)',
        'ENCERRAMENTO': 'Até a próxima!',
        'PONTUACAO': lambda pontuacao: f'Sua pontuação final é {pontuacao} pontos'
    }
}

def mensagem_tela(mnsagem, pontuacao=None, mensagem_result=None):
    TAMANHO_LINHA = 70
    ALINHAMENTO = F'^{TAMANHO_LINHA}'
    print(f'{"-" * TAMANHO_LINHA}')
    print(f'{mensagem.upper():{ALINHAMENTO}}')
    if pontuacao is not None:
        print(f'{mensagem_result.upper():{ALINHAMENTO}}')
    print(f'{"-" * TAMANHO_LINHA}')
    
def get_input_jog(mensagem):
    return str(input(mensagem))

def valida_tentativa_jog(numero):
    try:
        int(numero)
    except ValueError:
        return False
    return int(numero) in range(11)

def valida_opcao_jog(input):
    try:
        int(input)
    except ValueError:
        return False
    return int(input) in range(3)

def nova_partida(input):
    # 1 - Sim; 2 - Não
    return input == '1'