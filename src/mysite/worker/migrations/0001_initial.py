# Generated by Django 3.0.3 on 2020-04-21 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('ad_type', models.CharField(blank=True, max_length=32, null=True, verbose_name='description')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('ad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.Ad')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('gender', models.CharField(blank=True, choices=[('w', 'Women'), ('m', 'Man'), ('o', 'Other')], max_length=1, null=True, verbose_name='Gender')),
                ('first_name', models.CharField(max_length=256, verbose_name='First name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Last name')),
                ('phone', models.CharField(blank=True, max_length=256, null=True, verbose_name='Phone')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
            ],
            options={
                'verbose_name': 'User',
                'db_table': 'user',
                'unique_together': {('email', 'phone')},
            },
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('ad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.Ad')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='message content')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('conversation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.Conversation')),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.User')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=256, null=True, verbose_name='address1')),
                ('address2', models.CharField(blank=True, max_length=256, null=True, verbose_name='address2')),
                ('zip_code', models.IntegerField(blank=True, max_length=5, null=True, verbose_name='zip_code')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='city')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='country')),
                ('latitude', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True, verbose_name='Latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True, verbose_name='Longitude')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.User')),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.Category'),
        ),
        migrations.AddField(
            model_name='ad',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.User'),
        ),
    ]