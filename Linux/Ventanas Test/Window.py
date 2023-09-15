import tkinter as tk
import asyncio
import threading
int n=0
async def async_task():
    # Your asynchronous task goes here
    n+=1
    print(n)
    await asyncio.sleep(2)  # Simulated async task

def main_window():
    root = tk.Tk()
    # Your GUI creation code goes here
    
    def start_async_task():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(async_task())

    # Start the asynchronous task in a separate thread
    async_thread = threading.Thread(target=start_async_task)
    async_thread.start()

    root.mainloop()

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    main_window()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
