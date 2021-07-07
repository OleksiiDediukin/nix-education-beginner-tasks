def joining_of_strings(strings_list):
    if not isinstance(strings_list, list):
        raise TypeError(f"Arg must be {list}")
    return ','.join(strings_list)


def main():
    print(joining_of_strings(["first string", "second string", "third string"]))


if __name__ == '__main__':
    main()