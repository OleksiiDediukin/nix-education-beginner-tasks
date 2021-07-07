def rounding_of_num(num):
    if type(num) not in [int, float]:
        raise TypeError("Type of num must be float or int")
    rounded_num = round(num, 2)
    return rounded_num


def main():
    print(rounding_of_num(22.32131))
    print(rounding_of_num(58.66625))
    print(rounding_of_num(14.0))


if __name__ == '__main__':
    main()
