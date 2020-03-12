from django import forms

from .models import Post,Gato,Articulo

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('nombre','email', 'text',)

class GatoForma(forms.ModelForm):

	class Meta:
		model = Gato
		fields = ('nombre','descripcion','foto',)

class ArticuloForma(forms.ModelForm):
	
	class Meta:
		model = Articulo
		fields = ('autor','nombre','texto','foto',)