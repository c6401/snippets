from django.urls import resolve

func, args, kwargs = resolve(path)
module = func.__module__
name = func.__name__
