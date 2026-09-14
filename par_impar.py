def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


# --- Exemplo de uso ---
resultado = verificar_par_impar(7)
print(f"O número é: {resultado}")