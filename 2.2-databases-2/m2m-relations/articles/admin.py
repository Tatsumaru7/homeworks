from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            cleaned_data = form.cleaned_data
            # Добавьте ваши правила валидации сюда.
            # Например, если вы хотите проверить, что определенное поле
            # обязательно для заполнения:
            if not cleaned_data.get('name'):
                raise ValidationError('Поле name обязательно для заполнения.')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin): 
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline,]

@admin.register(Tag)
class ScopeAdmin(admin.ModelAdmin): 
    list_display = ['name']
    