from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Category

#usando CBV

class ProductListView(generic.ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 3

product_list = ProductListView.as_view()



'''
view com funçoes

def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)
'''


class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 3

#Obter a lista de itens para esta view. Este deve ser um iterable e pode ser um queryset
# (em que o comportamento específico do queryset será ativado).
#queryset , é uma lista de objetos de um dado modelo.
    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

#Retorna dados de contexto para exibir a lista de objetos.
    def get_context_data(self, **kwargs):

        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()





'''

def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category),

    }

    return render(request, 'catalog/category.html',context)

'''







def product(request, slug):
    product = Product.objects.get(slug=slug)

    context = {
        'product':product

    }
    return render(request, 'catalog/product.html',context)
