1. 执行命令创建项目
```sh
django-admin startproject blog 
```
2. 执行命令创建文章应用
```
python manage.py startapp article
```
3. 新建mysql数据库：django-blog
4. 修改blog下面的settings.py，搜索 DATABASES, 修改数据库连接配置，我使用的是mysql
5. 执行命令创建django自带的表，包括管理员等
```sh
python manage.py migrate
```
6. 修改article下面的models.py设计4个模型：分类；文章；标签；文章-标签关系
7. 将article应用添加到项目中
```py
# 修改blog/settings.py，添加第一项，其中ArticleConfig在/article/apps.py文件里
INSTALLED_APPS = [
    'article.apps.ArticleConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
8. 运行命令，激活模型
```sh
python manage.py makemigrations article
```
当看到下面的输出的时候，表示激活成功
```sh
Migrations for 'article':
  article\migrations\0001_initial.py
    - Create model Articles
    - Create model Categories
    - Create model Tags
    - Create model Tag_article
    - Add field category to articles
```
9. 运行命令，在数据库里创建模型对应的表
```sh
python manage.py migrate
```
10. 创建一个管理员账号，使用的信息：near；1233lch
```sh
python manage.py createsuperuser
```
11. 在article/admin.py文件里添加代码，在管理后台页面注册模型
```py
from .models import *
# Register your models here.

admin.site.register(Categories)
admin.site.register(Articles)
admin.site.register(Tags)
```
12. 启动服务器，并打开路由 /admin
```sh
python manage.py runserver
```
13. 在article文件夹，新建templates和static文件夹，新建base.html
14. 修改article/views.py 新增页面，添加articles/urls.py 添加路由，修改blog/urls.py新增路由
15. 安装富文本插件
```sh
pip install django-ckeditor
```
16. 完善页面，路由，模型和样式等功能
17. 新建服务器数据库django-blog，并添加用户，只给当前数据库相关的权限，并修改settings.py里的数据库连接信息
```mysql
CREATE DATABASE `django-blog` CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'djblog'@'%' IDENTIFIED BY 'django-blog-1233lch';
GRANT ALL on `django-blog`.* TO 'djblog'@'%';
```
18. 下载linux版本的anaconda并上传到服务器，执行安装anaconda的命令，安装完成后需要配置环境变量：
```sh
bash Anaconda3-2019.10-Linux-x86_64.sh
sudo vi /etc/profile
```
19. 修改环境变量为：export PATH=$PATH:/usr/local/anaconda3/bin
修改之后，需要执行下面命令，修改的配置才会生效
```sh
source /etc/profile
```
20. 测试python和pip命令都能正常使用之后，安装网站需要的依赖：
```sh
pip install django
pip install django-ckeditor
conda install mysqlclient
```
21. 需要执行数据库相关的操作
22. 在settings.py 添加代码：
```py
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
然后执行下面的命令，将admin的样式复制到当前项目的根目录，修改nginx配置，使得static定位到当前目录
```sh
python manage.py collectstatic
```
23. 安装uwsgi
```sh
pip install uwsgi
```
24. 在网站根目录添加uwsgi的配置文件blog.ini
25. 
使用uwsgi启动网站
```sh
uwsgi --ini blog.ini
```
其他停止和重启uwsgi的命令
```sh
uwsgi --stop blog.pid
uwsgi --reload blog.pid
```
查看当前状态
```sh
ps aux | grep uwsgi
```
26. 配置nginx，配置案例在nginx.conf里
