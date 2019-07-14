import math
import matplotlib.pyplot as plt
import numpy as np


def susceptible(t, values):   #eq. 1
	return (-alfa)*values[0]*values[1]


def infectious(t, values):   #eq. 2
	return alfa*values[0]*values[1] + beta*values[1]*values[2] + (-gamma)*values[1]


def recovered(t, values):    #eq. 3
	return (-beta)*values[1]*values[2] + gamma*values[1]


def sir(t, values):
	return susceptible(t, values), infectious(t, values), recovered(t, values)


def rk2(values, t=0, h=0.1, iterations=3):  #implementacao do rk2 para valores iniciais
	aux = [0,0,0]
	v = [values.copy()]
	h_variation = [t]

	for _ in range(iterations):
		tp = t + h
		h_variation.append(tp)

		k1 = sir(t, values)

		aux = [values[0]+(h*k1[0]), values[1]+(h*k1[1]), values[2]+(h*k1[2])]

		k2 = sir(tp, aux)

		values[0] = values[0] + (h/2)*(k1[0]+k2[0])
		values[1] = values[1] + (h/2)*(k1[1]+k2[1])
		values[2] = values[2] + (h/2)*(k1[2]+k2[2])

		t = tp
		v.append(values.copy())

	return v,h_variation


def imp(values, b, iterations=3, a=0):
	h = (b - a) / iterations
	v, h_variation = rk2(values,0,h,2)
	aux = [0,0,0]

	for _ in range(iterations):
		# primeiro calculamos o proximo valor para depois corrigi-lo com o implicito
		# o proximo valor e calculado usando o adams-bashfort e a correcao e feita com
		# o adams-moulton

		# calculando para a equação 1
		k1 = susceptible(h_variation[-1], v[-1])
		k2 = susceptible(h_variation[-2], v[-2])
		k3 = susceptible(h_variation[-3], v[-3])

		aux[0] = v[-1][0] + ((h/12)*((23*k1) - (16*k2) + (5*k3)))

		# calculando para a equação 2
		k1 = infectious(h_variation[-1], v[-1])
		k2 = infectious(h_variation[-2], v[-2])
		k3 = infectious(h_variation[-3], v[-3])

		aux[1] = v[-1][1] + ((h/12)*((23*k1) - (16*k2) + (5*k3)))

		# calculando para a equação 3
		k1 = recovered(h_variation[-1], v[-1])
		k2 = recovered(h_variation[-2], v[-2])
		k3 = recovered(h_variation[-3], v[-3])

		aux[2] = v[-1][2] + ((h/12)*((23*k1) - (16*k2) + (5*k3)))
		h_variation.append(h_variation[-1]+h)
		v.append(aux.copy())

		# agora que obtemos o novo vamos vamos corrigi-lo

		# calculando para a equação 1
		k1 = susceptible(h_variation[-1], v[-1])
		k2 = susceptible(h_variation[-2], v[-2])
		k3 = susceptible(h_variation[-3], v[-3])
		k4 = susceptible(h_variation[-4], v[-4])

		aux[0] = v[-2][0] + ((h/24)*((9*k1) + (19*k2) - (5*k3) + k4))

		# calculando para a equação 2
		k1 = infectious(h_variation[-1], v[-1])
		k2 = infectious(h_variation[-2], v[-2])
		k3 = infectious(h_variation[-3], v[-3])
		k4 = infectious(h_variation[-4], v[-4])

		aux[1] = v[-2][1] + ((h/24)*((9*k1) + (19*k2) - (5*k3) + k4))

		# calculando para a equação 3
		k1 = recovered(h_variation[-1], v[-1])
		k2 = recovered(h_variation[-2], v[-2])
		k3 = recovered(h_variation[-3], v[-3])
		k4 = recovered(h_variation[-4], v[-4])

		aux[2] = v[-2][2] + ((h/24)*((9*k1) + (19*k2) - (5*k3) + k4))

		v[-1] = aux.copy()

	return v, h_variation


def plot(v, h):   #funcao que plota o grafico do resultado
	v = np.array(v)
	s = v[:, 0]
	i = v[:, 1]
	r = v[:, 2]
	plt.plot(h, s, c="green", label="S")
	plt.plot(h, i, c="red", label="I")
	plt.plot(h, r, c="black", label="R")
	plt.legend()
	plt.show()
	plt.close()


def check(values):
	print((alfa-beta)*values[0] + beta*sum(values) - gamma)
	# return (alfa-beta)*values[0] + beta*sum(values) - gamma <= 0
	return 1

# alfa, beta, gamma = 0.015, 0.003, 3.3
# values = [1000,50,10]  # S(0), I(0), R(0)

alfa = float(input("Digite o valor do alfa (quantidade de tempo suscetivel a contaminação): "))
beta = float(input("Digite o valor do beta (chance de reinfecção do meme): "))
gamma = float(input("Digite o valor do gamma (velocidade da perda de interesse): "))


s = int(input("Digite o valor inicial de individuos suscetiveis a contaminacao: "))
i = int(input("Digite o valor inicial de individuos infectados: "))
r = int(input("Digite o valor inicial de individuos recuperados: "))

values = [s,i,r]

if check(values):
	v, h = imp(values.copy(), 20, 800)
	plot(v, h)

else:
	print("Valores inapropriados")
