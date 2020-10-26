# Asynchronous Programming

*A style of concurrent programming where tasks release the CPU during waiting periods so that other tasks can use it*

- Achieves speed through *efficient use of the CPU*, by seeking to reduce (or eliminate) CPU `wait-time`
- Does not involve any additional (magical) fire-power added to the CPU
- Can be achieved with a single process and a single thread

## Cooperative Multi-tasking

* Async frameworks use a scheduler, also called `event loops`
* The loop keeps track of all running tasks and is responsible for scheduling tasks to run on the CPU
* When a function is suspended, control returns to the loop which then finds another task to execute(start/resume) on the CPU
* Old Idea: Is how JS code runs on a Javascript engine

## Pitfalls

* You can't have long running CPU-intensive work, or blocking
    * examples of these are blocking network calls, or long running calculations
    * Doing so will starve the other tasks from CPU time. That's why tasks in general must give up the CPU for other tasks to run (be good cooperative citizens)
* All async frameworks provide non-blocking replacement functions for common blocking calls
    * Network calls and such

## Comparisons
|Criteria|Processes|Threads|Async|
|-|-|--|-|
|Managed By|OS|OS|Application Code (OS Ignorant)|
|Execution Mode|Preemptive|PreEmptive|Cooperative|
|Use all CPU Cors|Yes|Yes|No|
|Scalability|Low(tens)|Medium(Hundreds)|High(Thousands)|
|Can run blocking calls|Yes|Yes|No|

## When to use Async
- When you need massive scaling
- You don't have a lot of blocking calls

## References
- [PyCon talk on Async](https://www.youtube.com/watch?v=iG6fr81xHKA)