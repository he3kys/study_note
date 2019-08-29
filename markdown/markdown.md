# Markdown学习笔记 

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 入门](#1-入门)
  - [1.1. 环境准备](#11-环境准备)
- [2. 语法](#2-语法)
  - [2.1. 强调](#21-强调)
  - [2.2. 插入代码](#22-插入代码)
  - [2.3. 行内代码](#23-行内代码)
  - [2.4. Emoji & Font-Awesome](#24-emoji-font-awesome)
  - [2.5. 上标](#25-上标)
  - [2.6. 下标](#26-下标)
  - [2.7. 脚注](#27-脚注)
  - [2.8. 标记](#28-标记)
  - [2.9. 缩略](#29-缩略)
  - [2.10. 任务列表](#210-任务列表)
  - [2.11. 目录列表](#211-目录列表)
- [4. 参考资料](#4-参考资料)

<!-- /code_chunk_output -->

## 1. 入门 

### 1.1. 环境准备

需安装vscode软件，并安装markdown preview enhanced插件。本篇markdown文件也需要在此环境下打开，才能看到预期效果。

## 2. 语法

### 2.1. 强调

*这会是 斜体 的文字*
_这会是 斜体 的文字_
**这会是 粗体 的文字**
__这会是 粗体 的文字__
_你也 **组合** 这些符号_
~~这个文字将会被横线删除~~

### 2.2. 插入代码

```c {.line-numbers}
int a=0;
int b=0;
```

- 在插入代码时可以指定当前代码是什么语言，以便预览时可以将关键词用特殊颜色标记
- 在插入代码时可以显示行号：{.line-numbers}


### 2.3. 行内代码

我觉得你应该在这里使用 `<addr>` 才对。

### 2.4. Emoji & Font-Awesome

:smile: 
:fa-car:

### 2.5. 上标

30^th^

### 2.6. 下标

H~2~O

### 2.7. 脚注

Content [^1]
[^1]: Hi! This is a footnote

### 2.8. 标记

==marked==

### 2.9. 缩略

*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium
The HTML specification is maintained by the W3C.

### 2.10. 任务列表

- [x] 写代码
- [ ] 做笔记

### 2.11. 目录列表

Markdown Preview Enhanced 支持你在 markdown 文件中创建 TOC。你可以通过 cmd-shift-p 然后选择 Markdown Preview Enhanced: Create Toc 命令来创建 TOC。多个 TOCs 可以被创建。如果你想要在你的 TOC 中排除一个标题，请在你的标题后面添加{ignore=true} 即可。

## 4. 参考资料
1. [markdown preview enhanced 官方文档](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)
2. 
