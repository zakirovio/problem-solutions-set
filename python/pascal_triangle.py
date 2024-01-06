from typing import List


def create_sublist(lst: List[int]):
    sublist = [1]

    for i in range(len(lst)):
        if i + 1 == len(lst):
            break
        sublist.append(lst[i] + lst[i + 1])

    sublist.append(1)
    return sublist


def get_pascal_row(n: int) -> List[int]:
    for i in range(0, n + 1):
        if i == 0:
            arr.append([1])
        elif i == 1:
            arr.append([1, 1])
        else:
            arr.append(create_sublist(arr[i - 1]))

    return arr[n]


if __name__ == "__main__":
    arr = []
    num = int(input("Input row's number: "))
    print(get_pascal_row(num))
