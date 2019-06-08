alfa = 0.2  #quantidade de tempo suscetivel a contaminação
beta = 0.1  #chance de reinfecção do meme
gamma = 0.1  #velocidade da perda de interesse

def eq1(t, values):
	return (-alfa)*(values[0]*values[1])

def eq2(t, values):
	return ((alfa*values[0]*values[1]) + (beta*values[1]*values[2]) + (-gamma*values[1]))

def eq3(t, values):
	return ((-beta*values[1]*values[2]) + (gamma*values[1]))

def rk2(values, t=0, h=0.1, iterations=2):
	aux = [0,0,0]
	for _ in range(iterations):
		tp = t + h
		
		k1 =  [eq1(t,values),eq2(t,values),eq3(t,values)]
		
		aux = [values[0]+(h*k1[0]), values[1]+(h*k1[1]), values[2]+(h*k1[2])]
		
		k2 = [eq1(tp,aux), eq2(tp,aux), eq3(tp,aux)]
		
		values[0] = values[0] + (h/2)*(k1[0]+k2[0])
		values[1] = values[1] + (h/2)*(k1[1]+k2[1])
		values[2] = values[2] + (h/2)*(k1[2]+k2[2])

		print(values)

rk2([1000,10,0])