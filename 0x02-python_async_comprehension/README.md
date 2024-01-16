# 0x02. Python - Async Comprehension
- [0-async_generator.py](0-async_generator.py) - loops 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10
- [1-async_comprehension.py](1-async_comprehension.py) - collects 10 random numbers using an async comprehensing over async_generator, and returns the 10 random numbers