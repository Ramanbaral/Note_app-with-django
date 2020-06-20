from django.shortcuts import render,redirect
from .models import note
from django.views.generic import UpdateView

# Create your views here.
def index(request):
    if request.method == 'POST':
        user_inp_title=request.POST.get('title')
        user_inp_note=request.POST.get('note')
        created_note=note(title=user_inp_title,body=user_inp_note)
        created_note.save()

    notes=note.objects.all()
    return render(request,'Note_app/index.html',{'notes':notes})

def delete(request,pk):
    user_note=note.objects.filter(id=pk)
    user_note.delete()
    print(pk)
    return redirect('note-home')

def update(request,pk):
    #i need to get the values that already exists in title and body to update and update
    user_note=note.objects.filter(id=pk)
    notes=note.objects.all()
    return render(request,'Note_app/update.html',{'notes':notes,'user_note':user_note})

class NoteUpdateFrom(UpdateView):
    model=note
    template_name='Note_app/update.html'
    success_url='/notes'
    fields=['title','body']

def search(request):
    query=request.GET.get('search')
    print(query)
    notes=note.objects.filter(title__icontains=query)
    return render(request,'Note_app/search.html',{'notes':notes})
