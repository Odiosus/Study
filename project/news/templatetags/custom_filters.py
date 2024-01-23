from django import template

register = template.Library()

censor_list = ['смерть', 'убить', 'оружие', ]

# Слово "смерти" встречается в заголовке поста про шимпанзе
# Слово "убить" встречается в тексте этого же поста
# Слово "оружия" встречается в посте про вселенную

@register.filter()
def censor(text):
    text_list = text.split()
    for i, j in enumerate(text.split()):
        for k in censor_list:
            if j.find(k[:-1]) != -1:
                text_list[i] = len(text_list[i]) * '*'
    return ' '.join(text_list)


@register.filter()
def get_subscribers(category):
    sub_list = category.subscriptions.values_list('user_id', flat=True)
    return sub_list
