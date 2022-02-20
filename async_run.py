import time
import multiprocessing as mp

def show_current_time():
    while True:
        t = time.strftime("%H:%M:%S")
        print("Текущее время:", t)
        time.sleep(1)

def show_message():
    while True:
        print("(* ^ ω ^)")
        time.sleep(3)

if __name__ == "__main__":
    p1 = mp.Process(target=show_current_time)
    p2 = mp.Process(target=show_message)

    # метод start() запускает наш процесс (функцию)
    p1.start()
    p2.start()

    # метод join() дожидается окончания нашего процесса (функции)
    p1.join()
    p2.join()