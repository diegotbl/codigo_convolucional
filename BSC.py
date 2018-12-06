from random import *

# Realiza a transmissão bit a bit da palavra código
def transmissao(R, parametro):
    T = []
    lines = len(R)
    columns = len(R[1])
    for i in range(lines):
        aux = []
        for j in range(columns):
            if uniform(0, 1) <= parametro:
                aux.append((R[i][j] + 1) % 2)
            else:
                aux.append(R[i][j])
        T.append(aux)
    return T


if __name__ == "__main__":
    #R = [[1, 0, 1], [1, 1, 1], [0, 0, 1]]
    #p = 0.3
    #print(R)
    #print(transmissao(R, p))
    R = 1/3
    print(R)