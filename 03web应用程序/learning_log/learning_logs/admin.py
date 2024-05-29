from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic
from learning_logs.models import Entry

# 注册Topic模型
admin.site.register(Topic)
admin.site.register(Entry)
