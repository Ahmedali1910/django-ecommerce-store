from django.urls import path
from . import views
urlpatterns=[
path('',views.home,name="home"),
path ('products/',views.products,name="product_list"),
path('details/<int:id>/',views.details,name="product_details"),
path('categorize/<int:id>/',views.categorize,name='categorize'),
path('search/<str:price>/',views.search_by_price,name="search"),    
path('create/',views.create,name="create"),
path('edit/<int:id>/',views.edit,name="edit"),
path('delete/<int:id>/',views.delete,name='delete'),
path('categories/',views.category_list,name='categories'),
]