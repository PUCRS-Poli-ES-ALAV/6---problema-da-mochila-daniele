class Item:
    peso = 0
    valor = 0

    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

#----------------------------------------------#

def organizar_bp(qtd_prod, cap_total, itens):
    itens.insert(0, None)
    max_tab = [[0] * (cap_total + 1)] * (qtd_prod + 1)

    #printa_tab(max_tab)

    for i in range(1, qtd_prod):
        for j in range(1, cap_total):
            item_atual = itens[i]
            
            valor_mesma_mochila_sem_item = max_tab[i - 1][j]

            if item_atual.peso <= j:
                valor_mochila = max_tab[i - 1][j - item_atual.peso]
                
                soma_valores = item_atual.valor + valor_mochila
                

                max_tab[i][j] = max(valor_mesma_mochila_sem_item, soma_valores)
                
            else:
                max_tab[i][j] = max_tab[i - 1][j]

    printa_tab(max_tab)

    return max_tab[qtd_prod][cap_total]
    
    
def printa_tab(tab):
    for i in tab:
        print(i)


def cria_itens(pesos, valores):
    lista = []
    for i in range(len(pesos)):
        lista.append(Item(pesos[i], valores[i]))

    
    return lista

#valores_caso = [165, [23, 31, 29, 44, 53, 38, 63, 85, 89, 82], [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]]
valores_caso = [190, [56, 59, 80, 64, 75, 17], [50, 50, 64, 46, 50, 5]]

itens_caso = cria_itens(valores_caso[1], valores_caso[2])

#caso = [valores_caso[0], itens_caso]

itens = [Item(5,2), Item(2,4), Item(2,2), Item(1,3)]
caso = [7, itens]

print(organizar_bp(len(caso[1]), caso[0], caso[1]))
