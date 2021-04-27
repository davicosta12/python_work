from django.db import models
# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=60)

    def _str_(self):
        """Devolve uma representação em string do modelo."""
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.name
