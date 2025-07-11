scores = []

for i in range(1, 5):
    scores.append(float(input(f"Digite a {i}º nota: ")))

average = sum(scores) / len(scores)
print(f"A media final: {average}")
 