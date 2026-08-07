from datetime import datetime, timedelta

data_atual = datetime.now()(input("Digite a data atual"))
data_futura = data_atual + timedelta(2)
data_anterior = data_atual + timedelta(-1)

# print(data_futura)
#print(data_atual)
print(data_anterior)
