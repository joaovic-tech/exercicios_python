def main():
    scores = []

    for i in range(1, 5, 1):
        scores.append(float(input(f"Digite a {i}º nota: ")))

    average = sum(scores) / len(scores)

    print("-" * 30)
    print(f"A média do aluno é {average:.0f}")

    if average >= 7:
        print("Aprovado!")
        return

    scores.append(float(input(f"Digite a nota da prova final: ")))

    average = sum(scores) / len(scores)
    if average >= 5:
        print("Aprovado!")
    else:
        print("Reprovado!")

    print(f"Média final foi {average}")


if __name__ == "__main__":
    main()
