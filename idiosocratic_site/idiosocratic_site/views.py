def placeholder(request, width, height):
  
  return HttpResponse('Ok')
  

from django import forms  

from django.core.cache import cache
  
class ImageForm(forms.Form):

  """Form to validate requested placeholder image."""
  
  height = forms.IntegerField(min_value=1, max_value=2000)  
  width = forms.IntegerField(min_value=1, max_value=2000) 