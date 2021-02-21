# 운영체제의 역사

> serial -> simple batch -> multiprogrammed batch -> time-sharing

## Simple Batch Systems

> one by one

- Monitor
  - User submits the job on cards or tape to a computer operator, who batches them together sequentially and places them on an input device
  - Monitor is a resident software in main memory
  - Monitor reads in jobs one at a time from the input device
  - The current job is placed in the user program area
  - The control is passed to the job
  - When the job is completed, it returns control to the monitor



- I/O devices are slowcompared to processor
  - 프로세서가 가장 비싼데, 프로세서의 사용 효율성이 너무 떨어진다.



## Multiprogrammed Batch System

> 프로세서를 쉬지 않게 돌리자
>
> Known as Multitasking



- When one job needs to wait for I/O, the processor can switch to the other job, which is likely not waiting for I/O
- Memroy can be expanded to hold three, four, or more programs
- Sample Program Execution Attributes
  - Job1 : 주로 computation
  - Job2 : 주로 I/O 처리, terminal
  - Job3 : 주로 I/O 처리, disk, printer



## Time-Sharing Systems



- Can be used to handle multiple interactive jobs
- OS interleaves the execution of each user program in time *slice*
  - 주어진 시간이 지나면 다른 프로그램을 실행 -> 연산이 비교적 짧은 것은 빠르게 끝내자
    - 진행중이던 프로그램을 종료하면서 중지된 상태를 저장
- 매번 context switching이 발생할 때마다 disk I/O이 발생하기 때문에 overhead가 굉장히 큰 시스템
  - 요즘 time sharing system에서는 여러 job이 동시에 올라간다.



## Process 란?

- Definition : A process is an instance of a program in execution.
  - Not the same as **"program" or "processor"**
  - **process** vs **program**
  - program : 컴퓨터 디스크에 저장되어 있는 실행가능한 파일, 정적.
  - program을 더블클릭해서 실행하는 순간 그것은 process
    - 같은 인터넷 브라우저를 여러번 실행시키면 실행된 브라우저들은 각각 다른 instance (process)
-  Process provides two key abstractions
  - Logical control flow
    - each process has an exclusive use of the processor
  - Private address space
    - each process has an exclusive use of private memory
- How are these illusions maintained?
  - Multiprogramming : process executions are running on the system
  - Virtual Memory : OS provides a private space for each process
    - 각 프로세스가 독립적으로 원하는 만큼의 virtual memory를 제공
    - 실제로 virtual memory는 physical memory와 disk에 의해서 OS가 알아서 관리한다.



## Private Address Spaces

- Each process has its own private address space.



## Context switching

- Processes are managed by OS code called the *kernel*
- User mode and kernel mode
  - If the mode bit is set, the process is running in **kernel** mode (supervisor mode), and can execute any instruction and can access any memory location - (clock interrupt -> exception)
  - If the mode bit is not ste, the processs is running in **user** mode and is not allowed to execute privileged instructions