from source.trelica import criarTrelica
from source.codificador import codificar

#Decodificador baseado no algortimo de Viterbi

def estados(m):
    alpha = [0, 1]
    if m == 3:
        M = [[a, b, c] for a in alpha for b in alpha for c in alpha]
    elif m == 4:
        M = [[a, b, c, d] for a in alpha for b in alpha for c in alpha for d in alpha]
    else:
        M = [[a, b, c, d, e] for a in alpha for b in alpha for c in alpha for d in alpha for e in alpha]
    return M

# Função de custo
def DistanciaHamming(a, b):
    count = 0
    for l in range(len(a)):
        if a[l] != b[l]:
            count = count + 1
    return count

def binToInt(elemento):
    count = 0
    tam = len(elemento)
    for l in range(tam):
        count = count + pow(2, tam-1 - l)*elemento[l]
    return count


def decodificar(m, T, trelica):
    # m -> quantidade de memórias
    # T -> matriz de palavras código a serem decodificadas na forma (t3, t2, t1)
    # trelica -> trelica do algortimo usada para decodificação, mostrando todas as transições possíveis
    # Estados possíveis de memóriao = []
    M = estados(m)
    # Dicionário que guarda o peso aculmulado de cada memória
    dicPeso = {}
    for elemento in M:
        index = binToInt(elemento)
        dicPeso[index] = 0
    # caminho -> Será da forma (k, estadoInicial, estadoFinal, valor aculmulado)
    caminho = []
    # possibilidades -> Mostra a possibilidade de cada elemento

    estadoInicial = []
    estadosAcessados = []
    for a in range(m):
        estadoInicial.append(0)
    estadosAcessados.append(estadoInicial)
    # Cada k marca uma palavra código que será decodificada
    for k in range(len(T)):
        # Guarda os novos trechos que serão adicionados ao caminho
        possibilidades = []

        # Isso é para garantir que só serão olhados os estados que já foram atingidos na busca
        for estado in estadosAcessados:

            # Acha o elemento no automato
            for elemento in trelica:
                if estado == elemento[0]:
                    palavra = elemento[2]
                    index = binToInt(estado)
                    distancia = DistanciaHamming(T[k], palavra) + dicPeso[index]
                    # Analisa se vale a pena trocar o trecho atual cujo estadoFinal é elemento[3] por esse novo encontrado
                    existe = False
                    for possibilidade in possibilidades:
                        # Analisa se já existe algum caminho apontando para aquele estado final
                        if possibilidade[2] == elemento[3] and possibilidade[0] == k:
                            existe = True
                            if possibilidade[3] > distancia:
                                possibilidades.remove(possibilidade)
                                possibilidades.append((k, elemento[0], elemento[3], distancia))
                    if not existe:
                        possibilidades.append((k, elemento[0], elemento[3], distancia))

        #Insere os novos trechos no caminho e atualiza os Estados acessados e os pesos aculmulados dos estados
        for possibilidade in possibilidades:
            if len(estadosAcessados) != pow(2, m):
                if possibilidade[2] not in estadosAcessados:
                    estadosAcessados.append(possibilidade[2])
            index = binToInt(possibilidade[2])
            dicPeso[index] = possibilidade[3]
            caminho.append(possibilidade)
    #print(dicPeso)
    # Achar o menor peso final aculmulado
    menorPeso = -1
    for key in dicPeso.keys():
        if menorPeso < 0:
            menorPeso = dicPeso[key]
        elif menorPeso > dicPeso[key]:
            menorPeso = dicPeso[key]
    #print(menorPeso)
    # Escreve o caminho que foi percorrido e guardar a sequência de bits enviada
    k = len(T)-1
    u = []
    estadoAtual = []
    # Percorrer o caminho da decodificação
    #for element in caminho:
    #    if element[3] == 0:
            #print(element)
    while k >= 0:
        if k == len(T)-1:
            for trecho in caminho:
                if trecho[3] == menorPeso and k == trecho[0]:
                    #print(trecho[2])
                    estadoAtual = trecho[1]
                    #print(estadoAtual)
                    for elemento in trelica:
                        if elemento[0] == trecho[1] and elemento[3] == trecho[2]:
                            u.append(elemento[1])
                    k = k-1
                    break
        else:
            for trecho in caminho:
                if trecho[2] == estadoAtual and k == trecho[0]:
                    estadoAtual = trecho[1]
                    #print(estadoAtual)
                    for elemento in trelica:
                        if elemento[0] == trecho[1] and elemento[3] == trecho[2]:
                            u.append(elemento[1])
                    k = k-1
                    break
    u.reverse()

    return u
    #print(estadoAtual)
    # Nesse ponto, basta percorrer o caminho que gera a decodificação





if __name__ == "__main__":
    m = 3
    G = [[1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
    u = [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
    T = []
    mf = []
    M = [0, 0, 0]
    for ele in u:
        V = [0, 0, 0]
        codificar(ele, G, M, V, mf)
        #print(mf)
        T.append(V)
        M.clear()
        M.extend(mf)
        mf.clear()
    print(T)
    trelica = criarTrelica(m, G)
    T = [[0, 0, 1], [1, 0, 1], [1, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
    #print(T)
    print(u)
    print(decodificar(m, T, trelica))

