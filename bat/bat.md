# 入门

### 移动文件到文件夹

如果文件夹不存在需要先建立文件夹，然后调用move指令移动文件

```batch
if not exist include mkdir include
move *.h include
exit
```

### 复制文件到文件夹

如果文件夹不存在需要先建立文件夹，然后调用copy指令复制文件

```batch
if not exist include mkdir include
copy *.h include
exit
```
