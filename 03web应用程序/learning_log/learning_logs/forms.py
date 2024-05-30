from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    # 它告诉Django根据哪个模型创建表单
    class Meta:
        model = Topic
        # 表单只包含字段text
        fields = ['text']
        # 不要为字段text生成标签？
        labels = {'text': ''}


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
