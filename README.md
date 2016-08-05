# django-project-layout
关于django工程布局以及模板的使用.

![](https://travis-ci.org/510908220/django-project-layout.svg)
## 简介
平时在使用django时，由于所有配置都是在```settings.py```里.由于本地环境根测试环境配置的差异:
- 要么本地和开发环境配置文件各自改各自的，不提交
- 如果要提交，提交完后再修改回本地

## 改进
> 将配置单独挡在一个包内,目录结构如下:  

```
config
	settings
		__init__.py
		base.py
		local.py
		production.py
	__init__.py
	urls.py
	wsgi.py
```
这样的好处是本地环境和线上环境可以隔离开.

## 使用
> 为了方便创建环境隔离开的django工程，这里将上面打包成一个模板。
- 默认本地环境使用```django-debug-toolbar```
- django后台管理使用了```django-jet```




1.  根据模板创建工程
```
django-admin startproject --template=https://github.com/510908220/django-project-layout/archive/v1.0.tar.gz project_name
```

2.  安装包，执行```pip install -r requirements/local.txt```
