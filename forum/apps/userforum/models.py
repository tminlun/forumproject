from django.db import models
from user.models import UserProfile
from django.db.models.fields import exceptions
# Create your models here.

#帖子类型
class ForumType(models.Model):
    type_name = models.CharField(max_length=20,verbose_name="帖子类型")
    add_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "帖子类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name


#帖子
class Forum(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="发帖作者")
    title = models.CharField(max_length=15,verbose_name="标题")
    comment = models.TextField(verbose_name="帖子内容")
    forum_type = models.ForeignKey(ForumType,on_delete=models.CASCADE,verbose_name="帖子类型")
    read_number = models.IntegerField(default=0, verbose_name="阅读数量")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="发帖时间")

    class Meta:
        verbose_name = "帖子"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


#轮播图
class SowingMap(models.Model):
    title = models.CharField(max_length=30, verbose_name="轮播图标题")
    images = models.ImageField(upload_to="sowin/%Y%m", default="sowingmap/default.jpg", verbose_name="轮播图(750X450)")
    index_images = models.IntegerField(default=0,verbose_name="轮播顺序")
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
        ordering = ["index_images"]

    def __str__(self):
        return self.title

#帖子阅读数量
class ForumRead(models.Model):
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE,verbose_name="帖子")
    read_number = models.IntegerField(default=0,verbose_name="阅读数量")



    class Meta:
        verbose_name = "帖子阅读数"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.forum,self.read_number)