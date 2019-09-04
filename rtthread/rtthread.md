<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. rt_thread命名规则](#1-rt_thread命名规则)
- [2. 杂项](#2-杂项)
  - [2.1. main函数](#21-main函数)
  - [2.2. 栈](#22-栈)
- [3. 函数解析](#3-函数解析)
  - [3.1. rt_list_init](#31-rt_list_init)
  - [3.2. rt_list_insert_after](#32-rt_list_insert_after)
  - [3.3. rt_list_insert_before](#33-rt_list_insert_before)
  - [3.4. rt_list_remove](#34-rt_list_remove)
  - [3.5. rt_hw_stack_init](#35-rt_hw_stack_init)
  - [3.6. rt_list_entry](#36-rt_list_entry)
  - [3.7. rt_hw_context_switch_to](#37-rt_hw_context_switch_to)
    - [3.7.1. ARM常用汇编指令](#371-arm常用汇编指令)
    - [3.7.2. 全局变量](#372-全局变量)
    - [3.7.3. 常量](#373-常量)
    - [3.7.4. 汇编代码产生指令](#374-汇编代码产生指令)
    - [3.7.5. 函数解析](#375-函数解析)

<!-- /code_chunk_output -->

# 1. rt_thread命名规则

rt_thread_init函数遵循RT-Thread中的函数命名规则，以小写的rt开头，表示这是一个外部函数，可以由用户调用，以_rt开头的函数表示内部函数，只能由RT-Thread内部使用。紧接着是文件名，表示该函数放在哪个文件，最后是函数功能名称

# 2. 杂项

## 2.1. main函数

一个工程如果没有main函数是编译不成功的，会出错。因为系统在开始执行的时候先执行启动文件里面的复位程序，复位程序里面会调用C库函数__main，__main的作用是初始化好系统变量，如全局变量，只读的，可读可写的等等。__main最后会调用__rtentry，再由__rtentry调用main函数，从而由汇编跳入到C的世界，这里面的main函数就需要我们手动编写，如果没有编写main函数，就会出现main函数没有定义的错误。

## 2.2. 栈

在一个裸机系统中，如果有全局变量，有子函数调用，有中断发生。那么系统在运行的时候，全局变量放在哪里，子函数调用时，局部变量放在哪里，中断发生时，函数返回地址放在哪里？在裸机系统中，他们统统放在一个叫栈的地方，栈是单片机RAM里面一段连续的内存空间，栈的大小一般在启动文件或者链接脚本里面指定，最后由C库函数_main进行初始化。

在多线程系统中，每个线程都是独立的，互不干扰的，所以要为每个线程都分配独立的栈空间，这个栈空间通常是一个预先定义好的全局数组，也可以是动态分配的一段内存空间，但它们都存在于RAM中。

# 3. 函数解析

## 3.1. rt_list_init

rt_list_t类型的节点的初始化，就是将节点里面的next和prev这两个节点指针指向节点本身
```c {.line-numbers}
rt_inline void rt_list_init(rt_list_t *l)
{
    l->next = l->prev = l;
}
```

## 3.2. rt_list_insert_after

在双向链表后面插入一个节点

```c {.line-numbers}
/**
 * @brief insert a node after a list
 *
 * @param l list to insert it
 * @param n new node to be inserted
 */
rt_inline void rt_list_insert_after(rt_list_t *l, rt_list_t *n)
{
    l->next->prev = n; //l->next是node2
    n->next = l->next;

    l->next = n;
    n->prev = l;
}
```

![在双向链表后面插入一个节点](./Fig/rt_list_insert_after.jpg){#fig:rt_list_insert_after}

## 3.3. rt_list_insert_before

在双向链表尾部插入一个节点

```c {.line-numbers}
/**
 * @brief insert a node before a list
 *
 * @param n new node to be inserted
 * @param l list to insert it
 */
rt_inline void rt_list_insert_before(rt_list_t *l, rt_list_t *n)
{
    l->prev->next = n; //l->prev是NODEn
    n->prev = l->prev;

    l->prev = n;
    n->next = l;
}
```

![双向列表在尾部插入一个节点](./Fig/rt_list_insert_before.jpg){#fig:rt_list_insert_before}

## 3.4. rt_list_remove

从双向链表删除一个节点

```c {.line-numbers}
/**
 * @brief remove node from list.
 * @param n the node to remove from the list.
 */
rt_inline void rt_list_remove(rt_list_t *n)
{
    // NODE1->next = NODE3 
    // NODE3->prev = NODE1
    // NODE1 = n->prev
    // NODE3 = n->next

    n->next->prev = n->prev;
    n->prev->next = n->next;
    n->next = n->prev = n; //用自己初始化自己
}
```

![从双向链表删除一个节点](./Fig/rt_list_remove.jpg){#fig:rt_list_remove}


## 3.5. rt_hw_stack_init
```c {.line-numbers}
rt_uint8_t *rt_hw_stack_init(void       *tentry,
                             void       *parameter,
                             rt_uint8_t *stack_addr, /*线程栈顶地址-4*/
                             void       *texit)
{
    struct stack_frame *stack_frame;
    rt_uint8_t         *stk;
    unsigned long       i;

// 获取栈顶地址
    stk  = stack_addr + sizeof(rt_uint32_t);

// 让stk这个指针向下8个字节对齐，确保stk是8字节对齐的地址。
// 在Cortex-M3（Cortex-M4或Cortex-M7）内核的单片机中，因为总线宽度是32位的，
// 通常只要栈保持4字节对齐就行，可这样为啥要8字节？难道有哪些操作是64位的？
// 确实有，那就是浮点运算，所以要8字节对齐（但是目前我们都还没有涉及到浮点运算，
// 只是为了后续兼容浮点运行的考虑）。如果栈顶指针是8字节对齐的，
// 在进行向下8字节对齐的时候，指针不会移动，如果不是8字节对齐的，
// 在做向下8字节对齐的时候，就会空出几个字节，不会使用，比如当stk是33，
// 明显不能整除8，进行向下8字节对齐就是32，那么就会空出一个字节不使用
    stk  = (rt_uint8_t *)RT_ALIGN_DOWN((rt_uint32_t)stk, 8);

//stk指针继续向下偏移sizeof(struct stack_frame)个地址 
    stk -= sizeof(struct stack_frame);

// 将stk指针强制转化为stack_frame类型后存到stack_frame
    stack_frame = (struct stack_frame *)stk;

//以stack_frame为起始地址，将栈空间里面的sizeof(struct stack_frame)个内存初始化为0xdeadbeef
// stack_frame里面保存的是r4-r11,r0-r3,r12,lr,pc,psr寄存器
    for (i = 0; i < sizeof(struct stack_frame) / sizeof(rt_uint32_t); i ++)
    {
        ((rt_uint32_t *)stack_frame)[i] = 0xdeadbeef;
    }

// 初始化异常发生时需要自动保存的寄存器
    stack_frame->exception_stack_frame.r0  = (unsigned long)parameter; /* r0 : argument */
    stack_frame->exception_stack_frame.r1  = 0;                        /* r1 */
    stack_frame->exception_stack_frame.r2  = 0;                        /* r2 */
    stack_frame->exception_stack_frame.r3  = 0;                        /* r3 */
    stack_frame->exception_stack_frame.r12 = 0;                        /* r12 */
    stack_frame->exception_stack_frame.lr  = (unsigned long)texit;     /* lr */
    stack_frame->exception_stack_frame.pc  = (unsigned long)tentry;    /* entry point, pc */
    stack_frame->exception_stack_frame.psr = 0x01000000L;              /* PSR */

    /* return task's current stack address */
    return stk;
}

```

**stack_frame结构体定义**

```c {.line-numbers}
struct exception_stack_frame
{
    // 异常发生时，自动加载到CPU寄存器的内容
    rt_uint32_t r0;
    rt_uint32_t r1;
    rt_uint32_t r2;
    rt_uint32_t r3;
    rt_uint32_t r12;
    rt_uint32_t lr;
    rt_uint32_t pc;
    rt_uint32_t psr;
};

struct stack_frame
{
#if USE_FPU
    rt_uint32_t flag;
#endif /* USE_FPU */
// 异常发生时，需手动加载到CPU寄存器的内容
    /* r4 ~ r11 register */
    rt_uint32_t r4;
    rt_uint32_t r5;
    rt_uint32_t r6;
    rt_uint32_t r7;
    rt_uint32_t r8;
    rt_uint32_t r9;
    rt_uint32_t r10;
    rt_uint32_t r11;

    struct exception_stack_frame exception_stack_frame;
};
```

## 3.6. rt_list_entry

rt_list_entry()是一个已知一个结构体里面的成员的地址，反推出该结构体的首地址的宏

```c {.line-numbers}
/**
 * @brief get the struct for this entry
 * @param node the entry point
 * @param type the type of structure
 * @param member the name of list in structure
 */
#define rt_list_entry(node, type, member) \
    ((type *)((char *)(node) - (unsigned long)(&((type *)0)->member)))

/*@}*/
```

![rt_list_entry](./Fig/rt_list_entry.jpg){#fig:rt_list_entry}

我们知道了一个节点tlist的地址ptr，现在要推算出该节点所在的type 类型的结构体的起始地址f_struct_ptr。我们可以将ptr的值减去图中灰色部分的偏移的大小就可以得到f_struct_ptr的地址，现在的关键是如何计算出灰色部分的偏移大小。这里采取的做法是将0地址强制类型类型转换为type，即(type *)0，然后通过指针访问结构体成员的方式获取到偏移的大小，即(&((type *)0)->member)，最后即可算出f_struct_ptr = ptr - (&((type *)0)->member)

## 3.7. rt_hw_context_switch_to

当一个汇编函数在C文件中调用的时候，如果有一个形参，则执行的时候会将这个形参传入到CPU寄存器r0，如果有两个形参，第二个则传入到r1。

### 3.7.1. ARM常用汇编指令

| 指令名称    | 作用                                                                                                                                                                                                  |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EQU         | 给数字常量取一个名字，相当于C语言中的define                                                                                                                                                           |
| AREA        | 一个新的代码段或者数据段                                                                                                                                                                              |
| SPACE       | 分配内存空间                                                                                                                                                                                          |
| PRESERVE8   | 当前文件栈需按照8字节对齐                                                                                                                                                                             |
| EXPORT      | 声明一个标号具有全局属性，可被外部的文件使用                                                                                                                                                          |
| DCD         | 以字为单位分配内存，要求4字节对齐，并要求初始化这些内存                                                                                                                                               |
| PROC        | 定义子程序，与ENDP成对使用，表示子程序结束                                                                                                                                                            |
| WEAK        | 弱定义，如果外部文件声明了一个标号，则优先使用外部文件定义的标号，如果外部文件没有定义也不出错。要注意的是：这个不是ARM的指令，是编译器的，这里放在一起只是为了方便。                                 |
| IMPORT      | 声明标号来自外部文件，跟C语言中的EXTERN关键字类似                                                                                                                                                     |
| B           | 跳转到一个标号                                                                                                                                                                                        |
| ALIGN       | 编译器对指令或者数据的存放地址进行对齐，一般需要跟一个立即数，缺省表示4字节对齐。要注意的是：这个不是ARM的指令，是编译器的，这里放在一起只是为了方便。                                                |
| END         | 到达文件的末尾，文件结束                                                                                                                                                                              |
| MRS         | 加载特殊功能寄存器的值到通用寄存器                                                                                                                                                                    |
| MSR         | 存储通用寄存器的值到特殊功能寄存器                                                                                                                                                                    |
| CBZ         | 比较，如果结果为 0 就转移                                                                                                                                                                             |
| CBNZ        | 比较，如果结果非 0 就转移                                                                                                                                                                             |
| LDR         | 从存储器中加载字到一个寄存器中                                                                                                                                                                        |
| LDR[伪指令] | 加载一个立即数或者一个地址值到一个寄存器。举例：LDR Rd, = label，如果label是立即数，那Rd等于立即数，如果label是一个标识符，比如指针，那存到Rd的就是label这个标识符的地址                              |
| LDRH        | 从存储器中加载半字到一个寄存器中                                                                                                                                                                      |
| LDRB        | 从存储器中加载字节到一个寄存器中                                                                                                                                                                      |
| STR         | 把一个寄存器按字存储到存储器中                                                                                                                                                                        |
| STRH        | 把一个寄存器存器的低半字存储到存储器中                                                                                                                                                                |
| STRB        | 把一个寄存器的低字节存储到存储器中                                                                                                                                                                    |
| LDMIA       | 加载多个字，并且在加载后自增基址寄存器                                                                                                                                                                |
| STMIA       | 存储多个字，并且在存储后自增基址寄存器                                                                                                                                                                |
| ORR         | 按位或                                                                                                                                                                                                |
| BX          | 直接跳转到由寄存器给定的地址                                                                                                                                                                          |
| BL          | 跳转到 标号对应的地址，并且把跳转前的下条指令地址保存到 LR                                                                                                                                            |
| BLX         | 跳转到由寄存器REG给出的的地址，并根据 REG 的 LSB 切换处理器状态，还要把转移前的下条指令地址保存到 LR。ARM(LSB=0)，Thumb(LSB=1)。CM3 只在 Thumb 中运行，就必须保证 reg 的 LSB=1，否则一个 fault 打过来 |


### 3.7.2. 全局变量

```asm {.line-numbers}
IMPORT rt_thread_switch_interrupt_flag
IMPORT rt_interrupt_from_thread
IMPORT rt_interrupt_to_thread
```

使用IMPORT关键字导入一些全局变量，这三个全局变量在cpuport.c中定义

```c {.line-numbers}
/* 用于存储上一个线程的栈的sp的指针 */
rt_uint32_t rt_interrupt_from_thread;
/* 用于存储下一个将要运行的线程的栈的sp的指针 */
rt_uint32_t rt_interrupt_to_thread;
/* PendSV中断服务函数执行标志 */
rt_uint32_t rt_thread_switch_interrupt_flag;
```

### 3.7.3. 常量


*有关内核外设寄存器定义可参考官方文档：STM32F10xxx Cortex-M3 programming manual*
*系统控制块外设SCB地址范围：0xE000ED00-0xE000ED3F*

```asm {.line-numbers}
SCB_VTOR        EQU     0xE000ED08 ; 中断向量表偏移地址
NVIC_INT_CTRL   EQU     0xE000ED04 ; 中断控制状态寄存器
NVIC_SYSPRI2    EQU     0xE000ED20 ; 系统优先级寄存器(2)
NVIC_PENDSV_PRI EQU     0x00FF0000 ; PendSV 优先级值 (lowest)
NVIC_PENDSVSET  EQU     0x10000000 ; 触发PendSV exception的值
```

定义了一些常量，这些都是内核里面的寄存器，等下触发PendSV异常会用到。有关内核外设寄存器定义可参考官方文档：STM32F10xxx Cortex-M3 programming manual—4 Core peripherals，无论是M3/4/7内核均可以参考该文档。


### 3.7.4. 汇编代码产生指令

```asm {.line-numbers}
AREA |.text|, CODE, READONLY, ALIGN=2
THUMB
REQUIRE8
PRESERVE8
```

汇编代码产生指令，当我们新建一个汇编文件写代码时，必须包含类似的指令。AERA表示汇编一个新的数据段或者代码段，.text表示段名字，如果段名不是以字母开头，而是以其它符号开头则需要在段名两边加上‘|’，CODE表示为代码，READONLY表示只读，ALIGN=2，表示当前文件指令要2^2^字节对齐。THUMB表示THUMB指令代码，REQUIRE8和PRESERVE8均表示当前文件的栈按照8字节对齐。

### 3.7.5. 函数解析


```asm {.line-numbers}
;/*
; * void rt_hw_context_switch_to(rt_uint32 to);
; * r0 --> to
; * this fucntion is used to perform the first thread switch
; */
rt_hw_context_switch_to    PROC
    EXPORT rt_hw_context_switch_to
    ; set to thread
    LDR     r1, =rt_interrupt_to_thread
    STR     r0, [r1]

    IF      {FPU} != "SoftVFP"
    ; CLEAR CONTROL.FPCA
    MRS     r2, CONTROL             ; read
    BIC     r2, #0x04               ; modify
    MSR     CONTROL, r2             ; write-back
    ENDIF

    ; set from thread to 0
    LDR     r1, =rt_interrupt_from_thread
    MOV     r0, #0x0
    STR     r0, [r1]

    ; set interrupt flag to 1
    LDR     r1, =rt_thread_switch_interrupt_flag
    MOV     r0, #1
    STR     r0, [r1]

    ; set the PendSV exception priority
    LDR     r0, =NVIC_SYSPRI2
    LDR     r1, =NVIC_PENDSV_PRI
    LDR.W   r2, [r0,#0x00]       ; read
    ORR     r1,r1,r2             ; modify
    STR     r1, [r0]             ; write-back

    ; trigger the PendSV exception (causes context switch)
    LDR     r0, =NVIC_INT_CTRL
    LDR     r1, =NVIC_PENDSVSET
    STR     r1, [r0]

    ; restore MSP
    LDR     r0, =SCB_VTOR
    LDR     r0, [r0]
    LDR     r0, [r0]
    MSR     msp, r0

    ; enable interrupts at processor level
    CPSIE   I

    ; never reach here!
    ENDP
```

---

```asm {.line-numbers}
rt_hw_context_switch_to    PROC
……
    ENDP
```

PROC用于定义子程序，与ENDP成对使用，表示rt_hw_context_switch_to()函数开始

---

```asm {.line-numbers}
EXPORT rt_hw_context_switch_to
```

使用EXPORT关键字导出rt_hw_context_switch_to，让其具有全局属性，可以在C文件调用（但也要先在rthw.h中声明）。

---

```asm {.line-numbers}
    LDR     r1, =rt_interrupt_to_thread
    STR     r0, [r1]
```

设置rt_interrupt_to_thread的值。
第1行：将rt_interrupt_to_thread的地址加载到r1。
第2行：将r0的值存储到rt_interrupt_to_thread，r0存的是下一个将要运行的线程的sp的地址，由rt_hw_context_switch_to((rt_uint32_t)&to_thread->sp)调用的时候传到r0。

---

```asm {.line-numbers}
    LDR     r1, =rt_interrupt_from_thread
    MOV     r0, #0x0
    STR     r0, [r1]
```
