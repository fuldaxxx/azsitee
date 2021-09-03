
from django.db import models
from django.conf import settings
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel



class AbstractComment(models.Model):
    """Абстрактная модель комментариев"""
    text = models.TextField("Сообщение", max_length=2000)
    created_date = models.DateTimeField("Дата добавления", auto_now_add=True)
    update_date = models.DateTimeField("Изменен", auto_now=True)
    published = models.BooleanField("Опубликовать?", default=True)
    deleted = models.BooleanField("Удален?", default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:

        abstract = True



class Post(models.Model):
    text = models.TextField(max_length=10000)
    create_date = models.DateTimeField(auto_created=True)
    published = models.BooleanField(default=True)
    modearation = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post by {self.user}'


    def comments_count(self):
        return self.comments.count()



class Comment(AbstractComment, MPTTModel):
    """Модель коментариев к новостям"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, verbose_name="Новость", related_name="comments", on_delete=models.CASCADE
    )
    parent = TreeForeignKey(
        "self",
        verbose_name="Родительский комментарий",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{} - {}".format(self.user, self.post)