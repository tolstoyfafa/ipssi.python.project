from django.db import models

# Create your models here.


class User(models.Model):
    """User model contains user infos"""
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )
    gender = models.CharField(
        max_length=1,
        choices=(
            ('w', 'Women'),
            ('m', 'Man'),
            ('o', 'Other'),
        ),
        blank=True,
        null=True,
        verbose_name='Gender'
    )
    first_name = models.CharField(
        max_length=256,
        verbose_name='First name'
    )
    last_name = models.CharField(
        max_length=256,
        verbose_name='Last name'
    )
    phone = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Phone'
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Birth date'
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Update date'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Created date'
    )

    class Meta:
        verbose_name = 'User'
        db_table = 'user'
        unique_together = ['email', 'phone']


class Address(models.Model):
    """Address model contains address of user"""
    address1 = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='address1'
    )
    address2 = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='address2'
    )

    zip_code = models.IntegerField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name='zip_code')

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='city')

    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='country')

    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name=('Latitude'))

    longitude = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name=('Longitude'))

    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Update date'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Created date'
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE)


class Category(models.Model):
    """Category model contains address of user"""
    name = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name='name'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='description')


class Ad(models.Model):
    """Ad model contains address of user"""
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='title'
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='description'
    )
    ad_type = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name='description'
    )

    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Update date'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Created date'
    )

    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE)

    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE)


class Conversation(models.Model):
    """Conversation model infos about conversation beetween users"""
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Update date'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Created date'
    )

    ad_id = models.ForeignKey(
        Ad, on_delete=models.CASCADE)


class Message(models.Model):
    """Message model"""
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Update date'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Created date'
    )

    content = models.TextField(
        blank=True,
        null=True,
        verbose_name='message content'
    )

    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Update date'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Created date'
    )

    sender_id = models.ForeignKey(
        User, on_delete=models.CASCADE)

    conversation_id = models.ForeignKey(
        Conversation, on_delete=models.CASCADE)


class Mission(models.Model):

    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Update date'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Created date'
    )

    ad_id = models.ForeignKey(
        Ad, on_delete=models.CASCADE)

    customer_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
