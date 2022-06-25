# Generated by Django 4.0.5 on 2022-06-25 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='ad_images/', verbose_name='Фото объявления')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('publicated_at', models.DateTimeField(verbose_name='Дата публикации')),
                ('status', models.CharField(choices=[('on_moderation', 'На модерации'), ('published', 'Опубликовано'), ('rejected', 'Отклонено')], default='on_moderation', max_length=15, verbose_name='Статус')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'db_table': 'advertisements',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание'),
        ),
        migrations.DeleteModel(
            name='Ad',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ads', to='webapp.category', verbose_name='Категория'),
        ),
    ]
