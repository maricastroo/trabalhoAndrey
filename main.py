#link site de apoio para uso do lambda https://www.covildodev.com.br/artigo/funcao-lambda-python

# Funções f(x) e g(x) 
f = lambda x: x**1    #lambda criar função sem dar um nome para ela
g = lambda x: x - 69

# Valor de x para calcular as composições
x = 6969

# Calcula as composições diretamente e exibe os resultados
resultado_g_f = g(f(x))
resultado_g_g = g(g(x))
resultado_f_f = f(f(x))
resultado_f_g = f(g(x))

# Exibe os resultados
print("(g ∘ f)(x) =", resultado_g_f)
print("(g ∘ g)(x) =", resultado_g_g)
print("(f ∘ f)(x) =", resultado_f_f)
print("(f ∘ g)(x) =", resultado_f_g)
