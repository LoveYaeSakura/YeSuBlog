from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from mdeditor.fields import MDTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25, default='', verbose_name='文章分类', help_text='文章分类')
    desc = models.TextField(default='', verbose_name='类别描述', help_text='类别描述')

    class Meta:
        verbose_name_plural = verbose_name = '文章分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类', help_text='文章分类')
    name = models.CharField(max_length=20, verbose_name="文章标签")
    desc = models.TextField(max_length=50,verbose_name='标签描述')

    class Meta:
        verbose_name_plural = verbose_name = '文章标签'

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类', help_text='文章分类')
    top = models.CharField('是否置顶', default='no', choices=(('yes', '是'), ('no', '否')), max_length=5)
    title = models.CharField('标题', max_length=100,default='没有标题吖!')
    brief = models.TextField(max_length=500, verbose_name='简短描述', help_text='简短描述')
    content = MDTextField(help_text='正文', verbose_name='正文')
    created = models.DateField('创建时间', default=timezone.now)
    update = models.DateField('更新时间', auto_now=True)
    total_views = models.IntegerField('访问量', default=0)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = verbose_name = '文章'

    def __str__(self):
        return self.title



