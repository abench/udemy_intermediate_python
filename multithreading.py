# Practice Activity: Multithreading
#
# This is a simple practice activity to help you learn the concepts better. We're going to keep these activities brief so that you can do them quickly. Remember to post in the Q&A forums if you have any problem at all. I'm here to help.
#
# Here's your task:
#
# You need to simulate a simple ATM machie for withdrawl of cash. Here's the process.
#
# - Create a global variable called balance.
#   Set its initial value to 10,000.
#   This is the customer's starting balance.
#
# - Create a function that simulates withdrawl of $10.
#   For this purpose, the function must first retrieve the value of the global variable balance.
#   Then, it must check if the balance is more than or equal to 10.
#   If the balance isn't sufficient, the function should simply return.
#   If it is sufficient, the function sleeps for a second
#   to simulate the ATM machine counting cash.                                                                                                                                                                                                                                  '' \
#
#
# After that, the function must subtract 10 from the global variable balance.
#
# - In the main code, create 1,010 threads -- each running the withdrawl function we wrote above.
#   Make sure you start all threads first.
#   After all threds have been started, join them so that we wait until they are done processing.
#
# - Print the final balance and see if the balance is equal to 0 or if it has gone in the negative.
#   (Don't worry if the balance goes in the negative as we will fix this later.)
#                                                                                                                                                                                                           '

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


