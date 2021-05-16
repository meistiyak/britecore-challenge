import factory


class RiskFactory(factory.django.DjangoModelFactory):
    name = 'Vehicle'

    class Meta:
        model = 'insurance.Risk'


class RiskFieldFactory(factory.django.DjangoModelFactory):
    label = 'Gender'
    type = 'select'
    risk = factory.SubFactory(RiskFactory)

    class Meta:
        model = 'insurance.RiskField'


class FieldOptionFactory(factory.django.DjangoModelFactory):
    name = 'Male'
    field = factory.SubFactory(RiskFieldFactory)

    class Meta:
        model = 'insurance.FieldOption'
