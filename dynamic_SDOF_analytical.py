# -*- coding:utf-8 -*-
# 本程序用于解决正弦波冲击荷载下，常刚度、常阻尼单自由度体系的位移、速度、加速度时程曲线
# 正弦波脉冲为1/2周期的正弦波，冲击时长为1/2正弦函数周期
# 《结构动力学-第2版》 克拉夫 彭津 编著
import numpy as np
import matplotlib.pyplot as plt

t1 = 0.1
t_end = 0.5
t_step = 0.002

t_I = np.arange(0, t1+0.5*t_step, step=t_step)
t_II = np.arange(t1, t_end, step=t_step)

s = 5
k = 12000
xi = 0.1
omega = np.sqrt(k/s)
omega_D = omega*np.sqrt(1-xi**2)

p_0 = 500
omega_p = np.pi/t1
beta = omega_p/omega

# 以下为第一阶段，第一阶段正弦波脉冲荷载作用下结构发生强迫振动
u0 =0.1
v0 = 0.5

A = u0
B = (v0+u0*xi*omega)/omega_D

G1 = p_0/k * (-2*xi*beta)/((1-beta**2)**2+(2*xi*beta)**2)
G2 = p_0/k * (1-beta**2) /((1-beta**2)**2+(2*xi*beta)**2)

item1 = np.cos(omega_D*t_I)
item2 = np.sin(omega_D*t_I)
item3 = np.exp(-xi*omega*t_I)
item4 = np.cos(omega_p*t_I)
item5 = np.sin(omega_p*t_I)

ut = (A*item1+B*item2)*item3 + G1*item4 + G2*item5
vt = (-xi*omega)*item3*(A*item1+B*item2) - omega_D*item3*(A*item2-B*item1) - G1*omega_p*item5 + G2*omega_p*item4
at = (xi*omega)**2*item3*(A*item1+B*item2) + omega_D*xi*omega*item3*(A*item2-B*item1) + (xi*omega)*omega_D*item3*(A*item2-B*item1) - omega_D**2*item3*(A*item1+B*item2) - G1*omega_p**2*item4 - G2*omega_p**2*item5

# 以下为第二阶段，第二阶段正弦波脉冲荷载作用结束后，结构开始自由振动
u_t1 = ut[-1]
v_t1 = vt[-1] 
a_t1 = at[-1] 

C1 = u_t1
C2 = (v_t1+u_t1*xi*omega)/omega_D
C3 = np.exp(-xi*omega*(t_II-t1))
ut_free = (C1*np.cos(omega_D*(t_II-t1))+C2 * np.sin(omega_D*(t_II-t1)))*C3
vt_free = ut_free*(-xi*omega) + (-C1*np.sin(omega_D*(t_II-t1))+C2*np.cos(omega_D*(t_II-t1)))*C3*omega_D
at_free = vt_free*(-xi*omega) + (-C1*np.sin(omega_D*(t_II-t1))+C2*np.cos(omega_D*(t_II-t1)))*C3*omega_D*(-xi*omega) - (C1*np.cos(omega_D*(t_II-t1))+C2 * np.sin(omega_D*(t_II-t1)))*C3*omega_D**2
at_free1 = -2*xi*omega*vt_free + (xi**2*omega**2 - omega_D**2)*ut_free

t_total = np.hstack((t_I,t_II))
u_total = np.hstack((ut, ut_free))
v_total = np.hstack((vt, vt_free))
a_total = np.hstack((at, at_free))

plt.subplot(1,3,1)
plt.plot(t_total,u_total,'-',label='ut')
plt.legend(loc="best",fontsize=8)

plt.subplot(1,3,2)
plt.plot(t_total,v_total,'-',label='vt')
plt.legend(loc="best",fontsize=8)

plt.subplot(1,3,3)
plt.plot(t_total,a_total,'-',label='at')
plt.legend(loc="best",fontsize=8)
plt.show()

