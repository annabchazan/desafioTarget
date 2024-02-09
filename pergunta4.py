sp = 67836.43
rj = 36678.66
mg = 29229.86
es = 27165.53
outros = 19849.53

valor_mensal = sp + rj + mg + es + outros

porcentagem_sp = (sp *100)/ valor_mensal
porcentagem_rj = (rj *100)/ valor_mensal
porcentagem_mg = (mg *100)/ valor_mensal
porcentagem_es = (es *100)/ valor_mensal

print(f" São Paulo representa {porcentagem_sp}%")
print(f" Rio de Janeiro representa {porcentagem_rj}%")
print(f" Minas Gerais representa {porcentagem_mg}%")
print(f"Espírito Santo representa {porcentagem_es}%")