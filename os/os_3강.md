# Process

## Process Control Block

> 프로세스 마다 다양한 프로세스와 관련된 정보를 운영체를 관리하고 있는데 이러한 정보를 Process control Block 이라고 한다.



- Identifiers
  - Identifier of this process
  - Identifier of the process that created this process (parent process)
  - User Identifier
- Processor State Information
  - User-Visible Regitsters 
  - Control and Status Registers
    - Program counter : 다음 실행 할 명령의 주소
    - Condition codes
    - Status information
  - Stack Pointers
- Scheduling and State Information
- Data Structuring - tree
- Interprocess Communication - signal
- Process Privileges -> 사용자, kernel
- Memory Management - 논리적인 segment -> physical 메모리 page
- Resource Ownership and Utilization - 어떤 process가 어떤 resource를 가지고 있는지
  - 동시에 사용하면 안된다



## Program Status Word

> Contains condition codes and other status information of the currently running running process

- Examples: EEFLAGS register on Intel x86 processors



## Two- state Process Model

- A process may be in one of two states
  - running
  - Not running



## Queuing Diagram



## Process Creation and Termination

- Process spawning
  - OS may create a process at the explicit request of another process
    - A new process becomes a child process of the parent process
- Process termination
  - A process may terminate itself by calling a system call called EXIT
  - A process may terminate due to and erroneous condition such as memory unavailable, arithmetic error, or parent process termination, etc.



## fork: Creating new processes

- Process control
  - Unix provides a number of system calls for manipulating processes
  - Obtain Process ID, Create/Terminate Process, etc.



- fork
  - Creates a new process (child process) that is identical to the calling process (parent process)
  - Returns 0 to the child process
  - Returns child's pid to the parent process
  - Parent and child both run the same code
    - Distinguish parent from child by return value from fork
  - Duplicate but separate address space
    - Start with same state, but each has private copy



## exit: Destroying Process



- exit
  - Terminate a process with an exit status
- *atexit()* registers functions to be executed upon exit
  - 나 죽을때 실행시킬 명령 지정



## Five-State Process Model

- New - admit
- Ready - dispatch
- Running - timeout, event wait, release
- Blocked - event occurs
- Exit



## Reason for Process Creation

- New batch job
- Interactive logon
- Created by OS to provide a service
- Spawned by existing process 



## Suspended Processes

- Swapping
  - Sometimes, all the processes in memory are waiting for I/O
  - Involves moving part or all of a process from main memory to disk
  - Then, OS brings in another process into memory
- Suspended Process
  - The process is swapped out and is not immediately available for execution
  - The process was placed in a suspended state by an agent, either itself, a parent process, or the OS, for the purpose of preventing its execution
  - The process may or may not be waiting on an event



## Interrupts

> 비슷하지만 다르다.
>
> 둘 다 예외적인 상황이 발생한 것



- Exception : 현재 실행중인 프로세스에서 예외적인 상황이 발생 / Internal error, Synchronous
  - Traps : Debugging, System call
  - Faults
  - Aborts
- Interrupt : 외적인 상황 / Asynchronous, external events
  - 키보드
  - hardware reset