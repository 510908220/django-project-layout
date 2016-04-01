# django-project-layout
关于django工程布局以及模板的使用.

## 简介
平时在使用django时，由于所有配置都是在```settings.py```里.由于本地环境根测试环境配置的差异:
- 要么本地和开发环境配置文件各自改各自的，不提交
- 如果要提交，提交完后再修改回本地


## 使用

- 创建
```
django-admin startproject --template=https://github.com/510908220/django-project-layout/raw/master/django-project-template.zip project_name
```

- 切换到目录里，执行```pip install -r requirements/local.txt```

