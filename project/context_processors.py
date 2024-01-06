def get_group_list(request):
    return {
        'group_list': [i.name for i in request.user.groups.all()]
    }