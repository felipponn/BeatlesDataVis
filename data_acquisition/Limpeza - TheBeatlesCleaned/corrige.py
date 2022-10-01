import re

with open("TheBeatlesCleaned (corrigido).csv", "w") as f:
    with open("TheBeatlesCleaned (original).csv") as g:
        texto = g.readlines()

        for linha in texto:
            nova_linha = linha[1:]
            if linha[0] != '"':
                nova_linha = linha[0] + nova_linha
            if nova_linha[-2] == '"':
                nova_linha = nova_linha[:-2]+'\n'
            
            nova_linha = re.sub('""', '"', nova_linha)

            flag = 0

            for i in range(len(nova_linha)):
                if nova_linha[i] == ',' and not flag:
                    f.write('|')
                    continue
                if nova_linha[i] == '"':
                    flag = 1 - flag
                    continue
                f.write(nova_linha[i])