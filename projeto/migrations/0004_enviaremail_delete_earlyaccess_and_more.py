# Generated by Django 4.1.2 on 2022-10-18 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0003_earlyaccess_remove_stayintheknow_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnviarEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='EarlyAccess',
        ),
        migrations.AddField(
            model_name='stayintheknow',
            name='text_button',
            field=models.CharField(default='', max_length=100, verbose_name='Texto-Botão de enviar e-mail'),
        ),
    ]
