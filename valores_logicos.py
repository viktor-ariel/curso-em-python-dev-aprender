passaporte = True
comprada = True
menorDeIdade = False

print( (passaporte and comprada) and not menorDeIdade)
print((passaporte or comprada) and not menorDeIdade)
print( (not passaporte or comprada) and not menorDeIdade)
print((not passaporte or not comprada) and menorDeIdade)
print(passaporte and comprada and not menorDeIdade)