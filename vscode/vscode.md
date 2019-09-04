# 1. VSCode学习笔记


<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1.1. 配置](#11-配置)
  - [1.1.1. settings](#111-settings)
  - [1.1.2. snippets : c.json](#112-snippets-cjson)
  - [1.1.3. snippets : markdown.json](#113-snippets-markdownjson)
  - [1.1.4. snippets中可以使用的变量](#114-snippets中可以使用的变量)
- [1.2. 插件](#12-插件)
  - [1.2.1. Markdown TOC](#121-markdown-toc)
  - [1.2.2. Markdown preview enhanced](#122-markdown-preview-enhanced)
    - [1.2.2.1. 为markdown文件添加目录](#1221-为markdown文件添加目录)

<!-- /code_chunk_output -->


## 1.1. 配置

### 1.1.1. settings

在vscode中按下Ctrl+Shit+P，然后输入settings,选择preferences:open settings(JSON)，打开配置文件

```json {.line-numbers}
{
    "python.pythonPath": "C:\\Users\\01295\\AppData\\Local\\Programs\\Python\\Python36\\python.exe",
    "python.jediEnabled": false,
    "C_Cpp.updateChannel": "Insiders",
    "markdown-pdf.executablePath": "C:\\Users\\01295\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe",
    "git.autofetch": true,
    
    "[markdown]": {
        "editor.formatOnSave": true,
        "editor.renderWhitespace": "all",
        "editor.quickSuggestions": {
            "other": true,
            "comments": true,
            "strings": true
        },
        "editor.acceptSuggestionOnEnter": "on"
    },
    "window.zoomLevel": 0,
    "markdown.extension.print.absoluteImgPath": false,
	"markdown-preview-enhanced.previewTheme": "newsprint.css",
	"markdown-toc.depthFrom": 2,
	"editor.minimap.enabled": true,
}
```

### 1.1.2. snippets : c.json

点击左下角配置按钮 → user snippets → 选择c.json

```json {.line-numbers}
{
	"rt_sem_init":{
		"description": "信号量初始化",
		"prefix": "semi",
		"body": [
			"err=rt_sem_init(&$1,\"$2\",$3,RT_IPC_FLAG_FIFO);",
			"if(err != RT_EOK)",
			"{",
			"    rt_kprintf(\"trig $2 test sem init fail !\\n\");",
			"    RT_ASSERT(err == RT_EOK);",
			"}",
			"$0"
		]
	},
	"rt_sem_take : waiting forever":{
		"description": "永久等待一个信号量",
		"prefix": "semtwf",
		"body": [
			"rt_sem_take(&$1, RT_WAITING_FOREVER);",
			"$0"
		]
	},
	"rt_sem_take : waiting n ms":{
		"description": "等待信号量n ms",
		"prefix": "semtwnm",
		"body": [
			"err = rt_sem_take(&$1, MSec($2));",
			"$0"
		]
	},
	"rt_sem_trytake":{
		"description": "清空信号量",
		"prefix": "semtt",
		"body": [
			"while(rt_sem_trytake(&$1)==RT_EOK);",
			"$0"
		]
	},
	"rt_thread_init":{
		"description": "线程初始化:包括变量定义，初始化，线程入口函数创建",
		"prefix": "threadi",
		"body": [
			"#define RT_$1_THREAD_PRIO 21",
			"struct rt_thread $2_thread;",
			"rt_uint8_t $2_stack[1024];",
			"extern void $2_thread_entry(void *parameter);",
			"$0",
			"result = rt_thread_init(&$2_thread,\"$2\", $2_thread_entry, RT_NULL, (rt_uint8_t *)&$2_stack[0], sizeof($2_stack), RT_$1_THREAD_PRIO, 20);",
			"if (result == RT_EOK)",
			"{",
			"    rt_thread_startup(&$2_thread);",
			"    rt_kprintf(\"$2 thread start \\n\");",
			"}",
			"",
			"void $2_thread_entry(void *parameter)",
			"{",
			"    while(1)",
			"    {",
			"        rt_thread_delay(MSec(10));",
			"    }",
			"}"
		]
	},
	"variable : rt_semaphore":{
		"description": "定义一个信号量",
		"prefix": "vsem",
		"body": [
			"struct rt_semaphore $1;",
			"$0"
		]
	},
	"variable : err":{
		"description": "定义局部变量err",
		"prefix": "verr",
		"body": [
			"rt_err_t err;",
			"$0"]
	},
}
```

### 1.1.3. snippets : markdown.json

点击左下角配置按钮 → user snippets → 选择markdown.json

```json {.line-numbers}
{
	"insert url":
	{
		"description": "插入超链接",
		"prefix": "url",
		"body": ["[$1]($2)"],
	},
	"insert png Fig":
	{
		"description": "插入图片",
		"prefix": "figp",
		"body": ["","![$1](./Fig/$2.png){#fig:$2}","$0"],
	},
	"insert gif Fig":
	{
		"description": "插入图片",
		"prefix": "figg",
		"body": ["","![$1](./Fig/$2.png){#fig:$2}","$0"],
	},
	"insert png Fig for wiki":
	{
		"description": "插入图片",
		"prefix": "figpw",
		"body": ["","![$1](uploads/Fig/$2.png){#fig:$2}","$0"],
	},
	"insert gif Fig for wiki":
	{
		"description": "插入图片",
		"prefix": "figgw",
		"body": ["","![$1](uploads/Fig/$2.gif){#fig:$2}","$0"],
	},
	"code block of c":
	{
		"description": "插入c代码块",
		"prefix": "cc",
		"body": ["","```c {.line-numbers}","$1","```","$0"],
	},
	"code block of java":
	{
		"description": "插入java代码块",
		"prefix": "cj",
		"body": ["","```java {.line-numbers}","$1","```","$0"],
	},
	"code block of javascript":
	{
		"description": "插入javascript代码块",
		"prefix": "cjs",
		"body": ["","```javascript {.line-numbers}","$1","```","$0"],
	},
	"code block of html":
	{
		"description": "插入html代码块",
		"prefix": "ch",
		"body": ["","```html {.line-numbers}","$1","```","$0"],
	},
	"code block of batch":
	{
		"description": "插入batch代码块",
		"prefix": "cb",
		"body": ["","```batch {.line-numbers}","$1","```","$0"],
	},
	"code block of json":
	{
		"description": "插入json配置",
		"prefix": "cjson",
		"body": ["","```json {.line-numbers}","$1","```","$0"],
	},
	"insert bold text":
	{
		"description": "插入加粗文本",
		"prefix": "bt",
		"body": ["**$1**$0 "],
	},
	"insert todo list":
	{
		"description": "插入待办事项",
		"prefix": "td",
		"body": ["- [ ] "],
	},
}
```
### 1.1.4. snippets中可以使用的变量

The following variables can be used:

	TM_SELECTED_TEXT The currently selected text or the empty string
	TM_CURRENT_LINE The contents of the current line
	TM_CURRENT_WORD The contents of the word under cursor or the empty string
	TM_LINE_INDEX The zero-index based line number
	TM_LINE_NUMBER The one-index based line number
	TM_FILENAME The filename of the current document
	TM_FILENAME_BASE The filename of the current document without its extensions
	TM_DIRECTORY The directory of the current document
	TM_FILEPATH The full file path of the current document
	CLIPBOARD The contents of your clipboard
	WORKSPACE_NAME The name of the opened workspace or folder

For inserting the current date and time:

    CURRENT_YEAR The current year
    CURRENT_YEAR_SHORT The current year’s last two digits
    CURRENT_MONTH The month as two digits (example ‘02’)
    CURRENT_MONTH_NAME The full name of the month (example ‘July’)
    CURRENT_MONTH_NAME_SHORT The short name of the month (example ‘Jul’)
    CURRENT_DATE The day of the month
    CURRENT_DAY_NAME The name of day (example ‘Monday’)
    CURRENT_DAY_NAME_SHORT The short name of the day (example ‘Mon’)
    CURRENT_HOUR The current hour in 24-hour clock format
    CURRENT_MINUTE The current minute
    CURRENT_SECOND The current second

For inserting line or block comments, honoring the current language:

    BLOCK_COMMENT_START Example output: in PHP /* or in HTML <!–
    BLOCK_COMMENT_END Example output: in PHP */ or in HTML -->
    LINE_COMMENT Example output: in PHP // or in HTML <!-- -->


```json {.line-numbers}

"c_header": {
        "prefix": "c_header",
        "body": [
            "/**",
            " * Copyright © 2019 Silvester. All rights reserved.",
            " * ",
            " * @author: Silvester",
            " * @date: $CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE ",
            " */",
            "#include <stdio.h>",
            "#include <stdlib.h>",
            "#include <string.h>",
            "",
            "int main() {",
            "    /****** your code ******/",
            "    $0",
            "    return 0;",
            "}"
        ]
        // "description": "Log output to console"
    }
```

```c {.line-numbers}

/**
 * Copyright © 2019 Silvester. All rights reserved.
 * 
 * @author: Silvester
 * @date: 2019-05-20 
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    /****** your code ******/
    
    return 0;
}
```


## 1.2. 插件

### 1.2.1. Markdown TOC

**功能：**
- 为标题增加序号
- 生成目录
- 最好选择1.5.5版本，可以实现一级标题不参与编号

**从二级标题开始编号**

在编写markdown文档时，经常会以一级作为首行，如果为此一级标题添加编号，则所有标题都会以1.开头，影响视觉，可以从二级标题开始进行编号，此时需要在settings中增加如下配置：

```json {.line-numbers}
"markdown-toc.depthFrom": 2,
```

**为标题插入编号**

点击右键 → 点击markdown sections:insert/update

*注：1.5.5版本插入目录时会错乱，建议使用markdown preview enhanced添加目录*

### 1.2.2. Markdown preview enhanced

#### 1.2.2.1. 为markdown文件添加目录

将光标定位到需要插入目录的位置 → 按Ctrl+Shift+P调出命令面板 → 输入toc → 选择Markdown preview enhanced:Ctreate TOC → 配置depthFrom=2，让目录从二级标题开始生成 → 点击Ctrl+S生成目录

