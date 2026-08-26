#----------------------------Chapter 11: Concurrency - Threading,Multiprocessing & asyncio------------------
#since python is a single core language it runs in single core in a synchronus way, one after another step
#even there is a octa core processor in your system python only uses single core because of GIL(Global Interpretor Lock)
#here GIL locks each thread and executes one after other by releasing the one lock at a time this will helps
#to tackle the race conditions 
#Modern technologies now a days uses multithreading for example in web development we need to handle multiple 
#API calls at the movement or runs multiple apis at once including data base queries this process gets slow
#in single threaded (syncronous) so multi threading is used one or more threads for individual tasks

#The Global Interpreter Lock (GIL)
#GIL is a mutex(lock) in cpython which locks the threads, allows only one thread in one core is being used even 
#in a multicore cpu
#GIL avoid race condition issues
#GIL makes runs threads like a multi threading while waiting for I/O operations that takes time 
#GIL release the lock for other thread and start shifting the threads multiple times with very short period of
#time makes the parellelism but it is not a actual parellelism

#Threading - I/O-Bound Parallelism
#concurrent.futures was a built in module in python which is useful to implement the parallel execution of threads
#here ThreadPoolExecutor is a method from concurrent.futures which handles the thread creation and joining of
#threads together 
#Futures object is a promise object which states that the result will appear init after the thread executions
#as_completed function is used  to give the results from the future object that was decleared when thread starts
#as_completed returns the result of completed threads just after execution of that thread
print("*"*25+" concurrent.futures "+"*"*25)
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
def slow(name,duration):
    time.sleep(duration)
    print(f"the process {name} took {duration}s of time")

tasks=[('task1',4),('task2',2)]
start=time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as Executor:
    futures = {Executor.submit(slow,d,f):f for d,f in tasks}
    for future in as_completed(futures):
        future.result()
elapsed = time.perf_counter()-start
print("total time took:",round(elapsed,2),'s')

#Thread Locking is a technique that locking the variable which that only the current one thread at once can access
#the variable at that time so it solves the race conditions due to multiple threads 
import threading

count=0
lock=threading.Lock()
def counter():
    global count
    with lock:
        count+=1

threads=[threading.Thread(target=counter) for _ in range(1000)]
for t in threads:
    t.start()
for j in threads:
    j.join()
print(count)

#Multiprocessing — CPU-Bound Parallelism
from concurrent.futures import ThreadPoolExecutor
import math
def is_prime(number):
    if number<2:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number%i ==0:
            return False
    return True

numbers=list(range(100))
with ThreadPoolExecutor() as executor:
    results=list(executor.map(is_prime,numbers))
primes = [(n,p) for n,p in zip(results,numbers)]
print(len(primes),' : ',primes)

#asyncio — High-Concurrency I/O (Single Thread)
#asyncio is a python builtin module useful to provide the concurrency using a single thread that waits 
#until async functionalities completes the execution
import asyncio
async def fetch(url,delay):
    print("Fetching the url......",url)
    await asyncio.sleep(delay)
    return f"url {url} is fetched successfully"

async def main():
    result=await asyncio.gather(
        fetch('api1',3),
        fetch('api2',2),
        fetch('api3',5))
    for r in result:
        print(r)
asyncio.run(main())

#async/await Rules
#async def creates a coroutine function which we will define the await process async function waits until 
#await completes the execution then further instructions were executed
#await should always inside the async def function
#asyncio.run() is the entry point were the execution starts at the top most layer
#tasks are run concurrently so we use gather() function or TaskGroup to group the tasks
#results of the group tasks lies in tasks.result()
async def my_conc(TaskName):
    print("this is inside of async function")
    await asyncio.sleep(2)
    print("this statement is after sleeping the process for 2 sec")
    return TaskName

async def main():
    result=await asyncio.gather(
        my_conc('task1'),
        my_conc('task2'),
        my_conc('task3')
    )
    for i in result:
        print(i)

asyncio.run(main())