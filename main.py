from Game import *
import sys


# ler o arquivo de entrada, salvar as informações do cabeçalho
#e salvar todos os jogos em uma lista
def leituraDoArquivo(arquivo):
    linha = arquivo.readline()
    if not linha:
        return None

    arquivo.seek(0)  # voltar para a primeira linha
    primeiraLinha = linha.strip()
    infosArq = primeiraLinha.split()

    # Verificar se há pelo menos dois elementos em infosArq
    if len(infosArq) < 2:
        return None

    qtdRegistros_str = infosArq[0].split('=')
    top_str = infosArq[1].split('=')

    # Verificar se há pelo menos dois elementos em qtdRegistros_str e top_str
    if len(qtdRegistros_str) < 2 or len(top_str) < 2:
        return None

    qtdRegistros = int(qtdRegistros_str[1])  # quantidade de registros no arquivo
    top = int(top_str[1])
    games = []

    for linha in arquivo:
        campos = linha.strip().split('|')  # separar no |
        if len(campos) == 9:
            nome, produtora, genero, plataforma, ano, classificacao, preco, midia, tamanho = campos
            games.append(Game(nome, produtora, genero, plataforma, ano, classificacao, preco, midia, tamanho))
           

    return games, qtdRegistros, top

# adicionar novo jogo na lista
def adicionaRegistro(games, novoJogo,tamanho):
    #adicionar um jogo na lista
    #atualizar a qtd de registros
    return games, tamanho

#remover jogo, atualizar informações para cabeçalho
def removeRegistro(jogos,tamanho,top,indice):
    #preciso colocar *(top)| na frente do nome
    #atualizar top e tamanho
    #registros[i] = "*|" + registro[2:]
    jogos[indice].nome = "*" + str(top) + "|" + jogos[indice].nome[4:]
    tamanho-= 1
    top = indice
    return jogos, tamanho, top

#procurar um jogo na lista
#se encontrar será removido
def procuraRegistro(games, chave, tamanho, top):
    indice=-1 # as linhas começam em 0
    print(tamanho)
    for game in games:
        chave_registro = f"{game.nome}{game.ano}"
        chave_registro = chave_registro.replace(" ","") # tirar os espaços
        indice += 1
        if chave.upper() in chave_registro.upper():
            games, tamanho, top = removeRegistro(games,tamanho, top,indice)
            print(games[indice])
            print(tamanho)
            print(top)
            return games, tamanho, top

    print("Registro {chave} não encontrado")

#ler as operações
#se 'i' será inserido um novo jogo usando adicionaRegistro()
#se 'd' será pesquisado o jogo usando procuraRegistro(), o jogo será apagado em seguida
def lerOperacao(arquivo, jogos,tamanho, top):

    for linha in arquivo:
        campos = linha.strip().split(',')
        operacao = campos[0]
        print(operacao)
        if operacao == 'i':
            info = campos[1:]
            # Certificare de que há informações suficientes
            if len(info) == 9:
                #fazer de novo, mas usar adicionaRegistro
                jogos, tamanho = adicionaRegistro(jogos, info, tamanho)
        elif operacao == 'd':
            chave = campos[1].replace(" ","")#tirar o espaço do começo
            jogos,tamanho,top = procuraRegistro(jogos,chave, tamanho,top)

    return jogos,tamanho,top

#escreve o arquivo com os registros finais
#escreverArquivoTemporario()
#se voce quiser ajudar com alguma coisa, poded fazer essa

#função para compactar o arquivo
#storageCompaction()
#se voce quiser ajudar com alguma coisa, poded fazer essa
            

if __name__== "__main__":
    if len(sys.argv) !=5:
        print("Uso: python3 programa.py entrada1.txt op.txt temp.txt saida.txt")
        sys.exit(1)

    jogos = []
    op = []
    dados = []
    
    
    entrada = sys.argv[1]
    operacao = sys.argv[2]
    temporario = sys.argv[3]
    saida = sys.argv[4]

    # arquivo de entrada
    try:
        with open(entrada, "r") as arq_entrada:
            jogos,qtdRegistros,top = leituraDoArquivo(arq_entrada)  
    except FileNotFoundError:
        print('O arquivo não foi encontrado.')
    
    #arquivo com as operações
    try:
        with open(operacao,"r") as arq_operacao:
            #ler operações a serem realizadas
            #e executar o que é pedido
            jogos,qtdRegistros,top = lerOperacao(arq_operacao,jogos,qtdRegistros,top)
    except FileNotFoundError:
        print('O arquivo não foi encontrado.')

    #arquivo temporário
    try:
        with open(temporario,"w") as arq_temporario:
            #Escrever arquivo com com registro excluido  
            print("arquivo temporario foi aberto")
    except IOError:
        print('Ocorreu um erro ao escrever o arquivo')      

    #arquivo compactado
    try:
        with open(saida,"w") as arq_saida:
            #escrever arquivo com storageCompaction
            print("Arquivo de saida foi aberto")
    except IOError:
        print('Ocorreu um erro ao escrever o arquivo.')
       
