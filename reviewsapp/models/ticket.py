from django.conf import settings
from django.db import models


class Ticket(models.Model):
    # Your Ticket model definition goes here
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, "url"):
            return self.image.url

    def save(self, *args, **kwargs):
        try:
            this = Ticket.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except Exception:
            pass
        super(Ticket, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Ticket, self).delete(*args, **kwargs)

    def __str__(self):
        return (
            f"title: {self.title}, description: {self.description}, user: {self.user}"
        )
