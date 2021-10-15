import asyncio

async def count():
    print("One")

    # Give up the CPU so that something else can be scheduled to run
    # Control is passed back to the event loop, which will schedule something else
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())
    print("Everyone is done")


def scratch():
    import time
    time.perf_counter()


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print("{} executed in {} seconds".format(__file__, elapsed))