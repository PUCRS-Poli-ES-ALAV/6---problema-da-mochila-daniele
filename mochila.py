def organizar_bp(qtd_prod, cap_total, pesos, valores):
    
    bp_final = []

    for i in range(qtd_prod + 1):
        bp_final.insert(i, [0] *((cap_total) + 1))

    print(bp_final)
    

    for i in range(qtd_prod):
        for j in range(cap_total):
            peso_item_atual = pesos[i]

            if(peso_item_atual <= j):
                bp_final[i][j] = peso_item_atual


organizar_bp(10, 10, [23, 31, 29, 44, 53, 38, 63, 85, 89, 82], [92, 57, 49, 68, 60, 43, 67, 84, 87, 72])
