from django.db import models
from .utils import choices as ch
from django.core.validators import MaxValueValidator, MinValueValidator


class CommandsModel(models.Model):
    wbmode = models.CharField(
        max_length=50,
        choices=ch.wbmode_choices,
        null=True,
        blank=True
    )
    saturation = models.IntegerField(
        choices=ch.saturation_choices
    )
    sensor_id = models.IntegerField(
        choices=ch.sensor_id_choices
    )

    exposuretime = models.BigIntegerField(
        validators= [
            MinValueValidator(34000),
            MaxValueValidator(358733000)
        ])

    gain = models.IntegerField(
        validators= [
            MinValueValidator(1),
            MaxValueValidator(16)
        ])
        
    ispdigitalgain = models.IntegerField(
        validators= [
            MinValueValidator(1),
            MaxValueValidator(8)
        ])
        
    tnr_mode = models.CharField(
        max_length=50,
        default='NoiseReduction_Fast',
        choices=ch.tnr_mode_choices
        )
    ee_mode = models.CharField(
        max_length=50,
        default='EdgeEnhancement_Fast',
        choices=ch.ee_mode_choices
        )
    aeantibanding = models.CharField(
        max_length=50,
        default='AeAntibandingMode_Auto',
        choices=ch.aeantibanding_choices
        )
    
    exposurecompensation = models.IntegerField(
        default=0,
        validators= [
            MinValueValidator(-2),
            MaxValueValidator(2)
        ])
        
    aelock = models.BooleanField(default=False)
    awblock = models.BooleanField(default=False)