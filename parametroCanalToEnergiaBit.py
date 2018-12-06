from scipy.stats import norm
from math import sqrt

def converter(p, R):
    # p -> parâmetro do canal de transmissão
    # R -> Taxa de transmissão de bits de informação
    aux = []
    aux.extend(p)
    ei_n0 = []
    x = 0.000001
    while len(aux)>0:
        parameter = norm.sf(x)
        for elemento in aux:
            if abs(parameter - elemento) < 0.000003:
                aux.remove(elemento)
                ei_n0.append(pow(x, 2)/(2*R))
                break
        x = x + 0.00001

    return ei_n0

if __name__ == "__main__":
    p = [0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005, 0.0001, 0.00005, 0.00001]
    R = 1/3
    result = converter(p, R)
    for elemento in result:
        print(1 - norm.cdf(sqrt(2*R*elemento)))
    print(result)