def convert_to_uppercase(strings_list, word="price"):
    if not isinstance(strings_list, list):
        raise TypeError(f"Type of arg must be {type(list)}")
    return [elem.upper() if word in elem else elem for elem in strings_list]


def main():
    print(convert_to_uppercase(["high price", "text without necessary word", "price"]))


if __name__ == '__main__':
    main()
