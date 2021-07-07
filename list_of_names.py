def splitting_names_string(names_string):
    list_of_names = [name.strip() for name in names_string.split(',')]
    return list_of_names


def main():
    print(splitting_names_string("Денис, Олег, Вася, Петя,Дима,Женя"))


if __name__ == '__main__':
    main()
