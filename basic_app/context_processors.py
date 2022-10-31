from .forms import contactForm


def get_contactForm(request):
    return {'contactForm':contactForm(),}
