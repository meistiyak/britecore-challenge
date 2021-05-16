from django.db import models


class Risk(models.Model):
    name = models.CharField(
        null=False,
        max_length=128
    )
    description = models.CharField(
        null=True,
        blank=True,
        max_length=255
    )
    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class RiskField(models.Model):
    risk = models.ForeignKey(
        to=Risk,
        related_name='fields',
        on_delete=models.CASCADE
    )
    label = models.CharField(
        max_length=128
    )
    type = models.CharField(
        max_length=20
    )
    required = models.BooleanField(
        default=False
    )
    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.risk.name + '-' + self.label


class FieldOption(models.Model):
    field = models.ForeignKey(
        to=RiskField,
        related_name='options',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=128
    )

    def __str__(self):
        return self.field.label + '-' + self.name
