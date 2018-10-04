import threading
import time

# class my_thread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         pass
#     def run(self):
#         print(threading.current_thread().getName() + ", enter")
#         time.sleep(5)
#         print("my_thread is running !")
# my_thread().start()

def worker():
    print(threading.current_thread().getName() + ", i only wanner to sleep 3 seconds!")
    # time.sleep(5)

    try:
        raise InterruptedError(threading.current_thread().getName() + " is error !")
    except Exception as e:
        print(e)
    finally:
        print("finally is execute")
    print(threading.current_thread().getName() + ", 3 seconds is over! i am running!")

print(threading.current_thread().getName() + ", i am main thread !")
tt = threading.Thread(target=worker, name="worker")
tt.start()
time.sleep(5)
print(threading.current_thread().getName() + ", i am over, but worker thread is sleeping, that gay is so lazy !")