from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from recipe.forms.user_forms import *
from recipe.services.account import *
from recipe.services.recipe import *
# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddRecipeView(View):
	template_name = 'index.html'

	def get(self, request, *agrs, **kwargs):
		recipe_list = get_recipes()
		return render(request, self.template_name,{'recipe_list':recipe_list})

	def post(self, request, *agrs, **kwargs):
		form = request.POST
		pictures = request.FILES.getlist('food_images')
		print(pictures)
		status = add_recipe(form, pictures, request.user)
		return redirect('recipe:add_recipe')

@method_decorator(login_required, name='dispatch')
class UpdateRecipeView(View):
	template_name = 'index.html'

	def get(self, request, recipe_id, *agrs, **kwargs):
		recipe_details = get_recipes(recipe_id)
		return render(request, self.template_name, {'recipe_details':recipe_details})

	def post(self, request, recipe_id, *agrs, **kwargs):
		form = request.POST
		print(form)
		pictures = request.FILES.getlist('food_images')
		status = update_recipe(form, pictures, recipe_id)
		return redirect('recipe:add_recipe')

class UserRegistrationView(View):

	template_name = 'user_form.html'
	form_class = SignupForm

	def get(self, request, *agrs, **kwargs):
		if request.user.is_authenticated:
			return redirect("recipe:add_recipe")
		else:
			signup_form = self.form_class()
			return render(request, self.template_name, {"signup_form": signup_form})

	def post(self, request, *args, **kwargs):
		signup_form = self.form_class(request.POST)
		if signup_form.is_valid():
			status = register_user(signup_form)
			if status:
				return redirect('recipe:add_recipe')
			else:
				return render(request, self.template_name,{'signup_form': signup_form})
		else:
			return render(request, self.template_name,{"signup_form": signup_form})

class LoginView(View):

	template_name = 'user_form.html'
	form_class = LoginForm

	def get(self, request, *args, **kwargs):
		login_form = self.form_class()
		print(login_form)
		return render(request, self.template_name, {'login_form': login_form})

	def post(self, request, *args, **kwargs):
		login_form = self.form_class(request.POST)
		if login_form.is_valid():
			user = login_user(login_form)
			if user:
				login(request, user)
				return redirect('recipe:add_recipe')
			else:
				return render(request, self.template_name, {'login_form': login_form})
		else:
			return render(request, self.template_name, {'login_form': login_form})

@login_required
def delete_recipe(request, recipe_id):
	delete_recipe_by_id(recipe_id)
	return redirect('recipe:add_recipe')

def logout_user(request):
	logout(request)
	return redirect('recipe:login')