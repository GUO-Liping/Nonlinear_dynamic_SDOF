# -*- coding:-utf-8 -*-
# This programme aims at sovling the SDOF problems in
#"Dynamics of Structures  - 2nd Edition" example E7-2
#Impact force, Nonlinear stiffiness and nonlinear damp related.
# Numerical Solution
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
c = 0.2

t = 0
t_s = 0.1
t_total = 1.0
n_t = int(t_total/t_s)+1

u = 0
u_y = 1.2
u_m = 0

v = 0
u_array = np.zeros(n_t)
t_array = np.zeros(n_t)
i = 0
while(t<1.0 and i<1e3):
	u_array[i] = u
	t_array[i] = t
	p = func_p(t)
	f_S = func_f_S(u,v,u_y,u_m)
	f_D = func_f_D(v)

	a = 1/m * (p - f_D - f_S)
	k = func_k(u,v,u_y,u_m)
	k_d = k + 3*c/t_s + 6*m/(t_s**2)

	delta_p = func_p(t+t_s) - func_p(t)
	delta_p_d = delta_p + m*(6*v/t_s + 3*a) + c*(3*v + t_s*a/2)

	delta_u = delta_p_d/k_d
	delta_v = 3*delta_u/t_s - 3*v - t_s*a/2

	print(
	 '\t', 't=',   format(t, '.3f'), 
	 '\t', 'p=',   format(p, '.3f'), 
	 '\t', 'k=',   format(k, '.3f'), 
	 '\t', 'k_d=', format(k_d, '.3f'),
	 '\t', 'u=',   format(u, '.3f'), 
	 '\t', 'v=',   format(v, '.3f'),
	 '\t', 'a=',   format(a, '.3f'),
	 '\t', 'du=',  format(delta_u, '.3f'), 
	 '\t', 'dv=',  format(delta_v, '.3f'),
	 '\t', 'f_S=', format(f_S, '.3f'),
	 '\t', 'f_D=', format(f_D, '.3f')
	 )

	u = u + delta_u
	v = v + delta_v

	if u<u_m:
		u_m = u_m
	elif u >= u_m:
		u_m = u
	else:
		raise ValueError

	print('u_m=',u_m)
	
	t = t + t_s
	i = i + 1

plt.plot(t_array,u_array,'-*')
plt.show()
