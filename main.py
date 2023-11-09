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

#def procuraRegistro(arq, game):
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
if __name__== "__main__":
    if len(sys.argv) !=5:
        print("Uso: python3 programa.py entrada1.txt op.txt temp.txt saida.txt")
        sys.exit(1)
    jogos = []

    entrada = sys.argv[1]
    with open(entrada, "r") as arq_entrada:
        jogos = leituraDoArquivo(arq_entrada)   
            
    