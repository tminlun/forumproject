import os
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



#增加用户模型字段
class UserProfile(AbstractUser):
    nice_name = models.CharField(max_length=20,verbose_name="昵称")
    image = models.ImageField(upload_to="user/%Y%m",default=os.path.join("avatar", "default.png"),verbose_name="头像")
    gender = models.CharField(choices=(("nan", "男"), ("nv", "女")), max_length=10, default="nan", verbose_name="性别")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username