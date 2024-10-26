# import matplotlib as plt
# import numpy as np
# import pandas as pd
# from scipy.stats import beta
# from scipy.stats import norm
# from scipy.optimize import fsolve

# df = pd.read_csv("SuperMarketData.csv")

# print(df.head())

# sales = np.array(df["Sales"])*19.88

# max_sales = max(sales)
# min_sales = min(sales)
# sales_norm = (1/(max_sales - min_sales)) * (sales - min_sales)
# a,b,_,_=beta.fit(sales)

# print(a,b)

# mu_norm = a / (a + b)
# var_norm = (a * b) / ((a + b) ** 2 * (a+b+1))
# desv_norm = np.sqrt(var_norm)

# # mu = (max_sales - min_sales) * (mu_norm - min_sales)
# mu = mu_norm * (max_sales - min_sales) + min_sales
# var = (max_sales - min_sales) ** 2 * var_norm
# sigma = np.sqrt(var)
# print(mu_norm, var_norm)


# #------Salarios------
# fact = 1.15

# sal_cajeros = 258.25
# num_cajeros = 30
# dias_t = 24

# tot_sal_caj = sal_cajeros * num_cajeros*dias_t*fact

# sal_conserjes = 5000
# num_conserjes = 20

# tot_sal_conserjes = sal_conserjes* num_conserjes*fact

# gerente = 100000

# sub_gerentes = 45000
# num_subgerentes = 4
# tot_sal_sub = sub_gerentes*num_subgerentes

# sal_almacenista = 262.13
# num_almacenista = 40
# tot_sal_alm = sal_almacenista*num_almacenista*dias_t*fact

# g_pasillo = 264.65
# num_pasillos = 40
# tot_pasillo = g_pasillo*num_pasillos*fact

# nomina_tot = tot_sal_caj + tot_sal_conserjes + tot_sal_sub + gerente + tot_sal_sub + tot_sal_alm + tot_pasillo

# print(nomina_tot)
# gasto_luz = 120*2000*12*2.3
# print(gasto_luz)
# gastos_tot = gasto_luz+nomina_tot
# ingreso = gastos_tot + 1500000

# print(f"sigma = {sigma}, mu = {mu}, ingreso = {ingreso}")

# # omega =  norm.ppf(0.01)
# # print("This is omega", omega)
# # a_  = mu**2/(sigma**2 * omega**2)
# # b_ = -(2*mu*ingreso - omega**2 * sigma**2) / (sigma**2 * omega**2)
# # c_ = ingreso**2 / (sigma**2 * omega**2)

# # # Solving the quadratic equation
# # discriminant = b_**2 - 4 * a_ * c_
# # print(discriminant)
# # if discriminant >= 0:
# #     N1 = (-b_ + np.sqrt(discriminant)) / (2 * a_)
# #     N2 = (-b_ - np.sqrt(discriminant)) / (2 * a_)
# #     print(f"Possible values of N are {N1} and {N2}")
# # else:
# #     print("No real solutions")

# # porc_pob = N/160000
# # print(porc_pob)

# def equation(N):
#     Z = norm.ppf(0.99)
#     return (mu * N + Z * sigma * np.sqrt(N))**2 - ingreso**2

# valor_entrenado = ingreso/mu
# print("Trained N:", valor_entrenado)
# N = fsolve(equation, valor_entrenado)
# print("Estimated N:", N)

# poblacion = N/4
# porcentaje_poblacion = poblacion/40000
# print(f"Porcentaje de la población que debe visitar el supermercado: {porcentaje_poblacion}")

