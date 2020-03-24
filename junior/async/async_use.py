import time, asyncio


async def wait(wait_time):
    print('等待时间 {0} 秒'.format(wait_time))
    time.sleep(wait_time)


if __name__ == '__main__':
    print(asyncio.iscoroutinefunction(wait))
    print('*' * 20)
    coroutine = wait(2)
    loop = asyncio.get_event_loop()
    task = loop.create_task(coroutine)
    print(task)
    loop.run_until_complete(task)
    print(task)
