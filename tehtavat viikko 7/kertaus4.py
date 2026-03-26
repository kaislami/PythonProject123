def kuusi(koko):
    print("Tämä on kuusi!")
    for i in range(1, koko + 1):
        rivin_tahdet = "*" * (2 * i - 1)
        print(rivin_tahdet.center(2 * koko - 1))
    print("*".center(2 * koko - 1))
kuusi(5)