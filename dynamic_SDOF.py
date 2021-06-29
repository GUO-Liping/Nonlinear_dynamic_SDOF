import numpy as np

def func_f_D(para):
	return 0.2*para

def func_f_S(para):
	if 0 <=para < 1.2:
		return 5*para
	elif 1.2 <= para < 2.5:
		return 6
	else:
		return -5*para

def func_k(para):
	if 0 <=para < 1.2:
		return 5
	elif 1.2 <= para < 2.6:
		return 0
	else:
		return -5

def func_p(para):
	if round(10*para) == 0:
		return 0
	elif round(10*para) == 1:
		return 5
	elif round(10*para) == 2:
		return 8
	elif round(10*para) == 3:
		return 7
	elif round(10*para) == 4:
		return 5
	elif round(10*para) == 5:
		return 3
	elif round(10*para) == 6:
		return 2
	elif round(10*para) == 7:
		return 1
	elif round(10*para) == 8:
		return 0
	else:
		raise ValueError
m = 0.1
k_0 = 5
c_0 = 0.2

t = 0
t_s = 0.1

t_0 = 0
u_0 = 0
v_0 = 0

f_S0 = func_f_S(u_0)
f_D0 = func_f_D(v_0)
p_0 = func_p(t_0)

a_0 = 1/m * (p_0 - f_D0 - f_S0)
k_d = k_0 + 3*c_0/t_s + 6*m/(t_s**2)
delta_p = func_p(t_s) - func_p(t_0)

delta_p_d = delta_p + m*(6*v_0/t_s + 3*a_0) + c_0*(3*v_0 + t_s*a_0/2)
delta_u = delta_p_d/k_d
delta_v = 3*delta_u/t_s - 3*v_0 - t_s*a_0/2

n = 8
for i in range(n-1):
	t = t + t_s

	u_0 = u_0 + delta_u
	v_0 = v_0 + delta_v

	p_0 = func_p(t)
	f_S0 = func_f_S(u_0)
	f_D0 = func_f_D(v_0)

	a_0 = a_0 + 1/m * (p_0 - f_D0 - f_S0)
	k_0 = func_k(u_0)
	k_d = k_0 + 3*c_0/t_s + 6*m/(t_s**2)

	delta_p = func_p(t+t_s) - func_p(t)
	delta_p_d = delta_p + m*(6*v_0/t_s + 3*a_0) + c_0*(3*v_0 + t_s*a_0/2)

	#print('t=', t,'delta_p=',delta_p, 'u=', u_0, 'v=', v_0, 'a=', a_0)

	delta_u = delta_p_d/k_d
	delta_v = 3*delta_u/t_s - 3*v_0 - t_s*a_0/2

	print('k=', k_0, 'k_d=', k_d, 'u=', u_0, 'v=', v_0,'f_S0=', f_S0, 'f_D0=', f_D0)

