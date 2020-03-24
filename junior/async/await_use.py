import asyncio


async def sum(x, y):
    print('x + y => {0} + {1}'.format(x, y))
    await asyncio.sleep(2)
    return x + y

async def get_sum(x, y):
    ret = await sum(x, y)
    print('ret is {}'.format(ret))
    return ret


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_sum(2,3))
    loop.close()
