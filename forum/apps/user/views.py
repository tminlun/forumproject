import uuid
import os
import json

from django.shortcuts import render,redirect,reverse
from django.views import View
from django.http import JsonResponse

from PIL import Image
# Create your views here.

#处理头像
def crop_image(current_avatar, file, data, uid):
    """

    :param current_avatar: 旧头像的路径
    :param file: 用户上传头像文件
    :param data: 裁剪图片的数据
    :param uid: 用户id
    :return:
    """
    # 随机生成新的图片名，自定义路径。
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    cropped_avatar = os.path.join(str(uid), "avatar", file_name)

    #相对根目录路径
    file_path = os.path.join("media", str(uid), "avatar", file_name)

# 获取Ajax发送的裁剪参数data，先用json解析。
    coords = json.loads(data)
    t_x = int(coords['x'])
    t_y = int(coords['y'])
    t_width = t_x + int(coords['width'])
    t_height = t_y + int(coords['height'])
    t_rotate = coords['rotate']

    # 裁剪图片,压缩尺寸为300*300。
    img = Image.open(file)
    crop_im = img.crop((t_x, t_y, t_width, t_height)).resize((300, 300), Image.ANTIALIAS).rotate(t_rotate)
    #新建文件夹
    directory = os.path.dirname(file_path)

    #保存图片
    if os.path.exists(directory): #判断是否存在此文件夹，存在返回Ture，不存在返回False
        crop_im.save(file_path)
    else:
        os.makedirs(directory)
        crop_im.save(file_path)

    ##删除旧的图片
    #判断是否使用默认头像，否则进行删除操作
    if not current_avatar == os.path.join("avatar", "default.png"):
        current_avatar_path = os.path.join("media", str(uid), "avatar", os.path.basename(current_avatar.url))
        os.remove(current_avatar_path)

    return cropped_avatar

#展示用户头像
class UserAvatarView(View):
    def get(self,request):
        #判断是否登录
        if not request.user.is_authenticated:
            return redirect(reverse("login_or_registered"))

        return render(request,'user_avatar.html',{

        })

#上传用户头像
class AvatarAjaxView(View):
    def post(self,request):
        user = request.user
        #判断用户是否登录
        if not user.is_authenticated:
            return JsonResponse({"code":"401"})

        #获取上传图片
        img = request.FILES['avatar_file']
        #获取裁剪数据
        data = request.POST['avatar_data']

        #判断图像是否大于900 X 1200
        # if img.size/1024 > 700:
        #     return JsonResponse({"msg": "图片尺寸应小于900 X 1200 像素, 请重新上传.", "code":"500"})

        #获取头像地址
        current_avatar = user.image
        cropped_avatar = crop_image(current_avatar, img, data, user.id)
        user.image = cropped_avatar
        user.save()
        data = {"result": user.image.url,"code":"200"}
        return JsonResponse(data)
