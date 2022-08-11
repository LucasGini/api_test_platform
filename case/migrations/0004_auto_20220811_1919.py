# Generated by Django 3.2.15 on 2022-08-11 11:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_auto_20220811_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulelist',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='modulelist',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='projectlist',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='projectlist',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
    ]