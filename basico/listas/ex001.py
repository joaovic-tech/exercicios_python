def main():
    scores = []

    for i in range(1, 5, 1):
        scores.append(int(input(f"Digite a {i}º nota: ")))

    average = sum(scores) / len(scores)
    biggerScore = max(scores)
    smallerScore = min(scores)

    print("-" * 30)
    print(f"A média do aluno é {average:.0f}")
    print(f"A sua maior nota foi {biggerScore}")
    print(f"E a menor foi {smallerScore}")


if __name__ == "__main__":
    main()
