import threading

def run_A():
    print("Hello World from A")
    # do something
    barrier.wait()
    # do something else
    print("Hello World fromCc")

def run_B():
    barrier.wait()
    print("Hello World from B")
    # do something

barrier = threading.Barrier(2)
t1 = threading.Thread(target=run_A)
t2 = threading.Thread(target=run_B)
t1.start()
t2.start()
