from random import randrange
from source.codificador import codificar
from source.BSC import transmissao
from source.trelica import criarTrelica
from source.decodificador import decodificar
from matplotlib import pyplot as plt

def Gselector(m):
    if m == 3:
        return [[1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
    elif m == 4:
        return [[1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]]
    else:
        return [[1, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 0, 1]]

if __name__ == "__main__":
    # Quantidade de memórias que serão testadas
    memories = [3, 4, 6]
    # Parâmetros do canal
    p = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005, 0.0001, 0.00005, 0.00001]
    # Probbabilidade tota de acerto para as memória
    pAcerto = []
    # Número de bits de informação
    nBits = 10000
    # Entrada
    u = []
    # Gerar entrada
    for i in range(nBits):
        u.append(randrange(0, 9) % 2)
    for m in memories:
        print("Simulando para a memória {}".format(m))
        # Polinômios geradores
        G = Gselector(m)
        # Probabilidade de acerto com a correção para uma certa quantidade de memória
        pAcertoM = []
        # Palavras código
        C = []
        # Palavras recebidas da transmissão
        T = []
        # Auxiliar de estado final para codificação
        mf = []
        # Memória inicial
        M = []
        for aux in range(m):
            M.append(0)
        for ele in u:
            V = [0, 0, 0]
            codificar(ele, G, M, V, mf)
            C.append(V)
            M.clear()
            M.extend(mf)
            mf.clear()

        # Trelica desse sistema
        trelica = criarTrelica(m, G)
        for parameter in p:
            T = transmissao(C, parameter)
            resposta = decodificar(m, T, trelica)
            count = 0
            for i in range(len(resposta)):
                if u[i] != resposta[i]:
                    count = count + 1
            pAcertoM.append(count / nBits)
            print("Terminado para o parâmetro {}".format(parameter))
        pAcerto.append(pAcertoM)

    # Plotar os resultados em um gráfico
    plt.loglog(p, p, linestyle="solid", label='Transmissão Direta')
    k = 0
    for pm in pAcerto:
        if k == 0:
            plt.loglog(p, pm, linestyle="solid", label='m = 3')
        elif k == 1:
            plt.loglog(p, pm, linestyle="solid", label='m = 4')
        else:
            plt.loglog(p, pm, linestyle="solid", label='m = 6')
        k =k +1
    plt.legend(loc = 'upper right')
    plt.title("Probabilidade de erro x parâmetro do canal")
    plt.xlabel("Parâmetro do canal BSC")
    plt.xlim((0.5, 0))
    plt.ylabel("Probabilidade de erro")
    plt.show()