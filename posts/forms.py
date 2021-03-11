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
        error_messages = {
            'text': {
                'required': gtl('Посты без текста мало кому интересны, '
                                'пожалуйста, поделитесь своей историей!'),
            },
        }
