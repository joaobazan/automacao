from datetime import datetime

data_atual = datetime.now()
data_brasileira = data_atual.strftime("%d/%m/%Y")

#print(data_atual)
print(data_brasileira)