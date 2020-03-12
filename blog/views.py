from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, Gato, Articulo
from django.utils import timezone
from .forms import PostForm, GatoForma, ArticuloForma


def index(request):
	gatos = Gato.objects.all()
	return render (request, 'blog/index.html', {'gatos': gatos})

def usr_registro(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render (request, 'blog/usr_registro.html',{'posts' : posts})

def nosotros(request):
	return render(request, 'blog/nosotros.html')
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html',{'post': post})

def adopcion(request):
	gatos = Gato.objects.all()
	return render( request, 'blog/adopcion.html', {'gatos': gatos})

def blog(request):
	articulos = Articulo.objects.all()
	return render( request, 'blog/blog.html',{'articulos':articulos})

def form_articulo(request):
	if request.method == "POST":
		forma_articulo = ArticuloForma(request.POST)

		if forma_articulo.is_valid():
			articulos = form_articulo.save(commit=False)
			articulos.save()

	else:
		forma_articulo = ArticuloForma()

	return render(request, 'blog/forma_articulo.html',{'forma_articulo':forma_articulo})


def form_gato(request):
	if request.method == "POST":
		gato_forma = GatoForma(request.POST)

		if gato_forma.is_valid():
			gato_p = gato_forma.save(commit=False)
			gato_p.save()
			return render( request, 'blog/adopcion.html')

	else:
		gato_forma = GatoForma()

	return render(request, 'blog/form_gato.html',{'gato_forma': gato_forma})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)

		if form.is_valid():
			post = form.save(commit=False)
			post.published_date = timezone.now()
			post.save()
			return render( request, 'blog/index.html')

	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html',{'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})