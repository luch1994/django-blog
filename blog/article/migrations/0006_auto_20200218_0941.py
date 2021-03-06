# Generated by Django 3.0.2 on 2020-02-18 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20200212_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='tags',
            field=models.ManyToManyField(related_name='article_tag', to='article.Tags'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True, verbose_name='评论人姓名')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Articles', verbose_name='评论的文章')),
            ],
        ),
    ]
