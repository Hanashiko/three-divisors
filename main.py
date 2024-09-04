from typing import List

def get_devisors(n: int):
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            yield i
    yield n

def isThree(n: int) -> bool:
    devisors: List[int] = list(get_devisors(n))
    return len(devisors) == 3

def main() -> None:
    print(isThree(2))
    print(isThree(4))
    print(isThree(12))
    
if __name__ == "__main__":
    main()