from django.contrib import admin
from .models import *
# Register your models here.

class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 1

# 自定义文章管理列表
class ArticlesAdmin(admin.ModelAdmin):
    # 自定义列表显示，默认只显示一列，存在多对多关系的列不能指定显示和编辑
    list_display = ('title', 'category', 'is_recommend', 'is_show', 'view_times', 'updated_at')
    # 显示界面可编辑的列
    # list_editable = ('title')
    # 每页显示行数
    list_per_page = 30
    # 可排序列，默认升序，前面加-则为降序
    ordering = ('updated_at', 'view_times')
    # 显示搜索框，在搜索框内科通过指定字段进行搜索
    search_fields = ('title', 'category__name')
    # 过滤选项
    list_filter = ('is_recommend', 'is_show')
    # 文章的评论
    inlines = [CommentsInline]
    #添加时非必要信息折叠不显示
    # fieldsets = [(None, {'fields': ['sname','cls']}),('other information', {'fields': ['gender', 'age'], 'classes': ['collapse']})]  
    # 仅限多对多列使用，对存在多对多的列可搜索
    # filter_horizontal = ('cls',)
    # 同上
    # filter_vertical = ('cls',)


admin.site.register(Categories)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Tags)
# admin.site.register(Comments)
