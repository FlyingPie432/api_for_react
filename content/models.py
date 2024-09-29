from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    CONSULTATION_CHOICES = [
        ('təm', 'Təmir'),
        ('proqram', 'Proqram Təminatı'),
        ('virus', 'Virus Təmizlənməsi'),
        ('data', 'Data Bərpa'),
        ('digər', 'Digər'),
    ]

    first_name = models.CharField(max_length=100, verbose_name="Adınızı daxil edin")
    last_name = models.CharField(max_length=100, verbose_name="Soyadınızı daxil edin")
    phone_number = models.CharField(max_length=20, verbose_name="Azerbaijan +994")
    email = models.EmailField(null=True, verbose_name="Email ünvanınızı daxil edin")
    consultation_type = models.CharField(
        max_length=20,
        choices=CONSULTATION_CHOICES,
        default='təm',
        verbose_name="Konsultasiya seçin"
    )
    message = models.TextField(verbose_name="Mesajınızı daxil edin")

    def __str__(self):
        return f"{self.first_name}"
