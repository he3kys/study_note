
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 入门](#1-入门)
    - [1.0.1. 创建文件夹](#101-创建文件夹)
    - [1.0.2. 创建分支](#102-创建分支)
    - [1.0.3. 合并分支](#103-合并分支)
    - [1.0.4. 删除分支](#104-删除分支)
- [2. submodule](#2-submodule)
- [3. FAQ](#3-faq)
    - [3.0.5. gitignore 文件不生效](#305-gitignore-文件不生效)
- [4. 相关资料](#4-相关资料)
  - [参考文档](#参考文档)
  - [相关软件](#相关软件)

<!-- /code_chunk_output -->

# 1. 入门

### 1.0.1. 创建文件夹

在commit时，git对空文件夹是忽略的，因此不能直接创建一个空文件夹，需要在文件夹里面添加文件后才能被git识别。

### 1.0.2. 创建分支

从develop分支创建一个feature分支

> git checkout -b feature develop

### 1.0.3. 合并分支

将feature分支合并到develop分支

> git checkout develop
> git merge --no-ff feature

参考：
[git-merge完全解析](https://www.jianshu.com/p/58a166f24c81)

### 1.0.4. 删除分支

项目初始，为了实现不同的功能，不同人员处理不同的功能，所以在git上创建了很多分支（branch）。对于git菜鸟，只会add branch 或者Git commit, 不会删除git分支也是一个烦恼。

- 删除本地分支：git branch -d 分支名称
- 强制删除本地分支：git branch -D 分支名称
- 删除远程分支：git push origin --delete 分支名称

> git branch -d developbranch
> git branch -D developbranch
> git push origin --delete developbranch

注意：删除分支就不可以撤销。删除分支前需要慎重。

# 2. submodule

# 3. FAQ 

### 3.0.5. gitignore 文件不生效

.gitignore只能忽略那些原来没有被追踪的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。那么解决方法就是先把本地缓存删除（改变成未被追踪状态），然后再提交：


```batch {.line-numbers}
git rm -r --cached .
git add .
git commit -m 'update .gitignore'
```


# 4. 相关资料

## 参考文档

1. [Git分支管理策略](http://www.ruanyifeng.com/blog/2012/07/git.html)
1. [官方图书和文档](https://git-scm.com/book/zh/v2)
1. [菜鸟教程](https://www.runoob.com/git/git-tutorial.html)
1. [廖雪峰的博客](https://www.liaoxuefeng.com/wiki/896043488029600)
1. [图解git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html?no-svg)
1. [动画学git](https://learngitbranching.js.org/)

## 相关软件

- GIT客户端：[SourceTree](https://www.sourcetreeapp.com/) 颜值高，功能非常强大
- GIT客户端：[Tower Pro](https://www.git-tower.com/) 颜值高，功能非常强大

