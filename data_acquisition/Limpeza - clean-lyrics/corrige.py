import re  # módulo de RegEx

with open("clean-lyrics (corrigido).csv", "w") as g:
    # Transformaremos os delimitadores em pipeline
    with open("clean-lyrics (original).csv") as f:
        texto = f.readlines()

    for linha in texto:
        nova_linha = linha[:-2]  # Eliminamos o ; e o \n finais

        if nova_linha[0] == '"':
            nova_linha = nova_linha[1:]  # Eliminamos o " inicial
        
        nova_linha = re.sub('""""', '', nova_linha)  # Eliminamos "aspas de string"
        nova_linha = re.sub('""', '"', nova_linha)  # Simplificamos "aspas de citação"
        nova_linha = re.sub("\\\'", "'", nova_linha)  # Eliminamos caractere de escape

        flag = 0  # Flag que indica se estamos dentro de citação (dentro de letra ou listagem)

        for i in range(len(nova_linha)):
            if nova_linha[i] == '"':  # Entramos em citação
                flag = 1 - flag
                continue
            if nova_linha[i] == ',' and not flag and nova_linha[i+1] != ' ':
                # Detectamos delimitadores verificando se precedem espaço e se estamos fora de uma citação
                g.write('|')
                continue
            if nova_linha[i] in "’´":
                g.write("'")
                # Padronizamos apóstrofo como '
                continue
            g.write(nova_linha[i])
        
        g.write("\n")