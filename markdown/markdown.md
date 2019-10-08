# 1. Markdown学习笔记 

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1.1. 入门](#11-入门)
  - [1.1.1. 环境准备](#111-环境准备)
- [1.2. 语法](#12-语法)
  - [1.2.1. 强调](#121-强调)
  - [1.2.2. 插入代码](#122-插入代码)
  - [1.2.3. 行内代码](#123-行内代码)
  - [1.2.4. Emoji & Font-Awesome](#124-emoji-font-awesome)
  - [1.2.5. 上标](#125-上标)
  - [1.2.6. 下标](#126-下标)
  - [1.2.7. 脚注](#127-脚注)
  - [1.2.8. 标记](#128-标记)
  - [1.2.9. 缩略](#129-缩略)
  - [1.2.10. 任务列表](#1210-任务列表)
  - [1.2.11. 目录列表](#1211-目录列表)
  - [1.2.12. 表格](#1212-表格)
- [1.3. 参考资料](#13-参考资料)

<!-- /code_chunk_output -->

## 1.1. 入门 

### 1.1.1. 环境准备

需安装vscode软件，并安装markdown preview enhanced插件。本篇markdown文件也需要在此环境下打开，才能看到预期效果。

## 1.2. 语法

### 1.2.1. 强调

*这会是 斜体 的文字*
_这会是 斜体 的文字_
**这会是 粗体 的文字**
__这会是 粗体 的文字__
_你也 **组合** 这些符号_
~~这个文字将会被横线删除~~

### 1.2.2. 插入代码

```c {.line-numbers}
int a=0;
int b=0;
```

- 在插入代码时可以指定当前代码是什么语言，以便预览时可以将关键词用特殊颜色标记
- 在插入代码时可以显示行号：{.line-numbers}


### 1.2.3. 行内代码

我觉得你应该在这里使用 `<addr>` 才对。

### 1.2.4. Emoji & Font-Awesome

:smile: 
:fa-car:

### 1.2.5. 上标

30^th^

### 1.2.6. 下标

H~2~O

### 1.2.7. 脚注

Content [^1]
[^1]: Hi! This is a footnote

### 1.2.8. 标记

==marked==

### 1.2.9. 缩略

*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium
The HTML specification is maintained by the W3C.

### 1.2.10. 任务列表

- [x] 写代码
- [ ] 做笔记

### 1.2.11. 目录列表

Markdown Preview Enhanced 支持你在 markdown 文件中创建 TOC。你可以通过 cmd-shift-p 然后选择 Markdown Preview Enhanced: Create Toc 命令来创建 TOC。多个 TOCs 可以被创建。如果你想要在你的 TOC 中排除一个标题，请在你的标题后面添加{ignore=true} 即可。

### 1.2.12. 表格

**极简方式** 

name | 价格 |  数量  
-|-|-
1 | 1 | 5 |
1 | 1 | 6 |
1 | 1 | 7 |

**简单方法** 

name | 111111 | 222222 | 333333 | 444444
- | :-: | :-: | :-: | -:
a | b | c | d | e| 
f | g| h | i | 0|

**原生方法** 

name | 111111 | 222222 | 333333 | 444444
:-: | :-: | :-: | :-: | :-:
a | b | c | d | e| 
f | g| h | i | 0|

**语法说明** 

1. |、-、:之间的多余空格会被忽略，不影响布局。
1. 默认标题栏居中对齐，内容居左对齐。
1. -:表示内容和标题栏居右对齐，:-表示内容和标题栏居左对齐，:-:表示内容和标题栏居中对齐。
1. 内容和|之间的多余空格会被忽略，每行第一个|和最后一个|可以省略，-的数量至少有一个。

## 1.3. 参考资料
1. [markdown preview enhanced 官方文档](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)
2. 
