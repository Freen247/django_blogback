import xadmin
from .models import Article,  Category, Carousel, Keyword, FriendLink


class ArticleAdmin(object):
    # 这个的作用是给出一个筛选机制，一般按照时间比较好
    date_hierarchy = 'create_date'

    exclude = ('views',)

    # 在查看修改的时候显示的属性，第一个字段带有<a>标签，所以最好放标题
    list_display = ('id', 'title', 'author', 'create_date', 'update_date')

    # 设置需要添加<a>标签的字段
    list_display_links = ('title',)

    # 激活过滤器，这个很有用
    list_filter = ('create_date', 'category')

    list_per_page = 50  # 控制每页显示的对象数量，默认是100

    # filter_horizontal = ('tags', 'keywords')  # 给多选增加一个左右添加的框

    # 限制用户权限，只能看到自己编辑的文章
    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

xadmin.site.register(Article, ArticleAdmin)
# class TagAdmin(object):
#     list_display = ('name', 'id', 'slug')


class CategoryAdmin(object):
    list_display = ('name', 'id', 'slug')

xadmin.site.register(Category, CategoryAdmin)
# 自定义管理站点的名称和URL标题
xadmin.site.site_header = '网站管理'
xadmin.site.site_title = '博客后台管理'


# class TimelineAdmin(object):
#     list_display = ('title', 'side', 'update_date', 'icon', 'icon_color',)
#     fieldsets = (
#         ('图标信息', {'fields': (('icon', 'icon_color'),)}),
#         ('时间位置', {'fields': (('side', 'update_date', 'star_num'),)}),
#         ('主要内容', {'fields': ('title', 'content')}),
#     )
#     date_hierarchy = 'update_date'
#     list_filter = ('star_num', 'update_date')


class CarouselAdmin(object):
    list_display = ('number', 'title', 'img', 'url')

xadmin.site.register(Carousel, CarouselAdmin)
# class SilianAdmin(object):
#     list_display = ('id', 'remark', 'badurl', 'add_date')


class KeywordAdmin(object):
    list_display = ('name', 'id')

xadmin.site.register(Keyword, KeywordAdmin)

class FriendLinkAdmin(object):
    list_display = ('name', 'description', 'link', 'create_date', 'is_active', 'is_show')
    date_hierarchy = 'create_date'
    list_filter = ('is_active', 'is_show')
xadmin.site.register(FriendLink, FriendLinkAdmin)