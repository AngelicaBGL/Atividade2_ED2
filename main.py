from Game import *
import sys

def leituraDoArquivo(arquivo):
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
#modificar codigo, lembrar que estamos trabalhando com tamanho fixo e campos variados
'''
def escritaDoArquivo(arquivo, games):
    linha=""
    for game in games:
        linha = f"{game.nome}|{game.produtora}|{game.genero}|{game.plataforma}|{game.ano}|{game.classificacao}|{game.preco}|{game.midia}|{game.tamanho}\n"
        arquivo.write(linha)

'''

#def procuraRegistro(arq, game):
#procurar registro e já deletar
#reaproveitar esse codigo
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

'''
from Game import Game 
import sys

def grep(arquivo, palavra):
    indices = []
    linha_numero = 0  # Número da linha atual

    for linha in arquivo:
        campos = linha.strip().split('|')  # Separar os campos
        for campo in campos:
            if palavra.lower() in campo.lower():  #comparando string (ignorando maiúsculas/minúsculas)
                indices.append(linha_numero) #salvar indices
                break  # Se a palavra for encontrada, não precisa verificar o restante dos campos
        linha_numero += 1

    return indices

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 programa.py arquivo_entrada.txt")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]

    
    with open(arquivo_entrada, 'r') as arquivo:
        print("Digite uma palavra para a busca: ")
        palavra = input()

        resultados = grep(arquivo, palavra)

        if resultados:
            print("Palavra encontrada nas seguintes linhas:")
            arquivo.seek(0)  # Voltar ao início do arquivo
            lines = arquivo.readlines()
            for linha_numero in resultados:
                if linha_numero < len(lines):
                    game = Game(*lines[linha_numero].strip().split('|'))
                    print(game)
        else:
            print("A palavra não foi encontrada em nenhuma linha.")

    
'''


if __name__== "__main__":
    if len(sys.argv) !=5:
        print("Uso: python3 programa.py entrada1.txt op.txt temp.txt saida.txt")
        sys.exit(1)

    jogos = []

    entrada = sys.argv[1]
    operacao = sys.argv[2]
    temporario = sys.argv[3]
    saida = sys.argv[4]


    try:
        with open(entrada, "r") as arq_entrada:
            jogos = leituraDoArquivo(arq_entrada)  
    except FileNotFoundError:
        print('O arquivo não foi encontrado.')

    #try:
        #with open(operacao,"r") as arq_operacao:
            #ler operações a serem realizadas
    #except FileNotFoundError:
        #print('O arquivo não foi encontrado.')
     
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
            
   
