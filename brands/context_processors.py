from .models import AcBrands


def get_brands(request):
    return {'brands': AcBrands.objects.all()}
