from recipe.models import *

def add_recipe(form, pictures, user):
	recipe = Recipe()
	recipe.owner = User.objects.get(username=user.username)
	recipe.food = form['food_name']
	recipe.food_desc = form['food_desc']
	recipe.time_to_prepare = form['time_takes']
	recipe.save()
	for i in form.getlist('ingredients'):
		ingredient ,_ = Ingredients.objects.get_or_create(ingredient=i, quantity=1)
		recipe.ingredients.add(ingredient)
	for i in form.getlist('tags'):
		tag ,_ = Tags.objects.get_or_create(tag=i)
		recipe.tags.add(tag)
	if pictures:
		for pic in pictures:
			p = FoodImages()
			p.food = recipe
			p.image = pic
			p.save()



def update_recipe(form, pictures, id):
	recipe = Recipe.objects.get(id=id)
	recipe.food = form['food_name']
	recipe.food_desc = form['food_desc']
	recipe.time_to_prepare = form['time_takes']
	recipe.save()
	recipe.ingredients.clear()
	recipe.tags.clear()
	for i in form.getlist('ingredients'):
		ingredient ,_ = Ingredients.objects.get_or_create(ingredient=i, quantity=1)
		recipe.ingredients.add(ingredient)
	for i in form.getlist('tags'):
		tag ,_ = Tags.objects.get_or_create(tag=i)
		recipe.tags.add(tag)

	if pictures:
		p = FoodImages.objects.filter(food=recipe)
		p.delete()
		for pic in pictures:
			p = FoodImages()
			p.food = recipe
			p.image = pic
			p.save()


def get_recipes(recipe_id=None):
	if recipe_id is None:
		recipes = Recipe.objects.all()
		return recipes
	else:
		try:
			recipe = Recipe.objects.get(id=recipe_id)
		except Recipe.DoesNotExist:
			recipe = []
		return recipe

def delete_recipe_by_id(recipe_id):
	try:
		recipe = Recipe.objects.get(id=recipe_id)
		recipe.delete()
		return True
	except Recipe.DoesNotExist:
		return False
