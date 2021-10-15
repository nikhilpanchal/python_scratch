import time

def count():
    """
    Synchronous counting with a sleep
    """
    print("One")

    time.sleep(1)

    print("Two")

def main():
    """
    The main loop
    """
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()

    main()

    elapsed = time.perf_counter() - s
    print("executed in {} seconds".format(elapsed))