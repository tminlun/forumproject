from django.shortcuts import render,get_object_or_404,HttpResponse
from django.views import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Forum,ForumType,ForumRead


# Create your views here.

#帖子列表
class ForumView(View):
    def get(self,request):
        all_forum = Forum.objects.all()
        forum_count  = all_forum.count()
        forum_type = ForumType.objects.all()

        #分页插件
        try:
            #获取前端页数
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        #进行分页处理
        p = Paginator(all_forum,7,request=request)

        #取出分页页数数据
        forum = p.page(page)

        return render(request,'list.html',{
            "all_forum":forum,
            "all_forum_type":forum_type,
            "forum_count":forum_count,
        })


#详情页面
class ForumDatileView(View):
    def get(self, request,forum_id):
        #获取所有帖子类型数据
        forum_type = ForumType.objects.all()
        #获取详情页面帖子
        forum = get_object_or_404(Forum,id=forum_id)
        #获取从哪里点进来的页面
        from_html = request.GET.get('from','')

        #获取阅读数量
        try:
            forum_read = ForumRead.objects.get(forum=forum)
            form_read_number = forum_read.read_number
        except:
            form_read_number = 0

        response = render(request, 'info.html', {
            "forum":forum,
            "all_forum_type":forum_type,
            "from_html":from_html,
            "form_read_number":form_read_number,
        })
        #返回key
        key = 'forum_%s_read' % (forum_id)
        # 读取cookie
        cookie = request.COOKIES.get(key,'')
        #如果cookie不存在,增加阅读数
        if cookie == "":
            #是否存在此帖子数据
            read_forum, created = ForumRead.objects.get_or_create(forum=forum)
            #若不存在数据
            if created:
                read_forum =ForumRead.objects.get(forum=forum)

            #增加阅读数
            read_forum.read_number += 1
            read_forum.save()

            #增加帖子数据阅读数
            forum.read_number += 1
            forum.save()
            # 设置cookie为true
            response.set_cookie(key, 'true')
        return response


#帖子类型
class ForumTypeView(View):
    def get(self,request,type_id):
        #获取帖子类型对象
        type_name = get_object_or_404(ForumType,id=type_id)
        #过滤此类型对象的帖子
        all_forum_type = Forum.objects.filter(forum_type=type_name)
        #类型帖子的总数
        form_count = all_forum_type.count()
        #获取所有帖子类型对象
        all_type = ForumType.objects.all()

        #分页插件
        try:
            #获取前端页数
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        #进行分页处理
        p = Paginator(all_forum_type,7,request=request)

        #取出分页页数数据
        forum = p.page(page)


        return render(request,'type_list.html',{
            'all_forum':forum,
            'all_forum_type':all_type,
            'forum_count':form_count,
            'type_name':type_name,
        })
