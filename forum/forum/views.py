from django.shortcuts import render
from django.shortcuts import render
from userforum.models import Forum,SowingMap,ForumType,ForumRead
# Create your views here.


def index(request):
    read_number_list = []
    all_forum = Forum.objects.all()[:10]
    all_sowing_map = SowingMap.objects.all()
    all_forum_type = ForumType.objects.all()



    return render(request, 'index.html', {
        'all_forum': all_forum,
        'all_sowing_map':all_sowing_map,
        'all_forum_type':all_forum_type,
    })