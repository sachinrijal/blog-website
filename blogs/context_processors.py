from .models import Category


def categoryget(request):
    category = Category.objects.all()
    context ={
        'category':category
    }
    return dict(context)

