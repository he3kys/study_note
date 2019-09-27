
### 替换文件中的指定文本

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

流程：

1. 以只读方式打开
1. 读取文件内容到字符串中
1. 采用字符串替换的方式替换掉指定字符串
1. 关闭文件
1. 以只写的方式打开文件
1. 将替换后的字符串写入文件

说明：

1. 不能采用读写的方式操作，会报错
1. 用with的方式打开文件可以不需要关闭

