from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import striptags
import django.utils.timezone as timezone

# Create your models here.

# 分类
class Categories(models.Model):
    name = models.CharField('类别名称', max_length=50)
    sort = models.IntegerField('排序')

    def __str__(self):
        return self.name

# 标签
class Tags(models.Model):
    name = models.CharField('标签名', max_length=40)

    def __str__(self):
        return self.name


# 文章
class Articles(models.Model):
    title = models.CharField('文章标题', max_length=100, default='')
    head_img = models.CharField('主图', max_length=125, default='')
    category = models.ForeignKey(
        Categories, null=True, on_delete=models.SET_NULL)
    body = RichTextField('主体', default='')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    is_show = models.BooleanField('是否显示', default=True)
    view_times = models.IntegerField('查看次数', default=0)
    is_recommend = models.BooleanField('是否推荐', default=False)
    tags = models.ManyToManyField(Tags, related_name='article_tag')

    def __str__(self):
        return self.title

    def desc(self):
        return striptags(self.body)

    # 访问次数+1
    def viewed(self):
        self.view_times += 1
        self.save(update_fields=['view_times'])


# 评论
class Comments(models.Model):
    name = models.CharField('昵称', max_length=50, default='', null=True)
    content = models.TextField('内容')
    created_at = models.DateTimeField('评论时间', auto_now_add=True)
    email = models.CharField('邮箱地址', max_length=100, null=True, default='', blank=True)
    is_show = models.BooleanField('是否显示出来', default=True)
    article = models.ForeignKey(Articles, verbose_name="评论的文章", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content[:5] + '...'
