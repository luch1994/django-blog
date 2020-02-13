from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, EmptyPage

from .models import Articles, Categories

# Create your views here.

# 列表页通用
def index(request):
    # 获取参数
    p = int(request.GET.get('p', '1'))
    psize = int(request.GET.get('psize', '12'))
    c = int(request.GET.get('c', '0'))
    # 获取所有文章
    articles = Articles.objects.all().filter(is_show = True).order_by('-updated_at')
    if c != 0:
        articles = articles.filter(category = c)
    paginator = Paginator(articles, psize)
    # 计算分页范围
    if paginator.num_pages > 1:
        if p - 5 < 1:
            page_range = range(1, min(6, paginator.num_pages + 1))
        elif p + 5 > paginator.num_pages:
            page_range = range(max(1, paginator.num_pages - 5), paginator.num_pages + 1)
        else:
            page_range = range(p - 2, p + 3)
    else:
        page_range = paginator.page_range

    # 当前页码的数据
    try:
        current_page = paginator.page(p)
    except EmptyPage as e:
        current_page = paginator.page(1)
    # 类别列表
    categories = Categories.objects.all()
    # 其他推送
    new_list, hot_list, recommend_list = get_side_list()
    # 标题，前端seo关键字和描述
    title = '剧丸儿资源分享 最专业的资源收集分享平台'
    seoKeyword = '剧丸儿 资源 分享'
    seoDescription = '剧丸儿资源分享网-专注于资源分享'
    return render(request, 'index.html', locals())

# 详情页通用
def detail(request, article_id):
    # 获取当前文章详情
    article = get_object_or_404(Articles, pk = article_id)
    # 增加访问次数
    article.viewed()
    # 类别列表
    categories = Categories.objects.all()
    # 其他推送
    new_list, hot_list, recommend_list = get_side_list()
    # 标题，前端seo关键字和描述
    title = article.title
    seoKeyword = title
    seoDescription = article.desc
    return render(request, 'detail.html', locals())

# 获取推荐，热门，最新
def get_side_list():
    articles = Articles.objects.all().filter(is_show = True)
    # 最新
    new_list = articles.order_by('-updated_at')
    # 热门
    hot_list = new_list.order_by('-view_times')
    # 推荐
    recommend_list = new_list.filter(is_recommend=True)
    return new_list[:5],hot_list[:5],recommend_list[:8]

