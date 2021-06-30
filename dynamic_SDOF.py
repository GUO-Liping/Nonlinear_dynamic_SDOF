import numpy as np
import matplotlib.pyplot as plt

def func_f_D(para):
	return 0.2*para

def func_f_S(para, pv, uy, um):
	if pv>=0:
		if -uy <=para < uy:
			return 5*para
		elif uy <= para <= um:
			return 6
		else:
			print('para=',para)
			print('para=',para)
			raise ValueError
	elif pv<0:
		if -uy <=para < (um-2*uy):
			return -6
		elif (um-2*uy) <= para <= um:
			return -6+5*(para-(um-2*uy))
		else:
			print('para=',para)
			print('para=',para)
			raise ValueError
	else:
		raise ValueError

def func_k(para, pv, uy, um):
	if pv>=0:
		if -uy <=para < uy:
			return 5
		elif uy <= para <= um:
			return 0
		else:
			raise ValueError
	elif pv<0:
		if -uy <=para < (um-2*uy):
			return 0
		elif (um-2*uy) <=para <= um:
			return 5
		else:
			raise ValueError
	else:
		raise ValueError

def func_p(para):
	if 0<=para<=0.1:
		return 50*para
	elif 0.1<para<=0.2:
		return 5+30*(para-0.1)
	elif 0.2<para<=0.3:
		return 8-10*(para-0.2)
	elif 0.3<para<=0.4:
		return 7-20*(para-0.3)
	elif 0.4<para<=0.5:
		return 5-20*(para-0.4)
	elif 0.5<para<=0.6:
		return 3-10*(para-0.5)
	elif 0.6<para<=0.7:
		return 2-10*(para-0.6)
	elif 0.7<para<=0.8:
		return 1-10*(para-0.7)
	elif 0.8<para:
		return 0
	else:
		raise ValueError

m = 0.1
c_0 = 0.2

t = 0
t_s = 0.1

u_0 = 0
u_y = 1.2
u_m = 2.688

v_0 = 0

while(t<1.0):

	p_0 = func_p(t)
	f_S0 = func_f_S(u_0,v_0,u_y,u_m)
	f_D0 = func_f_D(v_0)

	a_0 = 1/m * (p_0 - f_D0 - f_S0)
	k_0 = func_k(u_0,v_0,u_y,u_m)
	k_d = k_0 + 3*c_0/t_s + 6*m/(t_s**2)

	delta_p = func_p(t+t_s) - func_p(t)
	delta_p_d = delta_p + m*(6*v_0/t_s + 3*a_0) + c_0*(3*v_0 + t_s*a_0/2)

	delta_u = delta_p_d/k_d
	delta_v = 3*delta_u/t_s - 3*v_0 - t_s*a_0/2

	print(
	 '\t', 	't=', format(t, '.3f'), 
	 '\t', 	'p=', format(p_0, '.3f'), 
	 '\t', 	'k=', format(k_0, '.3f'), 
	 '\t', 'k_d=', format(k_d, '.3f'),
	 '\t','u=', format(u_0, '.3f'), 
	 '\t','v=', format(v_0, '.3f'),
	 '\t','a=', format(a_0, '.3f'),
	 '\t','du=', format(delta_u, '.3f'), 
	 '\t','dv=', format(delta_v, '.3f'),
	 '\t','f_S0=', format(f_S0, '.3f'),
	 '\t','f_D0=', format(f_D0, '.3f')
	 )

	u_0 = u_0 + delta_u
	v_0 = v_0 + delta_v

	t = t + t_s

#plt.plot(t,u_0,'*')
#plt.show()
