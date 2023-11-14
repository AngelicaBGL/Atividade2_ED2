# --------------------------------
# --------------------------------
class Game:
    # construtor do objeto Game
    def __init__(self, nome=None,produtora=None,genero=None,plataforma=None,
                 ano=None,classificacao=None,preco=None, midia=None, tamanho=None):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho
        self.produtora = produtora

    
    def __str__(self):
        output = str(self.nome) + "|" + \
        str(self.produtora) + "|" + str(self.genero) + "|" + str(self.plataforma) + \
        "|" + str(self.ano) + "|" + str(self.classificacao) + "|" + str(self.preco) + \
        "|" + str(self.midia) + "|" + str(self.tamanho)
        return output

# --------------------------------
# --------------------------------