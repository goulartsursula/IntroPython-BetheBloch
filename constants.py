from numpy import pi, power

c = 3e10  # Velocidade da luz [cm/s]
r_e = 2.818e-15  # Raio clássico do elétron [m]
N_A = 6.022e23  # Número de avogadro [mol^-1]
p = 8.960
A = 63.546  # Massa atômica [g.mol^-1]
Z = 29  # Número atômico [adimensional]
z = 3.55
m_e = 0.5110  # Massa do elétron [MeV]
e_I = 322  # Energia média de excitação [MeV]
K = 4 * pi * N_A * power(r_e, 2) * m_e  # [MeV cm^2 mol^-1]
