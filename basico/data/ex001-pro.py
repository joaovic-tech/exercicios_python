from datetime import datetime, timedelta

actualDate = datetime.now()
twoDaysLater = actualDate + timedelta(2)

print(f"Data atual: {actualDate} \nProximo dia: {twoDaysLater}")
