
def organizar_bp(cap_total, pesos, valores):
    qtd_prod = len(pesos)
    max_tab = [[0] * (cap_total + 1)] * (qtd_prod + 1)
    
    for i in range(qtd_prod):
        for j in range(cap_total):
            print("indice item atual: " + str(i))
            #print(j)
            if(pesos[i] > j):
                print("peso item atual: " + str(pesos[i]))
                max_tab[qtd_prod][cap_total] = max_tab[qtd_prod][cap_total-1]
            else:
                
                print("anterior: "+ str(max_tab[qtd_prod][cap_total-1]))
                print("anterior + valor: "+ str(max_tab[qtd_prod][cap_total-1] + valores[i]))
                
                max_tab[qtd_prod][cap_total] = max(max_tab[qtd_prod][cap_total-1], max_tab[qtd_prod][cap_total-1] + valores[i])
                
                print("valor escolhido:" + str(max(max_tab[qtd_prod][cap_total-1], max_tab[qtd_prod][cap_total-1] + valores[i])))
                printa_tab(max_tab)
                print()
            

    printa_tab(max_tab)

def printa_tab(tab):
    for i in tab:
        print(i)

def gera_casos(caso):
    if(caso == 1):
        return [165, [23, 31, 29, 44, 53, 38, 63, 85, 89, 82], [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]]
    
    elif(caso == 2): 
        return [190, [56, 59, 80, 64, 75, 17], [50, 50, 64, 46, 50, 5]]
    elif(caso == 3):
        return [2, [1, 1, 1], [10, 20, 30]]
    elif(caso == 4):
        return [50, [10, 20, 30], [60, 100, 120]]
    else:
        return [7, [5,2,2,1], [2,4,2,3]]
    

caso = gera_casos(3)

print(organizar_bp(caso[0], caso[1], caso[2]))

