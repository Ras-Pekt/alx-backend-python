# 0x01. Python - Async
- [0-basic_async_syntax.py](0-basic_async_syntax.py) - takes in an integer argument, max_delay, waits for a random delay between 0 and max_delay seconds and eventually returns it
- [1-concurrent_coroutines.py](1-concurrent_coroutines.py) - takes in 2 int arguments: n and max_delay, spawns wait_random n times with the specified max_delay, and returns the list of all the delays in ascending order without using sort()
- [2-measure_runtime.py](2-measure_runtime.py) - takes 2 int argument: n and max_delay and measures the total execution time for wait_n(n, max_delay), and returns a float, total_time / n
- [3-tasks.py](3-tasks.py) - takes an integer max_delay and returns a asyncio.Task
- [4-tasks.py](4-tasks.py) - altered wait_n it into a new function task_wait_n that calls task_wait_random