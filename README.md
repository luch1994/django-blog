# django-blog
使用django3.0.2开发的个人博客，现在由我个人用于开发和维护一个资源分享网站

线上地址预览<a href="http://www.juwaner.net">剧丸儿资源分享</a>

前端使用mdui，一个比较轻量级的ui框架，可换肤

首次使用：
1. 安装依赖：
```sh
pip install django=3.0.2
pip install django-ckeditor=5.9.0
```

2. 激活模型
```sh
python manage.py makemigrations article
```

3. 初始化数据库
```sh
python manage.py migrate
```

4. 创建管理员账号
```sh
python manage.py createsuperuser
```

5. 启动服务
```sh
python manage.py runserver
```
或者
```sh
python manage.py 0.0.0.0:8000
```

6. 部署在服务器上，需要先在服务器上安装依赖uwsgi，在windows上安装失败，需要在linux上安装
```sh
pip install uwsgi
```
启动命令
```
uwsgi --ini blog.ini
```
停止命令
```sh
uwsgi --stop blog.pid
```
重启命令
```sh
uwsgi --reload blog.pid
```
