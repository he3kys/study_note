[toc]

# 总结

![git常用命令](./Fig/GitCommonCommand.png){#fig:GitCommonCommand}

## 分支操作

git常用分支开发模型：

- develop分支：频繁变化的一个分支
- test分支：供测试与产品等人员使用的一个分支，变化不是特别频繁
- master分支：生产发布分支，变化非常不频繁的分支
- bugfix分支：生产系统中出现了紧急bug，用于紧急修复多的分支
- hotfix分支：master分支上出现了严重bug，需要紧急修复，修复完后需要立马合并的master分支进行发布，类似于补丁发布

### 创建分支

```bash {.line-numbers}
# 从当前分支创建doe分支并切换到doe分支
git checkout -b doe 

# 从develop分支创建一个feature分支，并跳转到feature分支
git checkout -b feature develop

# 从指定分支创建分支
# 示例：基于远程origin/develop创建分支develop
git checkout -b develop origin/develop
```

### 分支切换


```bash {.line-numbers}

# 返回到上一个分支
git checkout -

# 切换到dev分支
git checkout dev

```

### 合并分支

```bash {.line-numbers}
# 将doe分支合并到当前分支，假如当前在master分支，则会将doe合并到master分支上
git merge doe
```

参考：
[git-merge完全解析](https://www.jianshu.com/p/58a166f24c81)

### 删除分支

常用删除分支操作：

- 删除本地分支：git branch -d 分支名称
- 强制删除本地分支：git branch -D 分支名称
- 删除远程分支：git push origin --delete 分支名称

```bash {.line-numbers}
# 删除本地分支 developbranch
git branch -d developbranch

# 强制删除本地分支developbranch
git branch -D developbranch

# 删除远程分支developbranch
git push origin --delete developbranch
```

注意：删除分支就不可以撤销。删除分支前需要慎重。

### rebase

rebase 一般用于整理提交信息，让提价信息看起来更加线性化

```bash {.line-numbers}
# 将doe分支合并到dev分支
# 步骤：
# 1. 切换到dev分支
# 2. 调用git rebase -i doe

# 将本分支的前几次提交压缩为一个提交
# 步骤：
# 1. git rebase -i commtid  或者 git rebase -i HEAD~2
# 2. git会自动调出vim，需要在vim中选择需要压缩或者保留的分支，如果需要保留就选择pick，如果需要压缩就选择s
# 3. 解决冲突 -> 将冲突文件add到版本库 -> git rebase --continue 
# 4. 填写rebase信息
# 5. 强制推送 git push -f 

```

### 版本回退

```bash {.line-numbers}
# 回退到上一个版本
git reset --hard HEAD^

# 回退两个版本
git reset --hard HEAD^^

# 回退到指定提交
# 格式：git reset --hard commitID简写
git reset --hard 47d3

# 回到之前的第n个提交
# 格式：git reset --hard HEAD~n
git reset --hard HEAD~3
```

### 其它操作


```bash {.line-numbers}
# 分支改名
# 说明：将doe分支的名字改为doe1
git branch -m doe doe1

# 设置别名
git config --global alias.br branch

```


## 文件操作

对于git工程，只有一个.git文件夹用于保存版本库信息，不像SVN在每个文件夹下都有一个.svn文件夹

```bash {.line-numbers}
# 回到上层目录
cd ..

# 回到home路径
cd ~

# 创建文件夹
mkdir temp_test

# 进入.git子目录
cd .git

# 列出当前路径下的所有文件及文件夹
ls -al

# 查看当前目录：
pwd

# 创建文件
touch test.txt

# 查看文件内容：
cat test.txt

# 用vi编辑器编辑readme.md
vi README.md

# 递归删除.git文件夹下的所有文件
rm -rf .git

# 将字符串hello Word 输出到文件hello.txt中，此操作会直接创建hello.txt
echo 'hello world' > hello.txt


```

## 状态变迁

文件的三种状态：

- 已修改(modified) ： 对应的是工作区
- 已暂存(staged) ： 对应的是暂存区
- 已提交(committed) ：对应的是本地仓库

![git文件状态](./Fig/GitFileStatus.png){#fig:GitFileStatus}


### 工作区和暂存区间的迁移

git add的作用
1. 将未跟踪的文件添加到跟踪列表
1. 将已经被追踪的文件纳入缓存区中
1. 冲突修改完后，用此命令标识冲突已解决

```bash {.line-numbers}

# 舍弃刚才进行的修改，使之与暂存区中的内容保持一致
# 实验过程：
# 1. 修改readme.md文件并保存
# 2. 调用git checkout命令舍弃掉刚才的修改
# 命令格式：
# git checkout -- 文件名称
git checkout -- README.md

# 将文件添加到暂存区
git add test.txt

# 将所有已修改的文件加入到暂存区
git add .

# 将之前添加到暂存区(stage,index)的内容回退到工作区
# 实验过程：
# 1. 修改readme.md文件并保存
# 2. 调用git add README.md 命令将readme.md文件从工作区添加到暂存区
# 3. 调用git reset HEAD README.md 命令将readme.md从暂存区回退到工作区
vi README.md
git add README.md
git reset HEAD README.md

```

### 暂存区和本地仓库间的迁移

git 的commitid是一个摘要，这个摘要值根据sha1计算出来的

```bash {.line-numbers}
# 将文件从暂存区提交到本地仓库
git commit 

# 提交时带上简明信息
git commit -m 'init commit'

# add与commit合二为一
git commit -am 'add hello world to readme.md'

```

### 远程仓库

push ：推送
pull：拉取，同时会执行合并 = fetch + merge

```bash {.line-numbers}
# 采用公钥的方式访问github
# 步骤：
# 1. 采用git remote add设置ssh形式的远程git地址
# 2. 查看本地公钥
# 3. 生成公钥和私钥
# 4. 将公钥.pub里的内容放到github上
git remote add origin git@github.com:gitlecture/gitlecture.git
cat ~/.ssh/known_hosts
ssh-keygen


# 将本地已有仓库推送到指定远程仓库
# 步骤
# 1. 调用git remote add命令设置一个远程仓库
# 2. 将本地master分支和远程master分支做关联
git remote add origin https://github.com/gitlecture/gitlecture.git
git push -u origin master 

# clone 仓库
git clone git@192.168.0.98:KangYashuai_01295/temp.git

# git pull时出现冲突时的解决流程
# 1. 用编辑器获取其它编辑器修改冲突部分，冲突部分git会做标记
# 2. 查看哪些文件哪些行发生冲突：git diff
# 2. 修改完冲突后调用git add命令标识当前冲突已解决
# 3. 调用git commit命令提交修改，git commit后面不需要增加其他参数，会自动进入冲突合并信息中
01295@CY-20180208PUBU MINGW64 ~/temp/temp_test/temp (doe|MERGING)
git diff
vi README.md
git add README.md
git commit

```


### 临时保存


```bash {.line-numbers}

# 将修改的内容临时保存
# 使用场景：当在dev分支上正在开发某个功能，此时需要切换到master分支，此时由于修改的内容还没有add到暂存区，所以会禁止切换到master分支。但由于还没有开发完又不想调用add命令将其添加到暂存区，此时就可以用stash命令将dev分支上修改的内容临时保存。
# 实验过程：
# 1. 调用git checkout doe命令切换到doe分支
# 2. 修改readme.md文件并保存
# 3. 调用git stash命令将修改的内容临时缓存
# 4. 调用 git checkout master命令切换到doe分支（此时可以成功切换到master分支）
# 5. 调用git stash pop命令将之前临时保存的内容恢复到工作区
git stash
vi README.md # 当前在test分支，修改readme文件
git checkout master # 此时调用checkout切换到master会报错
git stash # 将修改的内容临时保存
git checkout master # 此时可以顺利切换到master进行其它开发
git checkout test # 在master上开发完后再切回test分支
git st # 显示工作区是干净的
git stash pop # 调用此命令将刚才临时保存的内容恢复到工作区，显示readme.md文件处于modified状态


```

## 标签

- 标签有两种：轻量级标签（lightweight）与带有附注的标签（annotated）
- 创建一个轻量级的标签：git tag V1.0.1
- 创建一个带有附注的标签：git tag -a v1.0.2 -m 'release version'
- 删除标签：git tag -d tag_name


```bash {.line-numbers}

# 添加标签
git tag V1.0.0

# 删除标签
git tag -d V1.0.0

# 查看标签
git tag

# 查找标签（支持常见的正则表达式）
git tag -l 'V1.0'
git tag -l 'V1*'

# 带注释的标签
git tag V2.0 -m 'V2.0 release '

# 显示指定标签信息
git show V1.0

# 将标签推送到远程
# 示例：将V1.0的标签推送到远程
git push origin V1.0

# 示例：将V2.0，V3.0的标签推送到远程
git push origin V2.0 V3.0

# 示例：将所有标签推送到远程
git push origin --tags

# 删除远程仓库的标签
git push origin --delete tag V1.0

# 删除本地标签
git tag -d V1.0

```

## 比较

```bash {.line-numbers}

# 比较暂存区和工作区的差别
# 实验方法：
# 1. 修改readme.md并保存
# 1. 调用git diff命令比较工作区和暂存区的区别
# 
# 输出说明：
# --- a/README.md （三个减号表示原文件，也就是暂存区中的文件）
# +++ b/README.md（三个加号表示目标文件，也就是工作区中的文件）
# @@ -3,3 +3,5 @@ test （前面的-3表示原文件从第3行开始存在差异，后面的3表示总共有三行，后面的+3表示目标文件从 第三行开始存在差异，总共有5行）
git diff

# 比较最新提交和工作区之间的差别
git diff HEAD

# 比较指定提交和工作区之间的差别
# 命令格式：git diff commitID
git diff cb62915

# 比较最新提交和暂存区之间的区别
git diff --cached

# 比较指定提交和暂存区之间的区别
git diff --cached cb62915

```

## 其它

### 查看信息

```bash {.line-numbers}
# 查看提交日志
git log

# 查看最近3条日志
git log -3

# 以图形化的方式查看log
git log --graph

# commitID采用缩写方式显示
git log --graph --abbrev-commit

# commit信息用单行的方式显示
git log --graph --pretty=oneline --abbrev-commit

# 显示用户操作日志：此方式会将用户所有操作过程全部记录下来
git reflog

# 显示各分支最近一次提交信息
git branch -v

# 查看命令的帮助信息
# 格式：在命令的后面加上--help即可
git --help
git checkout --help

# 查看git版本：打开cmd，输入
git --version

# 查看某个文件的修改历史
git blame README.md

# 查看可执行程序所在路径
# 语法格式：which 可执行文件名字
which git

# 打开gitk界面
gitk

# 打开git gui界面
git gui

# 查看config文件的内容
git config --list

# 显示远程仓库
# 当存在多个远程仓库时，可以调用此命令显示远程仓库的名字
git remote show

# 查看环境变量
echo $PATH

# 查看本地和远程分支信息
git branch -a
git branch -av

# 查看本地配置文件
git config --local --list

# 查看全局配置文件
git config --list

# 查看本地分支和远程分支的关系
git remote show origin

# 查看工作区状态
git status

```

### 用户信息配置

对于user.name与user.email来说有三个地方可以设置：

- /etc/gitconfig : 整个计算机的范围，也就是无论这台电脑有多少用户，都用这一个设置（几乎不会使用）,配置方式为：git config --system
- ~/.gitconfig : 用户主目录（经常使用）,配置方式为：git config --global
- 针对于特定项目的，在当前工程的.git/config文件中，配置方式为：git config --local


```bash {.line-numbers}
# 设置本地名字
git config --local user.name 'test'

# 设置本地邮箱地址
git config --local user.email 'test@qq.com'
```


# 《深入理解git》学习笔记

视频来源：哔哩哔哩
讲师：风中叶

**git 裸库与submodule**


```bash {.line-numbers}
# 添加一个submodule
# 示例：将远程仓库stdlib添加本仓库
git submodule add git@192.168.0.98:ee_group/fw_lib/stdlib.git

# 添加一个submodlue到指定文件夹
# 示例：将远程仓库stdlib添加本仓库FWLib文件夹中
git submodule add git@192.168.0.98:ee_group/fw_lib/stdlib.git FWLib

# 更新所有子模块
git submodule foreach git pull

# 克隆带submodule的仓库
git submodule add git@192.168.0.98:ee_group/fw_lib/stdlib.git FWLib --recursive

# 删除指定submodule

```

**Mac操作**

命令行工具：
> bash : 自带的
> zsh ：强大但不宜用
> on my zsh  ： 强大美观易用

清屏：
> Ctrl+L 或者 clear

**资源**

- GitBook ： 采用markdown语法


# FAQ 

## gitignore 文件不生效

.gitignore只能忽略那些原来没有被追踪的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。那么解决方法就是先把本地缓存删除（改变成未被追踪状态），然后再提交：


```bash {.line-numbers}
git rm -r --cached .
git add .
git commit -m 'update .gitignore'
```

# 参考资料

## 网站
1. [git官网](http://www.git-scm.com)
1. [Git分支管理策略](http://www.ruanyifeng.com/blog/2012/07/git.html)
1. [官方图书和文档](https://git-scm.com/book/zh/v2)
1. [菜鸟教程](https://www.runoob.com/git/git-tutorial.html)
1. [廖雪峰的博客](https://www.liaoxuefeng.com/wiki/896043488029600)
1. [图解git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html?no-svg)
1. [动画学git](https://learngitbranching.js.org/)

## 文档

## 视频

1. [深入理解git](https://www.bilibili.com/video/av52286788?from=search&seid=3315075663787750735) ：哔哩哔哩-风中叶

## 相关软件

- GIT客户端：[SourceTree](https://www.sourcetreeapp.com/) 颜值高，功能非常强大
- GIT客户端：[Tower Pro](https://www.git-tower.com/) 颜值高，功能非常强大

