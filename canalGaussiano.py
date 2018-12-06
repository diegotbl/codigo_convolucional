import numpy as np

def canalGauss(T, ei_n0, taxaDeTransmissao):
    # T -> dados a serem transmitidos, já na modulação BPSK
    # ebi_n0 -> "parâmetro do canal"
    # taxaDeTransmissão -> quantidade de bits de informação transmitidos em uma palavra
    varianca = 1/(2*ei_n0)
    media = 0
    # O que foi captado após a transmissão pelo canal
    R = []
    # Transmissão
    for i in range(len(T)):
        ruido = np.random.normal(media, varianca, len(T[1]))
        aux = []
        for j in range(len(T[1])):
            aux.append(T[i][j] + ruido[j])
        R.append(aux)
    return R

if __name__ == "__main__":
    T = [[1, -1, 1], [1, 1, 1], [-1, -1, -1], [1, -1, 1]]
    ebi_n0s = [1.5000000000000002e-16, 0.09627174100028571, 0.4124930557323906, 1.0624863618455815, 2.463517195845924, 4.058198642706289, 6.326463985791422, 8.117088876234462, 9.95080492268385, 12.421649690570353, 14.316125226539597, 16.22480158254454, 20.66340521527296, 22.54018072689006, 26.53489705170363]
    R = 1/3
    for ebi_n0 in ebi_n0s:
        print("Para o seguinte {} ebi_n0".format(ebi_n0))
        R = canalGauss(T, ebi_n0, R)
        print("Escrever o sinal após passar pelo canal gaussiano")
        print(R)
        print("\nCalculando erro quadrático médio")
        for i in range(len(T)):
            answer = 0
            for j in range(len(T[1])):
                answer = answer + (T[i][j]-R[i][j])**2
            print(answer)
        print("")