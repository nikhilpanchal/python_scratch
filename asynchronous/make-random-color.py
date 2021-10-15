import asyncio
import random

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def make_random(idx: int, threshold: int = 6) -> int:
    print(c[idx+1], "Initiated make_random {}".format(idx))

    i = random.randint(0, 10)
    while i<threshold:
        print(c[idx+1], "Number not big enough, try again")
        await asyncio.sleep(idx+1)
        i = random.randint(0, 10)

    print(c[idx+1], "Finished: make_random({}, {}) == {}".format(idx, threshold, i))
    print(c[0])

async def main():
    res = await asyncio.gather(*(make_random(idx, 10-idx-1) for idx in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print("r1: {}, r2: {}, r3: {}".format(r1, r2, r3))