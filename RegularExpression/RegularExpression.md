
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 基本语法](#1-基本语法)
- [2. 编辑器中正则表达式搜索](#2-编辑器中正则表达式搜索)
  - [2.1. 关系或](#21-关系或)
  - [2.2. 关系与](#22-关系与)
  - [2.3. 搜索指定的一个或者多个任意文字](#23-搜索指定的一个或者多个任意文字)

<!-- /code_chunk_output -->


# 1. 基本语法

# 2. 编辑器中正则表达式搜索

常用编辑器如notepad++，vscode都支持正则表达式搜索

## 2.1. 关系或

- 关系或：用符号"|"，注意符号"|"两边不能加空格，除非需要搜索的关键词就带有空格

如下是一段运行log：

```c {.line-numbers}
09-10 16:49:01.847 [Station2 Coordinator] INFO  DefaultLog - 模组2_1：A料盘到位，准备取料
09-10 16:49:01.847 [Station2 Coordinator] INFO  DefaultLog - 模组2_1：A料盘：位置1，准备取料
09-10 16:49:02.187 [Station2 Coordinator] INFO  DefaultLog - 模组2_1：发送取料命令
09-10 16:49:02.307 [Station2 Coordinator] INFO  DefaultLog - 模组2_2：离开治具2_2
09-10 16:49:02.678 [Station2 Coordinator] INFO  DefaultLog - 治具2_2：上料完成，左穴有料，右穴有料，发送开始测试命令
09-10 16:49:02.893 [Unloader Coordinator] INFO  DefaultLog - write Reg_Downstream_Empty_Line_Ready: 1
09-10 16:49:03.217 [Station2 Coordinator] INFO  DefaultLog - 模组2_2：D料盘：位置11，准备取料
09-10 16:49:03.567 [Station2 Coordinator] INFO  DefaultLog - 模组2_2：发送取料命令
09-10 16:49:03.872 [Station2 Coordinator] INFO  DefaultLog - write Reg_Upstream_Empty_Tray_Ready: 0
09-10 16:49:04.357 [Station2 Coordinator] INFO  DefaultLog - 模组2_1：取料结果1，吸嘴1上有料，吸嘴2上有料
09-10 16:49:04.707 [Station2 Coordinator] INFO  DefaultLog - 模组2_1：载板上无料，吸嘴上有料，发送上料命令
09-10 16:49:05.078 [Station2 Coordinator] INFO  DefaultLog - 治具2_2：载板2测试完成，关闭真空吸，等待下料
```

如果想从中筛选出包含“模组2_1”或者“模组2_2”的日志，正则表达式的写法如下：

```c {.line-numbers}
模组2_1|模组2_2
```


## 2.2. 关系与

- 关系与：用两个符号".*"一起表示

如下是一段运行log：

```c {.line-numbers}
09-10 16:49:01.847 [Station2 Coordinator] INFO  DefaultLog - 模组2_1：A料盘到位，准备取料
09-10 16:49:01.847 [Station2 Coordinator] INFO  DefaultLog - 模组2_1：A料盘：位置1，准备取料
09-10 16:49:02.187 [Station2 Coordinator] INFO  DefaultLog - 模组2_1：发送取料命令
09-10 16:49:02.307 [Station2 Coordinator] INFO  DefaultLog - 模组2_2：离开治具2_2
09-10 16:49:02.678 [Station2 Coordinator] INFO  DefaultLog - 治具2_2：上料完成，左穴有料，右穴有料，发送开始测试命令
09-10 16:49:02.893 [Unloader Coordinator] INFO  DefaultLog - write Reg_Downstream_Empty_Line_Ready: 1
09-10 16:49:03.217 [Station2 Coordinator] INFO  DefaultLog - 模组2_2：D料盘：位置11，准备取料
09-10 16:49:03.567 [Station2 Coordinator] INFO  DefaultLog - 模组2_2：发送取料命令
09-10 16:49:03.872 [Station2 Coordinator] INFO  DefaultLog - write Reg_Upstream_Empty_Tray_Ready: 0
09-10 16:49:04.357 [Station2 Coordinator] INFO  DefaultLog - 模组2_1：取料结果1，吸嘴1上有料，吸嘴2上有料
09-10 16:49:04.707 [Station2 Coordinator] INFO  DefaultLog - 模组2_1：载板上无料，吸嘴上有料，发送上料命令
09-10 16:49:05.078 [Station2 Coordinator] INFO  DefaultLog - 治具2_2：载板2测试完成，关闭真空吸，等待下料
```

如果想从中筛选出包含“模组2”和“A料盘”的日志，正则表达式的写法如下：

```c {.line-numbers}
模组2.*A料盘
```

语法解析：
> 其中符号"."表示任意字符，符号"*"表示匹配0次或者多次，两者结合起来就表示多个任意字符，也就是关键词“模组2”和关键词“A料盘”之间有任意多个字符

*注：此种搜索方式只在段内匹配*

## 2.3. 搜索指定的一个或者多个任意文字

如下是一套试题中的一部分：

``` {.line-numbers}
软件设计中模块划分应遵循的准则是（B）.
已知如下代码，选项中函数调用语句错误的是（D）.
以下哪个选项可以组成一个正常通信的I2C报文（D）.
以下关于I2C的描述正确的是（ABC）.
```
现在要将括号中的答案全部删除，可以采用正则表达式替换的方式，搜索内容为：

```c {.line-numbers}
（.{1,4}）.
```

将其替换为：

```c {.line-numbers}
（ ）.
```

即可删除整套试题中所有选择题的答案

语法解析：
> 符号“.”表示任意字符，表达式“{1,4}”匹配1到4次，两者结合起来表示匹配1-4个任意字符，也就是关键词“（”和关键词“）.”之间有1-4个任意字符。

