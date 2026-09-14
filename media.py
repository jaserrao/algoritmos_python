n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
n3 = float(input('Terceira nota:'))

media = (n1 + n2 + n3) / 3
print(f'Média: {media:2f}')
if media >= 7:
    print('Aprovado!')
elif media >= 5:
    print('Recuperação!')
else:
    print('Reprovado!')