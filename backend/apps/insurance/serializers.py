from django.db import transaction
from rest_framework import serializers

from .models import FieldOption, RiskField, Risk


class FieldOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOption
        fields = (
            'id',
            'name'
        )


class RiskFieldSerializer(serializers.ModelSerializer):
    options = FieldOptionSerializer(
        many=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = RiskField
        fields = (
            'id',
            'label',
            'type',
            'required',
            'active',
            'options'
        )


class RiskSerializer(serializers.ModelSerializer):
    fields = RiskFieldSerializer(
        many=True,
        required=True
    )

    class Meta:
        model = Risk
        fields = (
            'id',
            'name',
            'description',
            'active',
            'fields'
        )

    @transaction.atomic()
    def create(self, validated_data):
        fields = validated_data.pop('fields')
        risk = Risk.objects.create(
            **validated_data
        )

        for field in fields:
            field['risk'] = risk
            options = field.pop('options', None)
            field_ob = RiskField.objects.create(
                **field
            )

            for option in options:
                option['field'] = field_ob
                FieldOption.objects.create(
                    **option
                )
        return risk
