from django.db import models


# Create your models here.

# Product에는 id, title, image, likes 4개 갖고있음.( id는 자동으로 생성?)
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass  # id 값은 자동으로 생성되는 값인가 봄. 그래서 다른건 일단 필요 없으니까 pass
