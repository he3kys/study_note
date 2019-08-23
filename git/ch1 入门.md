# Git

## 入门

### 创建分支

从develop分支创建一个feature分支

> git checkout -b feature develop

### 合并分支

将feature分支合并到develop分支

> git checkout develop
> git merge --no-ff feature

### 删除分支

> git branch -d feature

## 参考文档

- [Git分支管理策略](http://www.ruanyifeng.com/blog/2012/07/git.html)
