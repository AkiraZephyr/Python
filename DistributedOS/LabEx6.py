import threading

# Global variable shared by threads
counter = 0

# Lock for synchronization
lock = threading.Lock()

# Function to be executed by each thread
def increment():
    global counter
    for i in range(1000000):
        # Acquire the lock
        lock.acquire()
        counter += 1
        # Release the lock
        lock.release()

# Create two threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final value of the counter
print("Final counter value:", counter)