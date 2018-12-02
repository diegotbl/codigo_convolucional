# Codificador utilizado pelo Algortimo de Viterbi

def codificar(u, G, M, V, MF):
    # u -> Bit de entrada
    # G -> Matriz de polinômios geradores, onde cada linha é um polinômio gerador Ex: (g1;g2;g3)
    # M -> Vetor com o estado atual da memória, sendo o elemento de menor índice corresponde
    # ao elemnto de maior grau no polinômio cíclico
    # Ex com m = 3 => M = (m3, m2, m1)
    # V -> Vetor com a palavra-código Ex: (v1, v2, v3)
    # MF -> Próximo estado da memória Ex: (m3, m2, m1) para m = 3

    # Realiza o shift da memória e adiciona a entrada, crinado o novo estado
    MF.extend(M[1:])
    MF.append(u)
    #print(len(G), len(G[1]))
    # Codificação da entrada
    for i in range(0, len(G)):
        for j in range(0, len(G[1])):
            # Uso das memórias
            if j == (len(G[1])-1):
                V[i] = (V[i] + G[i][j]*u)%2
            else:
                #print(i, j)
                V[i] = (V[i] + G[i][j]*M[j])%2


if __name__ == "__main__":
    G = [[1, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 0, 1]]
    M = [0, 0, 0, 1, 0, 0]
    # Cada linha de G gera um elemento de V
    V = [0, 0, 0]
    MF = []
    u = 1
    codificar(u, G, M, V, MF)
    print(V)
    print(M)
    print(MF)




