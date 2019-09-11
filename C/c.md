
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 通用语法](#1-通用语法)
  - [1.1. "#和##的用法"](#11-和的用法)
    - [1.1.1. 功能](#111-功能)
    - [1.1.2. 一般用法](#112-一般用法)
    - [1.1.3. 注意事项](#113-注意事项)
  - [1.2. 函数指针](#12-函数指针)

<!-- /code_chunk_output -->

# 1. 通用语法

## 1.1. "#和##的用法"

### 1.1.1. 功能

使用#把宏参数变为一个字符串,用##把两个宏参数贴合在一起.

### 1.1.2. 一般用法

```c {.line-numbers}
#define STR(s) #s
#define CONS(a,b) (a##e##b)
void main(void)
{
	printf(STR(abcd));//输出字符串abcd
    printf("%f",1e3) ;//输出科学计数法1e3对应的浮点数1000.000000
}
```

### 1.1.3. 注意事项

> 当宏参数是另一个宏的时候，需要注意的是凡宏定义里有用’#’或’##’的地方宏参数是不会再展开。即， 只有当前宏生效, 参数里的宏不会生效

**示例**

```c {.line-numbers}
#include<limits.h>
#define A          (2)
#define STR(s)     #s
#define CONS(a,b)  (a##e##b)
void main(void)
{
	printf("int max: %s\n",  STR(INT_MAX));    // INT_MAX 在limits.h文件中 → 输出int max: INT_MAX
	printf("%s\n", CONS(A, A));                // compile error --- (AeA)
}
```

分析：
>由于A和INT_MAX均是宏，且作为宏CONS和STR的参数，并且宏CONS和STR中均含有#或者##符号，所以A和INT_MAX均不能被解引用。导致不符合预期的情况出现。

**解决对策**

> 解决这个问题的方法很简单. 加多一层中间转换宏. 加这层宏的用意是把所有宏的参数在这层里全部展开,那么在转换宏里的那一个宏(_STR)就能得到正确的宏参数.


```c {.line-numbers}
#include<limits.h>
#define A           2
#define _STR(s)     #s
#define STR(s)      _STR(s)          // 转换宏
#define _CONS(a,b)  (a##e##b)
#define CONS(a,b)   _CONS(a,b)       // 转换宏
void main(void)
{
	printf("int max: %s\n",  STR(INT_MAX));   
	printf("%f\n", CONS(A,A));                
}
```

## 1.2. 函数指针

函数指针变量：

一个数据变量的内存地址可以存储在相应的指针变量中，函数的首地址也以存储在某个函数指针变量中。这样，我就可以通过这个函数指针变量来调用所指向的函数了。在C系列语言中，任何一个变量，总是要先声明，之后才能使用的。函数指针变量也应该要先声明。

函数指针变量的声明：

> void (*funP)(int) ;   //声明一个指向同样参数、返回值的函数指针变量。

```c {.line-numbers}
#include <stdio.h>
#include <stdlib.h>

void (*funP)(int);   //声明也可写成void(*funP)(int x)，但习惯上一般不这样。
void (*funA)(int);
void myFun(int x);    //声明也可写成：void myFun( int );
int main()
{
    //一般的函数调用
    myFun(100);

    //myFun与funP的类型关系类似于int 与int *的关系。
    funP=&myFun;  //将myFun函数的地址赋给funP变量
    (*funP)(200);  //通过函数指针变量来调用函数

    //myFun与funA的类型关系类似于int 与int 的关系。
    funA=myFun;
    funA(300);

    //三个貌似错乱的调用
    funP(400);
    (*funA)(600);
    (*myFun)(1000);

    return 0;
}

void myFun(int x)
{
    printf("myFun: %d\n",x);
}
```

总结：

1. 其实，myFun的函数名与funP、funA函数指针都是一样的，即都是函数指针。myFun函数名是一个函数指针常量，而funP、funA是函数数指针变量，这是它们的关系。

1. 但函数名调用如果都得如(*myFun)(10)这样，那书写与读起来都是不方便和不习惯的。所以C语言的设计者们才会设计成又可允许myFun(10)这种形式地调用（这样方便多了，并与数学中的函数形式一样）。

1. 为了统一调用方式，funP函数指针变量也可以funP(10)的形式来调用。

1. 赋值时，可以写成funP=&myFun形式，也可以写成funP=myFun。

1. 但是在声明时，void myFun(int )不能写成void (*myFun)(int )。void (*funP)(int )不能写成void funP(int )。

1. 函数指针变量也可以存入一个数组内。数组的声明方法：int (*fArray[10]) ( int );

定义函数指针类型：

```c {.line-numbers}
#include <stdio.h>
#include <stdlib.h>

typedef void(*FunType)(int);
//前加一个typedef关键字，这样就定义一个名为FunType函数指针类型，而不是一个FunType变量。
//形式同 typedef int* PINT;
void myFun(int x);
void hisFun(int x);
void herFun(int x);
void callFun(FunType fp,int x);
int main()
{
    callFun(myFun,100);//传入函数指针常量，作为回调函数
    callFun(hisFun,200);
    callFun(herFun,300);

    return 0;
}

void callFun(FunType fp,int x)
{
    fp(x);//通过fp的指针执行传递进来的函数，注意fp所指的函数有一个参数
}

void myFun(int x)
{
    printf("myFun: %d\n",x);
}
void hisFun(int x)
{
    printf("hisFun: %d\n",x);
}
void herFun(int x)
{
    printf("herFun: %d\n",x);
}
```
