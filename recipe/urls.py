from django.urls import path, include
from recipe.views import *

app_name = 'recipe'

urlpatterns = [
	path('user/login/',LoginView.as_view(),name='login'),
	path('user/signup/',UserRegistrationView.as_view(),name='signup'),	
    path('',AddRecipeView.as_view(),name='add_recipe'),
    path('recipe/update/<int:recipe_id>',UpdateRecipeView.as_view(),name='update_recipe'),
    path('recipe/delete/<int:recipe_id>',delete_recipe, name='delete_recipe'),
    path('logout/',logout_user,name='logout_user')
]
