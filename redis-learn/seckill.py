# 实现秒杀功能
import redis, random
from colorama import Fore, Style
from redis_db import pool
from concurrent.futures import ThreadPoolExecutor


# 初始化秒杀数据字段
def init_seckill_keys():
    try:
        con = redis.Redis(connection_pool=pool)
        con.delete('kill_total', 'kill_num', 'kill_flag', 'kill_user')
        con.set('kill_total', '50')
        con.set('kill_num', '0')
        con.set('kill_flag', '1')
        con.expire('kill_flag', 600)
    except Exception as e:
        print(Fore.LIGHTRED_EX, 'init_seckill_keys error: ', e)
        print(Style.RESET_ALL)
    finally:
        if con: del con


# 秒杀线程函数
def seckill_foo():
    try:
        user_id = random.randint(1000, 10000)
        con = redis.Redis(connection_pool=pool)
        if con.exists('kill_flag') != 1: return
        pipline = con.pipeline()
        pipline.watch('kill_user', 'kill_num')
        print(pipline.get('kill_num').decode('utf-8'), pipline.get('kill_total').decode('utf-8'))
        if int(pipline.get('kill_num').decode('utf-8')) < int(pipline.get('kill_total').decode('utf-8')):
            pipline.multi()
            pipline.incr('kill_num')
            pipline.rpush('kill_user', user_id)
            pipline.execute()
    except Exception as e:
        print(Fore.LIGHTRED_EX, 'seckill_foo error: ', e)
        print(Style.RESET_ALL)
    finally:
        if pipline: pipline.reset()
        if con: del con

# 主函数
def main():
    init_seckill_keys()
    executor = ThreadPoolExecutor(200)
    for i in range(1000):
        executor.submit(seckill_foo)
    print(Fore.LIGHTGREEN_EX, '\n秒杀结束!')
    print(Style.RESET_ALL)


if __name__ == '__main__':
    main()

