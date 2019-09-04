# HTML+CS学习笔记


<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [HTML+CS学习笔记](#htmlcs%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b0)
  - [1. 简介](#1-%e7%ae%80%e4%bb%8b)
  - [2. 开发环境入门](#2-%e5%bc%80%e5%8f%91%e7%8e%af%e5%a2%83%e5%85%a5%e9%97%a8)
  - [3. HTML基本语法](#3-html%e5%9f%ba%e6%9c%ac%e8%af%ad%e6%b3%95)
    - [3.1. 常见元素](#31-%e5%b8%b8%e8%a7%81%e5%85%83%e7%b4%a0)
    - [3.2. 空元素](#32-%e7%a9%ba%e5%85%83%e7%b4%a0)
    - [3.3. 元素嵌套](#33-%e5%85%83%e7%b4%a0%e5%b5%8c%e5%a5%97)
    - [3.4. 文档声明](#34-%e6%96%87%e6%a1%a3%e5%a3%b0%e6%98%8e)
    - [3.5. 根元素](#35-%e6%a0%b9%e5%85%83%e7%b4%a0)
    - [3.6. href属性](#36-href%e5%b1%9e%e6%80%a7)
    - [3.7. target属性](#37-target%e5%b1%9e%e6%80%a7)
    - [3.8. 路径](#38-%e8%b7%af%e5%be%84)
    - [3.9. img元素](#39-img%e5%85%83%e7%b4%a0)
    - [3.10. src(路径)属性](#310-src%e8%b7%af%e5%be%84%e5%b1%9e%e6%80%a7)
    - [3.11. alt属性](#311-alt%e5%b1%9e%e6%80%a7)
    - [3.12. map元素](#312-map%e5%85%83%e7%b4%a0)
    - [3.13. figure元素](#313-figure%e5%85%83%e7%b4%a0)
    - [3.14. figcaption元素](#314-figcaption%e5%85%83%e7%b4%a0)
    - [3.15. 多媒体元素video和audio](#315-%e5%a4%9a%e5%aa%92%e4%bd%93%e5%85%83%e7%b4%a0video%e5%92%8caudio)
    - [3.16. 列表元素](#316-%e5%88%97%e8%a1%a8%e5%85%83%e7%b4%a0)
    - [3.17. 容器元素](#317-%e5%ae%b9%e5%99%a8%e5%85%83%e7%b4%a0)
    - [3.18. 元素的包含关系](#318-%e5%85%83%e7%b4%a0%e7%9a%84%e5%8c%85%e5%90%ab%e5%85%b3%e7%b3%bb)
  - [3.19. CSS 基本概念](#319-css-%e5%9f%ba%e6%9c%ac%e6%a6%82%e5%bf%b5)
    - [常见样式声明](#%e5%b8%b8%e8%a7%81%e6%a0%b7%e5%bc%8f%e5%a3%b0%e6%98%8e)

<!-- /code_chunk_output -->


## 1. 简介

**浏览器组成**.

1. shell：外壳
2. core:内核(JS执行引擎、渲染引擎)

**拥有独立内核的浏览器**.

- IE浏览器：内核为Trident

- firfox:Gecko

- Chrome：Webkit->blink

- safari：Webkit

- Opera:Presto->blink

**版本**.

HTML5:2014

CSS3:目前还没有制定完成

## 2. 开发环境入门

推荐使用Chrome浏览器，要设置为默认浏览器

- sublime
- atom
- dreamweaver
- vscode

**vscode 插件**.

- Live Server ：右键运行HTML页面
- emmit 插件 ： vscode默认安装的插件

**emmit 插件**

- 按感叹号(!) ：完整的HTML文档结构

## 3. HTML基本语法

```html
<a href="https://blog.csdn.net/serryuer/article/details/89393760">渡一教育</a>
```

element（元素） = 起始标记（begin tag） + 元素属性 +元素内容 + 结束标记（end tag）
- 起始标记：可以表示元素名称或者元素类型
- 元素属性：非必要的，描述元素的额外信息
- 元素内容：要在页面上显示的东西
- 结束标记

元素属性：
- 局部属性：某些元素特有的属性
- 全局属性：例如title属性

### 3.1. 常见元素
- a : 超链接
- h1 : 一级标题
- lang ： 全局属性，language
- head ： 文档头，内部的内容不会显示到页面上。
- meta ： 表示文档的元数据，也就是附加信息。
- charset ： 指定网页编码


### 3.2. 空元素
没有结束标记的元素：叫做空元素
```html
<meta charset="UTF-8">
```

### 3.3. 元素嵌套
- 元素不能互相嵌套
- 父元素，子元素，祖先元素，后代元素，兄弟元素（拥有同一个父元素）

### 3.4. 文档声明
文档声明：告诉浏览器当前文档使用的HTML标准是HTML5

```html
<!DOCTYPE html> 
```

### 3.5. 根元素
一个页面最多只能有一个根元素，并且该元素是所有其它元素的父元素或祖先元素。在HTML5中可以不需要此元素
```html
<html lang="en">
</html>
```

### 3.6. href属性

**链接**
1. 普通连接
2. 锚链接：#号开始
3. 功能连接：点击后触发某个功能 执行js代码：**JavaScript**  发送邮件：**mailto**

### 3.7. target属性

表示跳转页面窗口位置，默认情况下新打开链接的位置在当前页面，也就是会覆盖当前页面。

target的取值：
- _self：在当前页面中打开（默认值）
- _blank : 在新窗口中打开页面

### 3.8. 路径

**绝对路径**
一般站外资源用绝对路径

格式：
> 协议名://主机名:端口号/路径
> schema://host:port/path

- 协议名：http,https,file
- 主机名：域名，IP地址
- 端口号：如果协议是http协议，默认端口号是80，如果协议是https协议，默认端口号是443
- 路径：资源(如网页、图片，视频，音频)的路径

**相对路径**

一般站内资源用相对路径
- ./  : 表示当前资源所在的目录，一般可以省略
- ../  : 表示上一层目录

### 3.9. img元素

img是image缩写，空元素

### 3.10. src(路径)属性

src是source缩写

### 3.11. alt属性

当图片资源失效时，将使用该属性的文字替代图片

### 3.12. map元素

在图片中的某个区域添加动作

```html
    <map name="solarMap">
        <area shape="circle(圆形)" coords="399(圆心x坐标),223(圆心y坐标),48(半径)" href="连接" alt="图片失效时显示的名字" target="_blank">
        <area shape="rect(长方形)" coords="334,221(左上角坐标)  ,110,220(右下角) " href="" alt="">
        <area shape="poly(正多边形)" coords="需要输入每个角的坐标" href="" alt="">
    </map>
```
- shape : 形状：圆形，正方形等
- coords ： 坐标、大小
- href ：链接

### 3.13. figure元素

通常用于把图片，图片标题，描述等包裹起来

### 3.14. figcaption元素
图片标题

### 3.15. 多媒体元素video和audio

```html
<video controls="controls" autoplay muted loop src="视频地址(通常是AVI、mp4)" style="width:500px;">
    </video>
    <!-- 
        controls：控制播放控件的显示，取值只能为controls 
        某些属性只有两种属性：1.不写 2.取值为属性名这种属性叫做布尔属性
        布尔属性在HTML中可以不写属性值
        autoplay：表示自动播放，布尔属性
        muted：静音播放，布尔属性
        loop：循环播放，布尔属性
    -->

```
audio与video的格式是完全一样的

**问题**
1. 旧版本的浏览器不支持这两个元素
2. 不同的浏览器支持的音视频格式可能不一样
3. 视频格式一般支持mp4和webm

### 3.16. 列表元素

> ol : older list 有序列表
> li : list item ：列表项
> ul : unordered list 无需列表

---
有序列表
```html
   <ol type="1" reversed>
       <li>打开冰箱门</li>
       <li>把大象装进去</li>
       <li>把冰箱门关上</li>
   </ol>
   <!-- 
       属性type
       type = 1  表示前面的列表用数字表示
            = i  表示前面的列表用罗马数字表示
            = a  用a，b，c……字母    
            = A  用A，B，C……字母
        注意：尽量不要使用type属性，尽量用css控制显示

        属性reversed
            表示倒序排列
    -->
```

---
无序列表
```html
   <ul>
        <li>责任心</li>
        <li>孝敬父母</li>
        <li>会做家务</li>
   </ul>
   <!-- 
       无需列表常用于制作菜单或者新闻列表
    -->

```

---
定义列表：
```html
    <dl>
        <dt>
            HTML 
        </dt>
        <dd>
            超文本比较语言
        </dd>

        <dt>元素</dt>
        <dd>
            组成html文档的单元
        </dd>
    </dl>
    <!-- 
        通常用于术语定义（用的不多）
        dl：definition list
        dt：definition title
        dd：definition description
     -->
```

### 3.17. 容器元素

传统容器元素：

div 是容器元素，用于定义网页区域，div不带任何样式

div缺点：浏览器无法识别语义

HTML5的容器元素(语义化的容器元素)：

- header ： 通常用于表示页头，也可以表示文章头部
- footer : 通常用于表示页脚，也可以用于表示文章的尾部
- article ： 通常用于表示文章正文
- section ： 通常用于表示文章的章节
- aside ：通常用于表示侧边栏，或者用于表示一些附加信息
- nav : 导航

### 3.18. 元素的包含关系

以前：块级元素独占一行，行级元素不换行。块级元素可以包含行级元素，行级元素不可以包含块级元素，a元素除外

现在：元素的包含关系由元素的内容类别决定。

总结：

- 容器元素中可以包含任何元素
- a元素中可以几乎包含任意元素
- 某些元素有固定子元素
- 标题元素和段落元素不能相互嵌套，并且不能包含容器元素


## 3.19. CSS 基本概念

```css {.line-numbers}
h1{
    color: red;
    background-color: burlywood;
    text-align: center;
}
```
整个代码叫做一条CSS规则

**CSS规则包括：选择器 + 声明块**

选择器：用于确定样式范围，包括以下几种
1. 元素选择器：直接输入元素名称（选择范围太宽）
1. ID选择器：选中对应ID值的元素。#ID（选择范围太窄）
1. 类选择器： .classname (最常用)

**声明块：出现在大括号中**
声明块中包含很多声明，每个声明包含一个样式规则

**CSS代码书写位置**
1. 内部样式表：放在header的style里面
1. 内联样式表：放在HTML元素里面，用style属性表示
1. 外部样式表（推荐）：将样式书写在独立的css文件中，在header中用link ref="stylesheet"包含CSS问阿金路径

外部样式表优点：
- 外部样式表可以解决多页面样式重复的问题
- 有利于浏览器缓存，从而提高页面响应速度
- 有利于代码分离，更容易阅读和维护

### 常见样式声明

**color**

元素内部的颜色

RGB表示法
```css {.line-numbers}
color:rgb(0,255,0);
```

HEX表示法

```css {.line-numbers}
color:#008c90;
```

**background-color**

背景颜色

**font-size**

元素内部文字的尺寸和大小

- px：像素

- em：相对单位，相对于父元素的字体大小











