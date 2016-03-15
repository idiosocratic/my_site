import os

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join

def get_page_or_404(name):
  """Return content or 404"""
  try:
    file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
  except ValueError: 
    raise Http404('Page Not Found')
  else:
    if not os.path.exists(file_path):
      raise Http404('Page Not Found')
      
  with open(file_path, 'r') as f:
    page = Template(f.read())
    
  return page        
     
  

def placeholder(request, width, height):
  
  return HttpResponse('Ok')
  

from django import forms  

from django.core.cache import cache
  
class ImageForm(forms.Form):

  """Form to validate requested placeholder image."""
  
  height = forms.IntegerField(min_value=1, max_value=2000)  
  width = forms.IntegerField(min_value=1, max_value=2000) 