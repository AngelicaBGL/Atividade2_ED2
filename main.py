from Game import *
import sys

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
    games = [qtdRegistros]

    for linha in arquivo:
        campos = linha.strip().split('|')  # separar no |
        if len(campos) == 9:
            nome, produtora, genero, plataforma, ano, classificacao, preco, midia, tamanho = campos
            games.append(Game(nome, produtora, genero, plataforma, ano, classificacao, preco, midia, tamanho))
           

    return games, qtdRegistros, top

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
#def removeRegistro()
#dentro dessa função deve-se chamar procuraRegistro

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


def lerOperacao(arquivo, jogos):
    operacoes = []

    for linha in arquivo:
        campos = linha.strip().split('|')
        operacao = campos[0]

        if operacao == 'inserir':
            info = campos[1:]

            # Certifique-se de que há informações suficientes para criar uma instância de Game
            if len(info) == 9:
                #fazer de novo, mas usar adicionaRegistro
                nome, produtora, genero, plataforma, ano, classificacao, preco, midia, tamanho = info
                jogo = Game(nome, produtora, genero, plataforma, ano, classificacao, preco, midia, tamanho)
                operacoes.append(('inserir', jogo))
        elif operacao == 'remover':
            # Lógica para remover um jogo, se necessário
            pass
        # Adicione mais lógica para outras operações, se necessário
    #acho que seria melhor retornar os jogos atualizados
    #mudar codigo
    return operacoes

            
            

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
            jogos,qtdRegistros,top = leituraDoArquivo(arq_entrada)  
    except FileNotFoundError:
        print('O arquivo não foi encontrado.')
    
    try:
        with open(operacao,"r") as arq_operacao:
            #ler operações a serem realizadas
            lerOperacao(arq_operacao,jogos)
    except FileNotFoundError:
        print('O arquivo não foi encontrado.')
    
   


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
            
   
