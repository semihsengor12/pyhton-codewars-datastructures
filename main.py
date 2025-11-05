import threading
import os

def worker(thread_id):
    """Function to be executed by each thread."""
    print(f"Thread {thread_id} is starting.")
    # Simulate some work with a loop
    for i in range(20):
        print(f"Thread {thread_id} is working... {i+1}/5")
    print(f"Thread {thread_id} has finished.")

if __name__ == "__main__":
        # Create a list to hold the thread references
        threads = []
        
        # Start multiple threads
        for i in range(3):
            thread = threading.Thread(target=worker, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        print("All threads have completed.")