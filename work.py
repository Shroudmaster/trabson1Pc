import math

alfa = 5.78      #quantidade de tempo suscetivel a contaminação
beta = 3.91      #chance de reinfecção do meme
gamma = 1.26     #velocidade da perda de interesse

def healthy(t, values):
	global alfa
	# print((-alfa)*(values[0]*values[1]))
	return (-alfa)*(values[0]*values[1])

def infected(t, values):
	global alfa,beta,gamma
	# print(((alfa*values[0]*values[1]) + (beta*values[1]*values[2]) + (-gamma*values[1])))
	return ((alfa*values[0]*values[1]) + (beta*values[1]*values[2]) + (-gamma*values[1]))

def clean(t, values):
	global beta,gamma
	# print(((-beta*values[1]*values[2]) + (gamma*values[1])))
	return ((-beta*values[1]*values[2]) + (gamma*values[1]))
	

def rk2(values, t=0, h=0.1, iterations=3):
	aux = [0,0,0]
	for _ in range(iterations):
		tp = t + h
		
		k1 =  [healthy(t,values),infected(t,values),clean(t,values)]
		
		aux = [values[0]+(h*k1[0]), values[1]+(h*k1[1]), values[2]+(h*k1[2])]
		
		k2 = [healthy(tp,aux), infected(tp,aux), clean(tp,aux)]
		
		values[0] = values[0] + (h/2)*(k1[0]+k2[0])
		values[1] = values[1] + (h/2)*(k1[1]+k2[1])
		values[2] = values[2] + (h/2)*(k1[2]+k2[2])

		print(values)

rk2([1,0,100])