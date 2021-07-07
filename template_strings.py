def print_name_surname(name="Unknown", surname="Unknown"):
    print(f"New user registered. Name: {name}, surname: {surname}")
    print("He introduced himself as {name} {surname}".format(name=name, surname=surname))
    print("On the web, it is known as {} {}".format(name, surname))
    print("On Facebook, he is signed as {0} {1}".format(name, surname))


def main():
    print_name_surname()


if __name__ == '__main__':
    main()
