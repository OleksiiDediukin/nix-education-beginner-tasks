def difference(first_list, second_list):
    lists_difference = list(set(first_list).difference(second_list))
    return lists_difference


def main():
    print(difference([1, 2, 3, 4, 5], [1, 3, 4]))


if __name__ == '__main__':
    main()
