from Game import *
import sys

def leituraDoArquivo(arquivo):
    #falta fazer: 
    #ler a primeira linha para ter informações do arquivo
    games = []
    linha = arquivo.readline()
    if not linha:
        return None
    
    arquivo.seek(0) #voltar para a primeira linha
    for linha in arquivo:
        campos = linha.strip().split('|') #separar no |
        if len(campos) == 9:
            nome = campos[0]
            produtora = campos[1]
            genero = campos[2]
            plataforma = campos[3]
            ano = campos[4]
            classificacao = campos[5]
            preco = campos[6]
            midia = campos[7]
            tamanho = campos[8]
            games.append(Game(nome,produtora,genero,plataforma,ano,classificacao,preco,midia,tamanho))

    return games
#def adicionaRegistro(arq, game):

# basicamente escrever um registro no final
# não esquecer o topo da pilha
#modificar codigo, lembrar que estamos trabalhando com tamanho fixo e campos variados
'''
def escritaDoArquivo(arquivo, games):
    linha=""
    for game in games:
        linha = f"{game.nome}|{game.produtora}|{game.genero}|{game.plataforma}|{game.ano}|{game.classificacao}|{game.preco}|{game.midia}|{game.tamanho}\n"
        arquivo.write(linha)

'''

def procuraRegistro(games, chaves):
    #procurar registro e já deletar
    encontrou = False
    linhas = []
    #adaptar codigo, a chave precisa ser dividida em duas
    for i, game in enumerate(games):
        if chaves.upper() in game.upper():  # Procura no formato canônico
            games[i] = "*|" + game[2:]
            encontrou = True
            #escrever o registro modificado no arquivo
            #mudar topo
    if not encontrou:
        print("Registro não encontrado")

    if encontrou:
        linhas = [game for game in games if not game.startswith('*|')]


'''
def ler_arquivo(arquivo):
    registros = []
    arquivo.seek(0)
    for linha in arquivo:
        registros.append(linha.strip())  # Salva cada registro em uma lista
    return registros

def storageCompaction(registros, chave):
    encontrou = False
    linhas = []

    for i, registro in enumerate(registros):
        if chave.upper() in registro.upper():  # Procura no formato canônico
            registros[i] = "*|" + registro[2:]
            encontrou = True
            #escrever o registro modificado no arquivo
    if not encontrou:
        print("Registro não encontrado")

    if encontrou:
        linhas = [registro for registro in registros if not registro.startswith('*|')]

    with open("storageCompaction.txt", 'w') as arq_saida:
        for linha in linhas:
            arq_saida.write(linha + '\n')
'''


def lerOperacao(arq, games):
    info=[]
    linha = arq.readline()
    if not linha:
        return None
    
    arq.seek(0) #voltar para a primeira linha
    #ler o primeiro caracter e salvar em op[]
    #ler as strings seguintes e salvar em dados[]
    for linha in arq:
        info = linha.strip().split(',') #separar na ,
        op=info[0] #operacao
        if op=='i':
            #usar adicionaRegistro
            #o codigo abaixo é uma gambiarra
            games.append(info[1],info[2],info[3],info[4],info[5], info[6], info[7], info[8], info[9])
        elif op=='d':
            procuraRegistro(games,info[1])
            
            

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


    try:
        with open(entrada, "r") as arq_entrada:
            jogos = leituraDoArquivo(arq_entrada)  
    except FileNotFoundError:
        print('O arquivo não foi encontrado.')

    try:
        with open(operacao,"r") as arq_operacao:
            #ler operações a serem realizadas
            lerOperacao(arq_operacao,jogos)
    except FileNotFoundError:
        print('O arquivo não foi encontrado.')
    
    
    print(op)
    print(dados)
    #fazer um if else para as operações


    #try:
    #with open(temporario,"w") as arq_temporario:
        #Escrever arquivo com com registro excluido  
    #except IOError:
        #print('Ocorreu um erro ao escrever o arquivo')

    #try:
    #with open(saida,"w") as arq_saida:
        #escrever arquivo com storageCompaction
    #except IOError:
        #print('Ocorreu um erro ao escrever o arquivo.')
            
   
