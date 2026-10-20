import asyncio
import time

async def get_data(delay = 1):
    print("Начали получение")

    await asyncio.sleep(delay)

    print("Данные готовы")
    return f"результат {delay}"


async def main():
    result = await get_data()
    print(result)
    await asyncio.sleep(1)  

asyncio.run(main())

print("Все")

#конкурентность
async def main2():
  result = await asyncio.gather(
    get_data(1),
    get_data(2)
  ) # ~2 sec, результат в порядке переданных вызовов, кокурентное выполнение

  # планировка в цикле событий
  task1 = asyncio.create_task(get_data(1))
  task2 = asyncio.create_task(get_data(2))

  await task1
  await task2

asyncio.run(main2())


#to_trhead

def sync(delay):
  time.sleep(delay) # блокирующее ожидание, блокирует весь поток


async def main3():
  result = await asyncio.gather(
    asyncio.to_thread(sync(1)), # полезно для io-bound т.к. GIL - интерпритатор на 1 поток только работает
    asyncio.to_thread(sync(2))
  ) # ~2 sec 