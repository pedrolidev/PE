from datetime import datetime

def data_por_extenso(date_str):
    try:
        data = datetime.strptime(date_str, '%d-%m-%Y')
        data_formatada = data.strftime('%d de %B de %Y')
        return data_formatada
    except ValueError:
        return None

data_input = input("Digite a data de maneira em que seja identificada por DD/MM/AAAA")
data_extenso = data_por_extenso(data_input)
if data_extenso:
    print("A data por extenso é: {data_extenso}")
else:
    print("Essa data é inválida.")