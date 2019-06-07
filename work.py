def eq1(t):


def eq2(t):


def eq3(t):


def rk2(values, t=0, h=0.1, iterations=2):
	for _ in range(iterations):
		tp = t + h
		# calculo para eq. 1
		k1 = eq1(t,values[0])
		k2 = eq1(tp,(values[0]) + (h*k1))
		values[0] = values[0] + (h/2)*(k1+k2)

		# calculo para eq. 2
		k1 = eq2(t,values[1])
		k2 = eq2(tp,(values[1]) + (h*k1))
		values[1] = values[1] + (h/2)*(k1+k2)

		# calculo para eq. 1
		k1 = eq3(t,values[2])
		k2 = eq3(tp,(values[2]) + (h*k1))
		values[2] = values[2] + (h/2)*(k1+k2)