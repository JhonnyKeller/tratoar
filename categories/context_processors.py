from .models import Categories


def get_categories(request):
    return {'categories_cp': Categories.objects.all()}
