'''
Objetivo: encontrar o menor caminho num mapa entre qualquer cidade de bucharest,
utilizando como heurística a distância em linha reta entre as cidades e bucharest.

*heurística é o método utilizado para simplificar o processamento

Pseudo-Code:
# Criar uma Cidade, que armazena os atributos dela e as Cidades adjancentes
# Criar um banco de dados das distâncias em linha reta até bucharest(heurística)
# Criar um método de busca Gulosa, em que será dado o ponto de partida e o destino será bucharest
  No método de busca o algorítmo irá analisar as Cidades Adjacentes do ponto inicial e escolherá
  a Cidade com menor distância em linha reta até bucharest para ser o próximo ponto da busca
  (percebe-se que será um algoritmo recursivo).
'''
from distancias import dist_linha_reta

# Criar uma cidade:

class Cidade():
    def __init__(self, nome, distancia=None):
        self.nome = nome
        self.adjacentes = []

        # distancia entre Cidades
        self.distancia = distancia
        self.visitado = False


    def insereAdjacente(self, cidade, distancia):
        if isinstance(cidade, Cidade):
            # define a distância entre as cidades
            cidade.distancia = distancia
            self.adjacentes.append(cidade)


    def imprimeAdjacente(self):
        for cidade in self.adjacentes:
            print(f"Cidade: {cidade.nome} - Distância: {cidade.distancia}")


# Criar Busca Gulosa:

rota = []

def buscaGulosa(cidade_inicial, cidade_final):
    rota.append(cidade_inicial)
    if isinstance(cidade_inicial, Cidade):
        cidade_atual = cidade_inicial
        cidade_atual.visitado = True

        # ordenar por distâncias em linha reta(heurística da busca gulosa)
        cidade_atual.adjacentes.sort(key=lambda x: dist_linha_reta[str(x.nome)])

        # retirar as cidades que já foram visitadas
        cidades_adjacentes = list(filter(lambda x: x.visitado == False,cidade_atual.adjacentes))

        cidade_mais_perto = cidades_adjacentes[0]
        #print(cidade_mais_perto.nome)
        if cidade_mais_perto == cidade_final:
            rota.append(cidade_final)
            print("--- Melhor Trajeto pela Busca Gulosa ---")
            for c in rota:
                print(c.nome)

                # reseta o estado das cidades
                c.visitado = False

            rota.clear()
            return
        buscaGulosa(cidade_mais_perto, cidade_final)


# Criar Busca A*
def buscaAestrela(cidade_inicial, cidade_final):
    rota.append(cidade_inicial)
    if isinstance(cidade_inicial, Cidade):
        cidade_atual = cidade_inicial
        cidade_atual.visitado = True

        # ordenar por distâncias em linha reta + distância entre cidades(heurística da busca A*)
        cidade_atual.adjacentes.sort(key=lambda x: dist_linha_reta[str(x.nome)] + x.distancia)

        # retirar as cidades que já foram visitadas
        cidades_adjacentes = list(filter(lambda x: x.visitado == False, cidade_atual.adjacentes))

        cidade_mais_perto = cidades_adjacentes[0]
        #print(cidade_mais_perto.nome)
        if cidade_mais_perto == cidade_final:
            rota.append(cidade_final)
            print("--- Melhor Trajeto pela Busca Gulosa ---")
            for c in rota:
                print(c.nome)

                # reseta o estado das cidades
                c.visitado = False

            rota.clear()
            return
        buscaAestrela(cidade_mais_perto, cidade_final)

# Criar algumas cidades
arad = Cidade('Arad')
zerind = Cidade('Zerind')
timisoara = Cidade('Timisoara')
sibiu = Cidade('Sibiu')
fagaras = Cidade('Fagaras')
rimnicu = Cidade('Rimnicu Vilcea')
pitesti = Cidade('Pitesti')
craiova = Cidade('Craiova')
lugoj = Cidade('Lugoj')
bucharest = Cidade('Bucharest')
oradea = Cidade('Oradea')

# Inserir os adjancentes
arad.insereAdjacente(zerind, 75)
arad.insereAdjacente(sibiu, 140)
arad.insereAdjacente(timisoara, 118)

timisoara.insereAdjacente(arad, 118)
timisoara.insereAdjacente(lugoj, 111)

zerind.insereAdjacente(arad, 75)
zerind.insereAdjacente(oradea, 71)

sibiu.insereAdjacente(arad, 140)
sibiu.insereAdjacente(oradea, 151)
sibiu.insereAdjacente(rimnicu, 80)
sibiu.insereAdjacente(fagaras, 99)

rimnicu.insereAdjacente(sibiu, 80)
rimnicu.insereAdjacente(pitesti, 97)
rimnicu.insereAdjacente(craiova, 146)

fagaras.insereAdjacente(sibiu, 99)
fagaras.insereAdjacente(bucharest, 211)

pitesti.insereAdjacente(rimnicu, 97)
pitesti.insereAdjacente(craiova, 138)
pitesti.insereAdjacente(bucharest, 101)

craiova.insereAdjacente(rimnicu, 146)
craiova.insereAdjacente(pitesti, 138)

bucharest.insereAdjacente(fagaras, 211)
bucharest.insereAdjacente(pitesti, 101)

lugoj.insereAdjacente(timisoara, 111)

oradea.insereAdjacente(zerind, 71)
oradea.insereAdjacente(sibiu, 151)
