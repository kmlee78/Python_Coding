import asyncio
from asyncio import shield
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def time_consumed(func):
    def wrapper():
        start = time.time()
        res = func()
        print(time.time() - start, "seconds consumed")
        return res

    return wrapper


async def return_value(value):
    await asyncio.sleep(5 - value)
    return value


async def five_seconds():
    await asyncio.sleep(5)


async def factorial(name, number):
    result = 1
    for i in range(2, number + 1):
        print(f"Task [{name}]: Currently on process {result} X {i}")
        await asyncio.sleep(1)
        result *= i
    print(f"Task [{name}]: Result = {result}")


async def is_prime(value):
    divisor = value // 2
    await asyncio.sleep(10 - value)
    for i in range(2, divisor + 1):
        if value % i == 0:
            print(f"{value} is not a prime")
            return
    print(f"{value} is a prime")


async def main_task():
    logger.info("Prime test code starts")
    task1 = [is_prime(x) for x in range(2, 8)]  # 8초 <- main consumed time!
    task2 = asyncio.create_task(is_prime(9))  # 1초
    task3 = asyncio.create_task(is_prime(8))  # 2초
    await asyncio.gather(*task1)
    await task2
    await task3
    logger.info("Prime test code ends\n")

    logger.info("Factorial test code starts")
    await asyncio.gather(
        factorial("A", 3),  # 2초
        factorial("B", 4),  # 3초
        factorial("C", 5),  # 4초 <- main consumed time!
    )
    logger.info("Factorial test code ends\n")

    logger.info("Timeout test code starts")
    task_deprecate = asyncio.wait_for(five_seconds(), timeout=3)
    try:
        await task_deprecate  # 3초 <- main consumed time!
    except asyncio.TimeoutError:
        print("Timeout has occured")
    logger.info("Timeout test code ends\n")

    logger.info("Coroutine iterator test code starts")
    aws = [return_value(x) for x in range(1, 4)]
    for coro in asyncio.as_completed(aws):
        result = await coro  # 4초 <- main consumned time!
        print(f"{result} has returned")
    logger.info("Coroutine iterator test code ends\n")


@time_consumed
def main():
    asyncio.run(main_task())


if __name__ == "__main__":
    main()


"""
<Print result>

INFO:root:Prime test code starts
9 is not a prime
8 is not a prime
7 is a prime
6 is not a prime
5 is a prime
4 is not a prime
3 is a prime
2 is a prime
INFO:root:Prime test code ends

INFO:root:Factorial test code starts
Task [A]: Currently on process 1 X 2
Task [B]: Currently on process 1 X 2
Task [C]: Currently on process 1 X 2
Task [A]: Currently on process 2 X 3
Task [B]: Currently on process 2 X 3
Task [C]: Currently on process 2 X 3
Task [A]: Result = 6
Task [B]: Currently on process 6 X 4
Task [C]: Currently on process 6 X 4
Task [B]: Result = 24
Task [C]: Currently on process 24 X 5
Task [C]: Result = 120
INFO:root:Factorial test code ends

INFO:root:Timeout test code starts
Timeout has occured
INFO:root:Timeout test code ends

INFO:root:Coroutine iterator test code starts
3 has returned
2 has returned
1 has returned
INFO:root:Coroutine iterator test code ends

19.016084909439087 seconds consumed
"""
