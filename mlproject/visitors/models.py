from django.db import models

# Create your models here.
class Visitor(models.Model):

    full_name = models.CharField(
        verbose_name = 'Full name',
        max_length = 194,
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=11,
    )

    birth_date = models.DateField(
        verbose_name='Birth date',
        auto_now=False,
        auto_now_add=False, # Optional
    )

    house_number = models.PositiveSmallIntegerField(
        verbose_name='House number',
    )

    vehicle_sign = models.CharField(
        verbose_name='Vehicle Sign',
        max_length=7,
        blank=True,
        null=True
    )

    entrance_time = models.DateTimeField(
        verbose_name='Time of arrival',
        auto_now_add=True,
    )

    exit_time = models.DateTimeField(
        verbose_name='Exiting time',
        auto_now = False,
        blank=True,
        null=True
    )

    authorization_time = models.DateTimeField(
        verbose_name='Entrance authorization time',
        auto_now=False,
        blank=True,
        null=True,
    )

    responsible = models.CharField(
        verbose_name='Name of people responsible for the visitor',
        max_length=194,
        blank=True
     )
    
    registered_by = models.ForeignKey(
        'porteiros.porteiro',
        verbose_name='Porteiro responsible for registering visit',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name='Visitor'
        verbose_name_plural='Visitors'
        db_table='visitor'

    def __str__(self) -> str:
        return self.full_name
    