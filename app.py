from random import randrange
from source.codificador import codificar
from source.BSC import transmissao
from source.trelica import criarTrelica
from source.decodificador import decodificar
from matplotlib import pyplot as plt
from source.parametroCanalToEnergiaBit import converter
from source.canalGaussiano import canalGauss

def Gselector(m):
    if m == 3:
        return [[1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
    elif m == 4:
        return [[1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]]
    else:
        return [[1, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 0, 1]]

if __name__ == "__main__":
    convolucionalNormal = False
    convolucionalSemAproximacao = False
    BPSK = False
    cond = 2
    # Quantidade de memórias que serão testadas
    memories = [3]
    # Taxa de transmissão
    R = 1/3
    # Parâmetros do canal
    p = [0.5, 0, 4, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005, 0.0001, 0.00005, 0.00001]
    # Energia por bit de informação/Potência do canal
    ei_n0 = converter(p, R)
    # Número de bits de informação
    nBits = 5000
    # Entrada
    u = []
    # Gerar entrada
    for i in range(nBits):
        u.append(randrange(0, 9) % 2)
    for m in memories:
        print("Simulando para a memória {}".format(m))
        # Polinômios geradores
        G = Gselector(m)
        # Probabilidade de acerto
        pAcerto = []
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
            if cond == 2:
                Vaux = []
                for elemento in V:
                    if elemento == 0:
                        Vaux.append(-1)
                    else:
                        Vaux.append(1)
                C.append(Vaux)
            else:
                C.append(V)
            M.clear()
            M.extend(mf)
            mf.clear()
        # Trelica desse sistema
        trelica = criarTrelica(m, G, cond)
        # Transmissão
        if cond != 2:
            for parameter in p:
                T = transmissao(C, parameter)
                resposta = decodificar(m, T, trelica, cond, parameter)
                count = 0
                for i in range(len(resposta)):
                    if u[i] != resposta[i]:
                        count = count + 1
                pAcerto.append(count / nBits)
                print("Terminado para o parâmetro {}".format(parameter))
            print(pAcerto)
        else:
            for e in ei_n0:
                T = canalGauss(C, e, R)
                resposta = decodificar(m, T, trelica, cond, e)
                count = 0
                for i in range(len(resposta)):
                    if u[i] != resposta[i]:
                        count = count + 1
                pAcerto.append(count / nBits)
                print("Terminado para o parâmetro {}".format(e))
            print(pAcerto)

    # Plotar os resultados em um gráfico
    plt.loglog(p, p, linestyle="solid", label='Transmissão Direta')
    plt.loglog(p, pAcerto, linestyle="solid", label='m = 3')
    plt.legend(loc = 'upper right')
    plt.title("Probabilidade de erro x Ei/No")
    plt.xlabel("Ei/No")
    plt.xlim((0.5, 0))
    plt.ylabel("Probabilidade de erro")
    plt.show()