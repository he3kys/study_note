
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [1. 入门](#1-入门)
    - [1.0.1. 创建文件夹](#101-创建文件夹)
    - [1.0.2. 创建分支](#102-创建分支)
    - [1.0.3. 合并分支](#103-合并分支)
    - [1.0.4. 删除分支](#104-删除分支)
- [2. submodule](#2-submodule)
- [3. 参考文档](#3-参考文档)

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

### 1.0.4. 删除分支

> git branch -d feature

# 2. submodule


# 3. 参考文档

- [Git分支管理策略](http://www.ruanyifeng.com/blog/2012/07/git.html)
