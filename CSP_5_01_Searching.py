
import random
def randomSearch(items:list, target) -> int:

        tries = 0

        while True:
            tries += 1

            index = random.randint(0, len(items) - 1)

            if items[index] == target:
                print("Tries:", tries)
                return index


def linearSearch(items: list, target) -> tuple[int, int]:
    checks = 0

    for i in range(len(items)):
        checks += 1

        if items[i] == target:
            return (i, checks)

    return (-1, checks)

def binarySearch(items: list, target) -> tuple[int, int]:
    left = 0
    right = len(items) - 1
    checks = 0

    while left <= right:
        mid = (left + right) // 2
        checks += 1  

        if items[mid] == target:
            return (mid, checks)
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return (-1, checks)

#linear search
#best = 1
#worst = 15

#binary
#best = 1
#worst = 4

#code checklist
#target
#-stop : len(list) - 1
#-start : 0
#-list
#1 missing
