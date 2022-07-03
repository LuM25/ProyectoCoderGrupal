# Generated by Django 4.0.5 on 2022-06-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receta_1a3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('ingrediente_1', models.CharField(default='', max_length=30)),
                ('cantidad_1', models.FloatField(blank=True, null=True)),
                ('ingrediente_2', models.CharField(max_length=30)),
                ('cantidad_2', models.FloatField(blank=True, null=True)),
                ('ingrediente_3', models.CharField(max_length=30)),
                ('cantidad_3', models.FloatField(blank=True, null=True)),
                ('procedimiento', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='receta_4a6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('ingrediente_1', models.CharField(max_length=30)),
                ('cantidad_1', models.FloatField(blank=True, null=True)),
                ('ingrediente_2', models.CharField(max_length=30)),
                ('cantidad_2', models.FloatField(blank=True, null=True)),
                ('ingrediente_3', models.CharField(max_length=30)),
                ('cantidad_3', models.FloatField(blank=True, null=True)),
                ('ingrediente_4', models.CharField(max_length=30)),
                ('cantidad_4', models.FloatField(blank=True, null=True)),
                ('ingrediente_5', models.CharField(max_length=30)),
                ('cantidad_5', models.FloatField(blank=True, null=True)),
                ('ingrediente_6', models.CharField(max_length=30)),
                ('cantidad_6', models.FloatField(blank=True, null=True)),
                ('procedimiento', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='receta_7a10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('ingrediente_1', models.CharField(max_length=30)),
                ('cantidad_1', models.FloatField(blank=True, null=True)),
                ('ingrediente_2', models.CharField(max_length=30)),
                ('cantidad_2', models.FloatField(blank=True, null=True)),
                ('ingrediente_3', models.CharField(max_length=30)),
                ('cantidad_3', models.FloatField(blank=True, null=True)),
                ('ingrediente_4', models.CharField(max_length=30)),
                ('cantidad_4', models.FloatField(blank=True, null=True)),
                ('ingrediente_5', models.CharField(max_length=30)),
                ('cantidad_5', models.FloatField(blank=True, null=True)),
                ('ingrediente_6', models.CharField(max_length=30)),
                ('cantidad_6', models.FloatField(blank=True, null=True)),
                ('ingrediente_7', models.CharField(max_length=30)),
                ('cantidad_7', models.FloatField(blank=True, null=True)),
                ('ingrediente_8', models.CharField(max_length=30)),
                ('cantidad_8', models.FloatField(blank=True, null=True)),
                ('ingrediente_9', models.CharField(max_length=30)),
                ('cantidad_9', models.FloatField(blank=True, null=True)),
                ('ingrediente_10', models.CharField(max_length=30)),
                ('cantidad_10', models.FloatField(blank=True, null=True)),
                ('procedimiento', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
