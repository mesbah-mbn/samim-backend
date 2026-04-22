from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lead(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        CONTACTED = "contacted", "Contacted"
        OFFER_SENT = "offer_sent", "Offer sent"
        WON = "won", "Won"
        LOST = "lost", "Lost"

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    email = models.EmailField(blank=True, null=True)

    postcode = models.CharField(max_length=20)

    message = models.TextField(blank=True, null=True)

    product = models.CharField(max_length=200, blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    admin_notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
