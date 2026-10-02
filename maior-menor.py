def encontrar_o_maior_e_menor(numeros):
    if not numeros:
        return None, None 

    maior = max(numeros)
    menor = min(numeros)

    return maior, menor

lista_numeros = [15,99,2,45,6,32,8,]

maior_num,menor_num = encontrar_o_maior_e_menor(lista_numeros)

print(f"Lista: {lista_numeros}")
print(f"O maior número é: {maior_num}")
print(f"O menor número é: {menor_num}")