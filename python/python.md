[toc]

### 替换文件中的指定文本

**适用场景**

1. 当一个文本文件中存在中文时，如果需要替换文件中的指定文字时可以采用此种方式

**特点**

1. 可以指定当前文本的编码方式

**代码**

```python {.line-numbers}
import codecs

with codecs.open('test.md', 'r', 'utf-8') as f_source:
	contents = f_source.read()
	contents = contents.replace("```c {.line-numbers}", "\\begin{lstlisting}[language={c}]")
	contents = contents.replace("```", "\end{lstlisting}")
	f_source.close()
	with codecs.open('test.md', 'w', 'utf-8') as f_final:
		f_final.write(contents)
```

**流程**

1. 以只读方式打开
1. 读取文件内容到字符串中
1. 采用字符串替换的方式替换掉指定字符串
1. 关闭文件
1. 以只写的方式打开文件
1. 将替换后的字符串写入文件

**说明**

1. 不能采用读写的方式操作，会报错
1. 用with的方式打开文件可以不需要关闭

### 查找未包含在NewFW_SVN.uvprojx工程中的.c文件

**适用场景**

1. keil工程中存在大量无用的c源文件时，可以采用此脚本找到哪些文件未包含在工程中，以便将其删除

```python {.line-numbers}
import os

project_path = r"D:\Home\edison\ee_std\fw\project\func"
# .c文件列表
# item0：当前文件所在文件夹
# item1：文件名
# item2：文件完整路径
file_list = []

# 不在uvprojx中的.c文件列表
c_file_list_not_exist = []

for foldername,subfolders,filenames in os.walk(project_path+"\\User"):
    for filename in filenames :
        if str(filename).endswith(".c"):
            file_list.append([str(foldername),str(filename),str(foldername)+"\\"+str(filename)])

with open(project_path+"\\Project\\NewFW_SVN.uvprojx","r") as projectfile:
    filecontent = projectfile.read()
    for curfile in file_list:
        if curfile[1] not in filecontent :
            c_file_list_not_exist.append(curfile)

for item in c_file_list_not_exist :
    print("\""+item[2]+"\",")

print(len(c_file_list_not_exist))

```

**知识点**

os.walk 函数：

1. 作用：遍历目录树

1. 输入参数：os.walk()函数被传入一个字符串值，即一个文件夹的路径

1. os.walk()在循环的每次迭代中返回三个值：

	1. 当前文件夹名称的字符串

	1. 当前文件夹中所有子文件夹的字符串的列表

	1. 当前文件夹中所有文件的字符串的列表

### 将列表内的指定文件删除到回收站

利用 send2trash，比 Python 常规的删除函数要安全得多，因为它会将文件夹和文件发送到计算机的垃圾箱或回收站，而不是永久删除它们。如果因程序缺陷而用
send2trash 删除了某些你不想删除的东西，稍后可以从垃圾箱恢复。

```python {.line-numbers}
import os
import send2trash

fileDir = r'D:\Home\edison\ee_std\fw\project\func\Project\Obj'

files = ["api_lib.d"]

os.chdir(fileDir)

for i in range(len(files)):
    filePath = fileDir+"\\"+files[i]
    print(filePath)
    send2trash.send2trash(filePath)

```
