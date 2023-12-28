from django.db import models

# Create your models here.
class Porteiro(models.Model):
    
    user = models.OneToOneField(  # Link a user to each porteiro object
        verbose_name='User',
        on_delete=models.PROTECT,
        to='usuarios.User'
    )

    full_name = models.CharField(
        verbose_name='Full name',
        max_length = 194,
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=11,
    )

    phone_number = models.CharField(
        verbose_name='Phone number',
        max_length=11,
    )

    birth_date = models.DateField(
        verbose_name='Birth date',
        auto_now=False,
        auto_now_add=False, # Optional
    )

    USERNAME_FIELD = 'full_name'


    class Meta:
        verbose_name = 'Porteiro'
        verbose_name_plural = 'Porteiros'
        db_table = 'porteiro'

    def __str__(self) -> str:
        return self.full_name