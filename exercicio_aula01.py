# Exercício 1:

# Escreva um expressão em função de uma incógnita nota que resulte em True caso nota esteja no intervalo aberto (3.0, 5.0), e resulte em False caso contrário.

nota = 4

if 3.0 <= nota <= 5.0:
    nota = True
else:
    nota = False
    
print(nota)

# Exercício 2:

# Um ano bissexto ocorre aproximadamente a cada 4 anos. 
# # Escreva uma expressão (em função de uma incógnita ano) que resulte em True caso ano seja bissexto e False caso contrário. Para ser bissexto, o valor de ano precisa ser múltiplo de 4, exceto múltiplos de 100 que não são múltiplos de 400. Assim o ano de 2020 é bissexto pois satisfaz todas essas condições.

ano = 2020

if ano % 4 == 0:
    resultado = True
else:
    resultado = False
    
print(resultado)