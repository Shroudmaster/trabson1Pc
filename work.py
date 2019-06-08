import math

alfa = 0.578      #quantidade de tempo suscetivel a contaminação
beta = 0.391      #chance de reinfecção do meme
gamma = 0.126     #velocidade da perda de interesse

def healthy(t, values):   #eq. 1
	global alfa
	return (-alfa)*(values[0]*values[1])

# def exata(x,y):
# 	print(x,y)
# 	return (x - 1 + (2*(math.e- x)))


def infected(t, values):   #eq. 2
	global alfa,beta,gamma
	return ((alfa*values[0]*values[1]) + (beta*values[1]*values[2]) + (-gamma*values[1]))

def clean(t, values):    #eq. 3
	global beta,gamma
	return ((-beta*values[1]*values[2]) + (gamma*values[1]))

# def healthy(t,values):
# 	return ((-values[0]) + t)	


def rk2(values, t=0, h=0.1, iterations=3):
	aux = [0,0,0]
	v = [values.copy()]
	h_variation = [t]

	for _ in range(iterations):
		tp = t + h
		h_variation.append(tp)
		
		k1 =  [healthy(t,values),infected(t,values),clean(t,values)]
		
		aux = [values[0]+(h*k1[0]), values[1]+(h*k1[1]), values[2]+(h*k1[2])]
		
		k2 = [healthy(tp,aux), infected(tp,aux), clean(tp,aux)]
		values[0] = values[0] + (h/2)*(k1[0]+k2[0])
		values[1] = values[1] + (h/2)*(k1[1]+k2[1])
		values[2] = values[2] + (h/2)*(k1[2]+k2[2])

		t = tp
		v.append(values.copy())

	return v,h_variation

def imp(values, b, iterations=3, a=0):
	h = (b - a) / iterations

	v,h_variation = rk2(values,0,h,2)
	aux = [0,0,0]

	for _ in range(iterations):
		#primeiro calculamos o proximo valor para depois corrigi-lo com o implicito
		#calculando para a equação 1
		k1 = healthy(h_variation[-1], v[-1])
		k2 = healthy(h_variation[-2], v[-2])
		k3 = healthy(h_variation[-3], v[-3])

		aux[0] = v[-1][0] + ((h/12)*((23*k1) - (16*k2) + (5*k3)))
		
		#calculando para a equação 2		
		k1 = infected(h_variation[-1], v[-1])
		k2 = infected(h_variation[-2], v[-2])
		k3 = infected(h_variation[-3], v[-3])

		aux[1] = v[-1][1] + ((h/12)*((23*k1) - (16*k2) + (5*k3)))

		#calculando para a equação 3
		k1 = clean(h_variation[-1], v[-1])
		k2 = clean(h_variation[-2], v[-2])
		k3 = clean(h_variation[-3], v[-3])

		aux[2] = v[-1][2] + ((h/12)*((23*k1) - (16*k2) + (5*k3)))
		h_variation.append(h_variation[-1]+h)
		v.append(aux.copy())

		#agora que obtemos o novo vamos vamos corrigi-lo
		#calculando para a equação 1
		k1 = healthy(h_variation[-1], v[-1])
		k2 = healthy(h_variation[-2], v[-2])
		k3 = healthy(h_variation[-3], v[-3])
		k4 = healthy(h_variation[-4], v[-4])

		aux[0] = v[-2][0] + ((h/24)*((9*k1) + (19*k2) - (5*k3) + k4))

		#calculando para a equação 2
		k1 = infected(h_variation[-1], v[-1])
		k2 = infected(h_variation[-2], v[-2])
		k3 = infected(h_variation[-3], v[-3])
		k4 = infected(h_variation[-4], v[-4])

		aux[1] = v[-2][1] + ((h/24)*((9*k1) + (19*k2) - (5*k3) + k4))

		#calculando para a equação 3
		k1 = clean(h_variation[-1], v[-1])
		k2 = clean(h_variation[-2], v[-2])
		k3 = clean(h_variation[-3], v[-3])
		k4 = clean(h_variation[-4], v[-4])

		aux[2] = v[-2][2] + ((h/24)*((9*k1) + (19*k2) - (5*k3) + k4))

		v[-1] = aux.copy()

	return v



print(imp([1000,100,10], 100, 100))