print(*sorted([input() for _ in range(int(input()))],
        key=lambda x: int(x.split(".")[0]) * (256 ** 3) + int(
            x.split(".")[1]) * (256 ** 2) + int(x.split(".")[2]) * (
                          256 ** 1) + int(x.split(".")[3])),sep="\n")
