from datetime import datetime


def hasZero(num):
    if num < 10:
        return f"0{num}"
    else:
        return num


actualDate = datetime.now().date()
twoDaysLater = f"{actualDate.year}-{hasZero(actualDate.month)}-{actualDate.day + 2}"

print(f"Data atual: {actualDate} \nProximo dia: {twoDaysLater}")
