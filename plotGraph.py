from matplotlib import pyplot as plt
from source.parametroCanalToEnergiaBit import converter

plotHamming = True
plotBPSK = True
plotCiclico = False
plotConvolucionalNormal = True
plotConvolucionalSemAproximacao = True

pAcertoHamming = [0.499805, 0.321588, 0.195864, 0.06737, 0.01976, 0.003514, 0.0009139, 0.0002197]#, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
pAcertoConvolucional = [0.4996, 0.4088, 0.1911, 0.0056, 0.0006, 0.0, 0.0, 0.0]#, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
pAcertoSemAproximacao = [0.444, 0.4084, 0.1726, 0.009, 0.0000, 0.0000, 0.0000, 0.0000]#, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
pAcertoBPSK = [0.5015, 0.0709, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]#, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
pAcertoCiclico = []
p = [0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]#, 0.002, 0.001, 0.0005, 0.0001, 0.00005, 0.00001]

if plotHamming:
    R = 4/7
    ei_n0 = converter(p, R)
    plt.plot(ei_n0, pAcertoHamming, linestyle = 'solid', label = 'Hamming')

R = 1/3
ei_n0 = converter(p, R)

if plotBPSK:
    plt.plot(ei_n0, pAcertoBPSK, linestyle="solid", label='BPSK com m = 3')

if plotConvolucionalNormal:
    plt.plot(ei_n0, pAcertoConvolucional, linestyle="solid", label='Convolucional m = 3')

if plotConvolucionalSemAproximacao:
    plt.plot(ei_n0, pAcertoSemAproximacao, linestyle="solid", label='Convolucional sem aproximação m = 3')

plt.plot(ei_n0, p, linestyle = "solid", label = 'Transmissão Direta')
plt.plot()
plt.yscale('log')
plt.xscale('linear')
plt.legend(loc = "lower left")
plt.title("Probabilidade de erro x Ei/No")
plt.xlabel("Ei/No")
plt.xlim((-10, 100))
plt.ylabel("Probabilidade de erro")
plt.show()

