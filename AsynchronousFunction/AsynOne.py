import asyncio


"""
This code defines an asynchronous function named async_function that takes two
parameters: name (a string representing the task's name) and seconds (an integer representing the sleep duration). 
The function prints a message indicating the start of the task, then asynchronously sleeps for the specified number 
of seconds using asyncio.sleep, and finally prints a message indicating the end of the task.
"""

async def async_function(name, seconds):
    print(f"Start {name}")
    await asyncio.sleep(seconds)
    print(f"End {name}")

q = input("enter your name: ")



"""
 The main function is also asynchronous. It uses asyncio.gather to run multiple asynchronous 
 functions concurrently. In this case, it gathers the results of calling async_function with different parameters.
"""


async def main():
    # Using asyncio.gather to run multiple asynchronous functions concurrently
    await asyncio.gather(
        async_function("Task 1", 1),
        async_function("Task 2", 2),
        async_function("Task 3", 3)
    )

# Run the asynchronous code using the event loop
# if __name__ == "__main__":
asyncio.run(main())

