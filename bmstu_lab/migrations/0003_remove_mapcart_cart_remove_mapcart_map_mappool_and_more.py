# Generated by Django 5.1.1 on 2024-09-29 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu_lab', '0002_remove_mapcart_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapcart',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='mapcart',
            name='map',
        ),
        migrations.CreateModel(
            name='MapPool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('deleted', 'Удалён'), ('submitted', 'Сформирован'), ('completed', 'Завершён'), ('rejected', 'Отклонён')], default='draft', max_length=20)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('submit_date', models.DateTimeField(blank=True, null=True)),
                ('complete_date', models.DateTimeField(blank=True, null=True)),
                ('moderator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moderated_map_pools', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_pools', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MapMapPool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmstu_lab.map')),
                ('map_pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmstu_lab.mappool')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='MapCart',
        ),
        migrations.AddConstraint(
            model_name='mapmappool',
            constraint=models.UniqueConstraint(fields=('map_pool', 'map'), name='unique_map_pool_map'),
        ),
    ]
