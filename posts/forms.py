from django.forms import ModelForm
from django.utils.translation import gettext_lazy as gtl

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']
        labels = {
            'text': gtl('Текст Вашего поста'),
        }
        help_texts = {
            'text': gtl('Здесь Вы можете рассказать, что у Вас нового.'),
            'group': gtl('Выберите группу, которая лучше всего '
                         'подходит к теме Вашего поста.')
        }

    def check_request(request):
        if request.POST or None:
            return PostForm(request.POST)
        return PostForm()
