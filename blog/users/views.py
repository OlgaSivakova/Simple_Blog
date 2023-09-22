from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreationForm
from django.contrib.auth import authenticate, login


from django.views.generic.base import View #для представления по классам
from .models import Post, Likes
from .forms import CommentsForm, PostForm
from django.db.models import Q
 
# Create your views here.
class Register(View):
    template_name = 'registration/register.html'
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = UserCreationForm(request.POST) #передаём данные которые на этапе регистрации пришли от пользователя чтобы его залогинить
        if form.is_valid():
            form.save() #сохр пользователя
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password) #передача данных
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

# Create your views here.

class PostView(View):
    
    def get(self, request): #request -инфа от пользователя, self = имя модели
        searchq = request.GET.get('search', '')
        if searchq:
            posts = Post.objects.filter(Q(title =searchq) | Q(descript=searchq))
            
        else:
            posts = Post.objects.all()
        return render(request, 'base.html', {'post_list': posts})
    
    
    
    
class PostElement(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk) #одна запись
        return render(request, 'blogelement.html', {'post': post} )
    
class DelElement(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk) #одна запись
        post.delete()
        return redirect('home')

class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST) #получить все данные, которые в форме в теймплейте ввёл пользователь
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk #получаем конкретное айди поста
            form.save()
        return redirect(f'/{pk}')
        
    

    
def addpost(request):
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_entry = Post()
            post_entry.title = form.cleaned_data['title']
            post_entry.descript = form.cleaned_data['descript']
            post_entry.author = form.cleaned_data['author']
            
            
            post_entry.img = form.cleaned_data['img']
            

            post_entry.save()

            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'addposts.html', {'form':form})


def get_client_ip(request):
    x_forw = request.META.get('HTTP_X_FORW')
    if x_forw:
        ip = x_forw.split(',')[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

class AddLike(View):
    def get(self,request,pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.p = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')
        
        
class DelLike(View):
    def get(self,request,pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}') #удаляем запись из модели по ай пи
        except:
           
            return redirect(f'/{pk}')
    