from django.contrib.auth import authenticate
from django.db import IntegrityError
from recipe.models import User


def register_user(form):
	try:
		user = User.objects.create_user(
			username=form.cleaned_data["username"],
			password=form.cleaned_data["password"],
		)
		return True
	except IntegrityError:
		return False


def login_user(form):
	username = form.cleaned_data["username"]
	password = form.cleaned_data["password"]
	user = authenticate(username=username, password=password)
	if user is None:
		return False
	return user
