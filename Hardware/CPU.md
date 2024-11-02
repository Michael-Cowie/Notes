# What is a CPU?

The **Central Processing Unit (CPU)**, often referred to as the "brain" of the computer, is a crucial component responsible for executing instructions from programs. It performs the basic arithmetic, logic, control, and input/output (I/O) operations specified by the instructions.

# CPU Components

1. **Control Unit (CU)**: 

- Directs the operation of the processor. It tells the computer's memory, arithmetic logic unit (ALU), and I/O devices how to respond to a program's instructions. 

- The Control Unit directs the operation of the processor. It manages and coordinates the operations of the CPU and controls the flow of data and instructions between the CPU and other parts of the computer system. It directs the flow of data between the CPU and the other devices. 

2. **Arithmetic Logic Unit (ALU)**: The arithmetic logic unit (ALU) is a digital circuit within the processor that performs integer arithmetic and bitwise logic operations.

3. **Registers**: 

- Small, fast storage locations within the CPU used to hold temporary data and instructions. 

- CPU registers are small, high-speed storage locations. They are the fastest memory in the memory hierarchy. 

- Registers can store a variety of data types, including instructions, memory addresses and individual data items. The size of a register is typically measured in bits, ranging from 8 to 64 bits, depending on the processor architecture. The size of the register determines the size of data that it can hold.

- Registers are the fastest type of memory in a computer system. They are built into the CPU chip for quick data access.

- Registers are used by the CPU as high-speed temporary storage during program execution. They hold data that is being used or processed by the CPU.

4. **Cache**: A small-sized type of volatile computer memory that provides high-speed data access to the CPU and improves processing speed by storing frequently used instructions and data.

5. **Buses**: Communication systems that transfer data between components inside a computer or between computers. The main buses are the data bus, address bus, and control bus.

# CPU Cores

A CPU core is a smaller processor within the CPU. Modern CPUs can have multiple cores, allowing them to process multiple tasks simultaneously. This improves overall performance, especially in multitasking environments.

- **Single-core CPU**: Has one core that can execute one instruction stream at a time.

- **Multi-core CPU**: Has multiple cores (e.g., dual-core, quad-core, hexa-core, octa-core) that can execute multiple instruction streams simultaneously.

# What Does a CPU Do?

The CPU performs a series of repeated tasks referred to as the Fetch-Decode-Execute cycle.

1. **Fetch**: The first step in the cycle is fetching the instruction from memory. The CPU looks at the program counter to determine the memory address of the next instruction. The instruction at this memory location is then fetched and placed into a register within the CPU.

2. **Decode**: Converts the instruction into signals that control other parts of the CPU. Once the instruction has been fetched, the CPU decodes it. In this step, the CPU determines what operation the instruction is supposed to perform. The control unit within the CPU is responsible for this decoding.

3. **Execute**: Performs the operation defined by the instruction (e.g., arithmetic operations, data transfer). After the instruction is decoded, the CPU executes it. This involves performing the operation that was determined during the decode step. The exact nature of this operation can vary widely, depending on what the instruction was.

4. **Store**: Writes back the result of the operation to memory or a register.

After the execute step, the CPU moves on to the next instruction in the program, and the cycle starts over. This process is repeated for every instruction in the program until the program ends.

Consider a simple instruction `ADD R1, R2, R3`.

1. **Fetch**: The instruction `ADD R1, R2, R3` is fetched from memory.

2. **Decode**: The Control Unit decodes this instruction:

- **Opcode**: `ADD` (Indicating an addition operation)

- **Operands**: `R1`, `R2`, `R3` (Indicating the registers involved)

3. The CPU translates this into control signals that:

- Selects the contents of `R2` and `R3`
- Sends these contents to the ALU.
- Configure the ALU to perform the addition.
- Store the result of the addition back into `R1`.

The control signals are essentially binary codes that:

- Enable or disable specific pathways (buses) for data movement.
- Trigger specific functions in the ALU (like addition, subtraction, etc...)
- Control read/write operations to and from registers and memory.
- Direct the data flow between the CPU and other parts of the computer.

# Essential CPU Components and Terminology

- **Clock Cycle**: A clock cycle is a single oscillation of the clock signal in a computer. It represents the smallest unit of time in which a processor can complete a basic operation, such as fetching an instruction, decoding it, or executing it. 

- **Clock Speed**: The speed at which a CPU executes instructions, measured in GHz(gigahertz). Higher clock speeds generally indicate faster performance. For example a CPU that is 4GHz, meaning it can execute 4 billion clock cycles in 1 second.

- **Threads**: Virtual versions of CPU cores. They allow a single core to handle multiple tasks simultaneously using a technique called hyper-threading or simultaneous multithreading (SMT).

- **Instruction Set Architecture (ISA)**: A set of instructions that the CPU can execute. Examples include x86, ARM, and MIPS.

- **Integrated Graphics Processing Unit (iGPU)**: Some CPUs include a GPU built into the same chip, allowing for graphics processing without a separate graphics card.

It's important to not get confused over a **hardware thread** and a **software thread**.

## Hardware Threads (Logical Processors)

Hardware threads are threads that the CPU can manage directly, allowing each core to handle multiple instruction streams simultaneously.

These are also known as Hyper-Threading (Intel) or Simultaneous Multithreading (AMD). This technology allows a single physical CPU core to run multiple tasks simultaneously rather than sequentially, improving performance in most situations. A single physical CPU core with hyper-threading appears as two logical CPUs to an operating system. The CPU pretends it has more cores than it does, and it uses its own logic to speed up program execution.

For example, the Intel Core i7 with Hyper-Threading has 4 physical cores but 8 logical processors (each core handles 2 hardware threads). This allows the CPU to manage 8 instruction streams simultaneously.

**While a core cannot run multiple threads in true parallel** (At the same time), Hyper-Threading allows it to handle multiple threads in a way that they appear to be running simultaneously by rapidly switching between them.

## Software Threads

Software threads are threads created and managed by the operating system or applications.

- **Dynamic Creation**: Software threads can be created as needed by the application.

- **Scheduling by OS**: The operating system schedules software threads on available hardware threads (logical processors).

For application examples,

- **Single-Core**: When running a web browser, one core processes all tasks sequentially (loading pages, running scripts, user input).

- **Multi-Core**: When running a video editing application, each core handles different tasks (e.g., rendering video, processing audio, applying effects), resulting in faster performance.

- **Running a Single Process with Multiple Threads**: If you have a single process with 20 threads running on a CPU with 4 cores, each having 2 hardware threads (due to Hyper-Threading), then your operating system’s scheduler will distribute these 20 threads across the available logical processors. This means that up to 8 threads (4 cores * 2 hardware threads per core) could potentially be running truly simultaneously. The remaining threads will have to wait for their turn to be scheduled on a core. The code execution on each Core will be in parallel, but the hardware threads within a Core will switch between them.

## Unified Example

Consider a quad-core CPU with Hyper-Threading (8 logical processors).

- **CPU Cores**: The 4 physical cores can handle 4 tasks in true parallel. Each core can execute one instruction stream independently and truly in parallel.

- **Hardware Threads**: Each core supports 2 hardware threads, allowing (4 x 2) 8 instruction streams to be managed simultaneously.

- **Software Threads**: An application like a web server might create 20 software threads to handle incoming requests. The OS schedules these 20 software threads across the 8 logical processors for execution.

**When each core in a multi-core CPU is executing its own instruction stream at the same time, this is true parallel execution**. For example, in a quad-core CPU, four separate tasks can be executed at the exact same moment, one on each core.

Within each physical core, Hyper-Threading or SMT allows two (or more) instruction streams (hardware threads) to be managed simultaneously. **This means the core can quickly switch between these threads or run them in an interleaved fashion**.

Imagine a CPU with 4 cores, each capable of Hyper-Threading.
- Core 1 runs two threads, T1 and T2.
- Core 2 runs two threads, T3 and T4.
- Core 3 runs two threads, T5 and T6.
- Core 4 runs two threads, T7 and T8.

Now, 

- Core 1: T1 and T2 are interleaved. When T1 is waiting for data, T2 can execute. **T1 and T2 are not ran in true parallel, because they're threads within the same core**.

- Core 2: T3 and T4 are interleaved similarly.

This allows each core to appear as if it’s doing more work simultaneously, improving efficiency, but the actual execution is interleaved and resource-sharing.

- **Simultaneous Execution**: In the context of hardware threads, simultaneous execution means interleaving (alternating between) execution to improve resource utilization.

- **Parallel Execution**: True parallel execution refers to multiple physical cores executing different instruction streams at the same time.

Thus, when we say "Each core supports 2 hardware threads, allowing 8 instruction streams to be managed simultaneously," it means,

- **Parallel Execution**: 4 cores can run 4 instruction streams in parallel (one per core).

- **Simultaneous/Interleaved Execution**: Each core can interleave 2 hardware threads, making it appear as if 8 instruction streams are being managed simultaneously.

This combination enhances the CPU's ability to handle multiple tasks efficiently by using both true parallel execution (across cores) and interleaved execution (within each core).



# CPU Instruction Set

The CPU instruction set (or instruction set architecture, ISA) **is a set of commands that a specific CPU can execute**. It defines the operations the CPU can perform and how those operations are encoded.

- **Abstract Operations**: It includes operations like arithmetic, data movement, control flow, and logic.

- **Architecture-Specific**: Different CPU architectures (e.g., x86, ARM, MIPS) have different instruction sets.

- **Examples**: Instructions like `ADD`, `MOV`, `JMP`, etc., are part of the instruction set.

- **x86 Instruction Set**: Common in Intel and AMD CPUs, includes instructions like `MOV`, `ADD`, `SUB`, `MUL`.

- **ARM Instruction Set**: Common in mobile devices and embedded systems, includes instructions like `LDR`, `STR`, `ADD`, `SUB`.

Every other layer (assembly language and machine code) **is built to conform to this set of instructions.**



# Assembly Language

Assembly language is a low-level programming language that uses human-readable mnemonics **to represent the machine code instructions of a specific CPU's instruction set**. This means each ISA has its own assembly language that directly corresponds to its machine instructions.

This means that when programming in assembly, the specific commands and syntax you use will depend on the ISA for the target architecture..

- **One-to-One Mapping**: Each assembly instruction corresponds directly to a machine code instruction.

- **Human-Readable**: Uses mnemonics and labels to make the code more understandable.

- **Architecture-Specific**: Assembly language is specific to a CPU's instruction set.

**x86 Assembly**

In this example, `MOV`, `AX` and `ADD` are from the x86 ISA.

```
MOV AX, 1   ; Move the value 1 into the AX register
ADD AX, 2   ; Add the value 2 to the AX register
```

**ARM Assembly**

In this example, `MOV`, `ADD` and `R0` are from the ARM ISA, `#1` and `#2` are constants.

```
MOV R0, #1  ; Move the value 1 into the R0 register
ADD R0, R0, #2  ; Add the value 2 to the R0 register
```

# Machine Code

Machine code is the binary representation of the instructions that the CPU executes. It is the lowest-level programming language, **directly executed by the CPU**.


- **Binary Format**: Represented in binary (0s and 1s), often displayed in hexadecimal for readability.

- **Direct Execution**: This is the actual code that the CPU runs.

- **Architecture-Specific**: Different CPUs have different machine code formats corresponding to their instruction sets.

**x86 Machine Code (Hexadecimal Representation)**

```
B8 01 00 00 00  ; MOV AX, 1
83 C0 02        ; ADD AX, 2
```

**ARM Machine Code (Hexadecimal Representation)**

```
E3A00001        ; MOV R0, #1
E2800002        ; ADD R0, R0, #2
```

## Why Machine Code or Assembly Can't Run on Every CPU

1. **Instruction Set Architecture (ISA)**

- **Different ISAs**: Each CPU family (x86, ARM, MIPS, etc.) has its own unique ISA, defining the binary encoding of instructions and their behavior. An instruction in x86 assembly or machine code has no meaning on an ARM CPU and vice versa.

- **Specific Encoding**: The way instructions are encoded in binary (machine code) is specific to the ISA. For example, the machine code `B8 01 00 00 00` means "move the value 1 into the AX register" on an x86 CPU, but the same binary sequence would be meaningless on an ARM CPU.

2. **CPU Architecture**

- **Hardware Design**: CPUs are designed with a specific ISA in mind. The control logic, registers, and execution units are tailored to execute the instructions defined by that ISA.

- **Different Registers and Operations**: Different architectures have different sets of registers and supported operations. For instance, ARM CPUs have different registers and operations than x86 CPUs, making their machine code incompatible.

3. **Assembly Language Specificity**

- **Direct Correspondence**: Assembly language is a human-readable form of machine code for a specific ISA. Writing assembly code for one ISA does not translate to another. An x86 assembly program can't run on an ARM CPU because the instructions and register names are different.

# x86 and x64

**x86 is a family of instruction set architectures (ISAs) initially developed by Intel based on the Intel 8086 microprocessor** and its successors. Intel both designed and manufactured the x86 architecture. x86 simply refers to a family of processors and the instruction set they all use. It doesn't actually say anything specific about data sizes. The term "x86" comes from Intel’s line of processors that started with the Intel 8086 in 1978. The "86" in x86 refers to the last two digits in the names of these early processors, such as the 80**86**, 801**86**, 802**86**, 803**86**, and 804**86**. It can access up to 4GB of RAM and uses 32-bit data paths. x86 applications are compatible with both 32-bit and 64-bit operating systems.

x86 uses a complex instruction set, allowing it to execute multi-step operations with a single instruction. The x86 architecture maintains backward compatibility, meaning software designed for older x86 processors generally works on newer ones. The primary developer and the largest manufacturer of x86 CPUs is Intel. The x86 architecutre is predominantly used in personal computers (PCs), laptops, and servers. A major competitor to Intel is AMD, also producing x86 CPUs.

x86-64 is the full, technical name of the 64-bit extension to the original x86 architecture, developed by AMD and sometimes called AMD64. When AMD introduced 64-bit processing for x86, they called it **x86-64** to indicate backwards compatibility with 32-bit x86 but with the 64-bit capabilities. x64 became shorthand for x86-64, adopted mainly for simplicity. This term was popularized by operating systems like Windows, which labeled 64-bit versions as x64 to distinguish them from x86 (32-bit). So, x64 is widely used to mean x86-64 but is technically a branding term rather than a strict technical one.


**x86** - 32-bit, but technically a family name that includes both 16-bit and 32-bit processors.
**x86-64** - The precise technical name for the 64-bit extension to x86, originally by AMD.
**x64** - A shorthand term for x86-64, commonly used in OS and software terminology.

On Windows, we can also observe two program files directories, `Program Files` and `Program Files (x86)`.

For `Program Files (x86)`

- This folder is specifically for 32-bit applications that use the x86 ISA.
- The term x86 here reflects the historical link to 32-bit processing. x86 becomes synonymous with 32-bit after the intel 80386 introduced 32-bit capabilities.

For `Program Files`

- This folder is for 64-bit applications, compatible with x64 (or x86-64) architecture, which is technically an extension of the x86 ISA to support 64-bit processing.
- Programs here are compiled with 64-bit instructions and can fully utilize the 64-biot addressing and processing capabilities of a 64-bit CPU, like accessing more than 4 GB of RAM.
- These applications rely on 64-bit versionf of system libraries, which aren't compatible with 32-bit programs.

So, both folders are related to the x86 ISA family, but they organize applications based on which version of the x86 ISA they are built for. If different ISA was used to create binaries such as ARM then it will need to be placed into a different installation directory.

# ARM Architecture

ARM (Advanced RISC Machines) is a family of ISAs developed by ARM Holdings, based on the RISC (Reduced Instruction Set Computing) principles.

ARM uses a simpler, more efficient instruction set that requires fewer transistors, leading to lower power consumption and heat output.

**ARM Holdings licenses its designs to other companies who then manufacture and sell the actual chips**. It is widely used in mobile devices (smartphones, tablets), embedded systems, and increasingly in laptops and servers. For example,

- **Apple**: Produces custom ARM-based chips (e.g., M1, M2) for its devices.

- **Samsung**: Manufactures Exynos chips for its own and other devices.

- **Nvidia**: Produces ARM-based processors for various applications, including gaming consoles and automotive systems.

x86 and ARM are two different types of CPU architectures, with x86 being used mainly in PCs and servers, and ARM being dominant in mobile and embedded devices. 

# CPU Compatibilities

The major manufacturers of these processors include **Intel and AMD for x86 and x86-64 (x64)**, and companies like **Apple, Samsung, and Nvidia for ARM**. This means, different companies (Intel and AMD) can build their own CPUs, **but build to support the ISA**.

Both Intel and AMD CPUs adhere to the x86 and x86-64 ISA specifications so they can understand and execute the same instructions. This means any code compiled for x86/x86-64 will run on both intel and AMD CPUs, **as long as it doens't rely on CPU-specific extensions**.

Each company is free to implement the x86 instructions in its own way at the **microarchitecture** level. The microarchitecture is the detailed design of how instructions are executed within the CPU, including things like pipelines, cache sizes, branch predictors and execution units. This is where Intel and AMD make the CPUs unique. **While they execute the same instructions, they optimize differently to improve speed, efficiency and power consumption**.

Beyond the standard x86 instructions, each company may add **optional extensions** that improve performance for specific applications. Intel and AMD must adhere to the x86 ISA to ensure compatibility, but they are free to innovate on microarchitecture and use extensions and compiler optimizations to differentiate performance. This is why you’ll see performance differences between Intel and AMD CPUs even when running the same x86-compiled code.

1. **Intel has AVX-512 (Advanced Vector Extensions)**, which allows for more complex operations in parallel for large datasets, especially useful in fields like scientific computing.

2. **AMD includes its own extensions like SS35** and, in some models, Advanced Vector Extensions tailored to its architecture.

Compilers can detect when they're running on CPUs with specific extensions and generate code that takes advantage of those instructions. When using the Intel Compiler, for example, can be optimized to utilize **Intel-specific features**, like AVX-512, if it detects they're available. This might make the code run more efficiently on Intel CPUs than on AMD CPUs. Using compiler specific extensions will no longer make it compatible with other CPUs, such as using the Intel Compiler with extensions enabled, will no longer make it run on AMD CPUs.
