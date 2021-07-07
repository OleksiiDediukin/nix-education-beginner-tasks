import string


def search_list_element(random_list, elem=777):
    for index in range(len(random_list)):
        if random_list[index] == elem:
            return index
        if index == 99:
            raise Exception("Element not found")


def generate_random_list(list_size):
    import random
    random_list = []
    for i in range(list_size):
        if random.random() > 0.5:
            random_list.append(random.randint(0, 1000))
        else:
            random_list.append(''.join(random.choice(string.ascii_lowercase) for _ in range(10)))
    return random_list


def main():
    random_list = generate_random_list(200)
    random_list.insert(10, 777)
    print(search_list_element(random_list))


if __name__ == '__main__':
    main()
