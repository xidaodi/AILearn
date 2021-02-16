# Python中的第三方库的管理和虚拟环境



## 第三方库的管理

> python中比较牛逼的地方就是由大量的第三方库提供给你使用。

#### 第三方库的管理网站 https://pypi.org/

#### 如何安装第三方库

####  pip

> pip就是python的包管理工具，解决了包直接的依赖关系。可以方便的管理第三方库(包).
>
> 类似于PHP中Composer，或者Nodejs中的npm，或者Linux中的yum。

### 如何使用pip

`pip install 包名（库名）`

注意：如果有多个python环境的情况下，可能需要使用pip3

例如安装pymysql这个库

`pip install pymysql`

### 安装指定版本的包

`pip install 包名==版本`

### 搜索已经安装的包

`pip show 包名`

### 查看安装的所有包

`pip list` 

### 更换pip的镜像源

```
PIP 更换国内安装源

pip国内的一些镜像
  阿里云 http://mirrors.aliyun.com/pypi/simple/ 
  中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
  豆瓣(douban) http://pypi.douban.com/simple/ 
  清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
  中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

修改源方法：

临时使用： 
可以在使用pip的时候在后面加上-i参数，指定pip源 
pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple

永久修改： 
linux: 
修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：

[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn


windows: 
直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，在pip 目录下新建文件pip.ini，内容如下

或者按照网友的建议：win+R 打开用户目录%HOMEPATH%，在此目录下创建 pip 文件夹，在 pip 目录下创建 pip.ini 文件, 内容如下

 
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn

```

## 虚拟环境

> 虚拟环境就是在当前的系统环境中，去配置另外一个python的运行环境，是可以创建多个不同的虚拟环境。
>
> python的虚拟环境相互独立，互不影响。

+ 虚拟环境中可以在没有权限的情况下安装新的库（Linux系统中可能会出现的问题）
+ 不同的应用可以使用不同的库或不同的版本。
+ 虚拟环境中的库升级也不影响其它环境
+ 虚拟环境可以作为一个项目的专有环境。在需要部署时，一键导出项目的所需要的包

### 如何去使用python的虚拟环境

1。在pycharm中可以直接创建虚拟环境

#### 2。自己安装独立的虚拟环境

1. #### 创建虚拟环境

`python -m venv 虚拟环境名`

2. #### 进入虚拟环境，激活虚拟环境

   + linux

   ```shell
   # 使用 source 命令 去执行 v1/bin/ 目录下的 activate
   localhost:code yc$ source v1/bin/activate
   (v1) localhost:code yc$ 
   ```

   + windows

   ```shell
   # windows系统需要 进入 v1/Scripts/ 这个目录
   cd v1/Scripts/ 
   # 运行 activate.bat 文件
   activate.bat
   (v1) F:\code>
   ```

3. #### 接下来就可以在虚拟环境中安装一些包

`pip install pymysql`

4. #### 查看是否安装了某个包

`pip show pymysql` 如果安装过则能显示信息。

5. #### 退出虚拟环境

   + linux :  deactivate
   + Windows： 直接ctrl+c

6. #### 导出当前环境中所有安装过的包

```shell
# 查看所有安装的包
pip list
'''
Package      Version
------------ -------
Click        7.0    
Flask        1.1.1  
itsdangerous 1.1.0  
Jinja2       2.10.3 
MarkupSafe   1.1.1  
pip          19.0.3 
PyMySQL      0.9.3  
setuptools   40.8.0 
Werkzeug     0.16.0 
'''

# 导出所有包到文件
pip freeze > ./requirements.txt
```

7. #### 删除环境

退出虚拟环境后，直接删除虚拟环境文件夹即可



