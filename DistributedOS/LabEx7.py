import threading

# Create two locks
lock1 = threading.Lock()
lock2 = threading.Lock()

# Function representing the first thread's task
def thread1_task():
    print("Thread 1 trying to acquire lock 1")
    lock1.acquire()
    print("Thread 1 acquired lock 1")
    
    # Introducing delay to increase the chances of deadlock
    import time
    time.sleep(1)
    
    print("Thread 1 trying to acquire lock 2")
    lock2.acquire()
    print("Thread 1 acquired lock 2")
    
    # Do some work
    
    # Release locks
    lock2.release()
    print("Thread 1 released lock 2")
    lock1.release()
    print("Thread 1 released lock 1")

# Function representing the second thread's task
def thread2_task():
    print("\nThread 2 trying to acquire lock 2")
    lock2.acquire()
    print("Thread 2 acquired lock 2")
    
    # Introducing delay to increase the chances of deadlock
    import time
    time.sleep(1)
    
    print("\nThread 2 trying to acquire lock 1")
    lock1.acquire()
    print("Thread 2 acquired lock 1")
    
    # Do some work
    
    # Release locks
    lock1.release()
    print("Thread 2 released lock 1")
    lock2.release()
    print("Thread 2 released lock 2")

# Create and start both threads
thread1 = threading.Thread(target=thread1_task)
thread2 = threading.Thread(target=thread2_task)
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads finished execution")
