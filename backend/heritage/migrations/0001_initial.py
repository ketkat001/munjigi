# Generated by Django 2.2.7 on 2020-09-10 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Heritage',
            fields=[
                ('selnum', models.IntegerField(primary_key=True, serialize=False)),
                ('k_name', models.CharField(max_length=50)),
                ('h_name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('imageURL', models.URLField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('era', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=150)),
                ('clsfc_code', models.IntegerField()),
                ('clsfc_name', models.CharField(max_length=50)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_heritages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('heritage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heritage.Heritage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_recommend', models.ManyToManyField(blank=True, related_name='recommend_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
