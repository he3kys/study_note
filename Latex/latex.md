
# 学习笔记：latex中文教程-15集 从入门到精通包含各种latex操作

- 视频地址：在bilibili可找到

## latex源文件基本构成


```latex {.line-numbers}
%导言区
\documentclass{book} %article,book,report,letter , 可以通过修改文档类修改显示格式

% 标题
\title{My First Document}
\author{Me}
\date{\today}

%正文区
\begin{document}
\maketitle %输出标题
    hello world ! 

    % 单$模式包含的数学公式显示在当前行   
    let $f(x)$ be defined by the formular 
    $f(x)=3x^2+x-1$

    % 双$$模式包含的数学公式单独显示一行  
    let $f(x)$ be defined by the formular 
    $$f(x)=3x^2+x-1$$


\end{document}

```

## latex中的中文处理办法

编码需要采用utf-8，解析引擎需要用xelatex

打开ctex说明文档：在命令行中输入:
> texdoc ctex



# 资料

## 参考文档

1. [LaTeX开源小屋](https://www.latexstudio.net/)