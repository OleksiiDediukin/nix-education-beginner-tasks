def splitting_of_list(arr, num):
    if not isinstance(num, int):
        raise TypeError(f"Type of variable num must be {int}")
    if len(arr) < num:
        raise Exception("Array length must be greater or equal to the number of splits")
    
    splitting_list = [arr[i:i+len(arr)//num] for i in range(0, len(arr)-len(arr) % num, len(arr)//num)]
    splitting_list[-1].extend(arr[len(arr) - len(arr) % num:])
    return splitting_list


def main():
    print(splitting_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))


if __name__ == '__main__':
    main()
