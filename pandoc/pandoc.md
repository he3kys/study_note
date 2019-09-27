# 将markdown转为pdf

如下批处理命令是将stdfw_user_manual.md文件转化为stdfw_user_manual.pdf文件。
> pandoc --pdf-engine=xelatex --toc -f markdown+fenced_code_blocks --template=yanmade.latex -N  -V documentclass=ym_article stdfw_user_manual.md  -o stdfw_user_manual.pdf 

其中：

- --pdf-engine=xelatex：将markdown转换为pdf时采用xelatex引擎
- -f markdown+fenced_code_blocks：采用pandoc markdown扩展命令fenced_code_blocks（此处没什么用处）
- --template=yanmade.latex：采用yanmade.latex作为latex模板
- -N：表示在标题前面增加编号
- -V documentclass=ym_article ：documentclass采用自定义的ym_article.cls
- stdfw_user_manual.md  -o stdfw_user_manual.pdf  ： 指定输入和输出文件，如果输入文件存在多个，则会将所有输入文件按照顺序组合成一个文件输出

*注：使用此条命令时，需要将ym_article.cls，yanmade.latex等文件copy到stdfw_user_manual.md路径下*

