# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\11\21 0021 19:13$'
import xadmin
from xadmin import views





class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# xadmin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "Pig管理"
    site_footer = "Pig"
    #收起菜单
    menu_style = "accordion"





# 将开启主题功能注册
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView,GlobalSettings)