# Practice Activity: Asynchronous Programming
#
# Continue from the previous practice activity.
# Change your code to use asyn functions instead of threads.
# Create an even loop just as we did in the video --
# you will just need to change the function body itself.
#
# Note: When you are doing async functions,
# you cannot use time.sleep(1).
# Instead, you should use:  await asyncio.sleep(1)


import time
import threading
balance = 10000

lock = threading.Lock()

def withdrawl():
    global balance, lock
    with lock:
        v =  balance
        if v >= 10:
            time.sleep(0.001)
            v = v - 10
            balance = v
    return

if __name__ == "__main__":
    thread_list = []
    for i in range(1100):
        t = threading.Thread(target=withdrawl)
        thread_list.append(t)
        t.start()


    for i in thread_list:
        i.join()
    print("Balance: {}".format(balance))


