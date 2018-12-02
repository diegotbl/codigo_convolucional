from matplotlib import pyplot as plt

pAcerto = [0.4918, 0.3182, 0.1971, 0.0067, 0.0003, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
p = [0.5, 0.25, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005, 0.0001]

plt.loglog(p, pAcerto, linestyle = "solid", label = 'm = 3')
plt.loglog(p, p, linestyle = "solid", label = 'Transmissão Direta')
plt.legend(loc = "upper right")
plt.title("Probabilidade de erro x parâmetro do canal")
plt.xlabel("Parâmetro do canal BSC")
plt.xlim((0.5, 0))
plt.ylabel("Probabilidade de erro")
plt.show()

