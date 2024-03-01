from django.shortcuts import render, get_object_or_404, redirect
from .models import File, Comment, Rating
from .forms import FileForm, CommentForm
from django.contrib.auth.decorators import login_required


def file_list(request):
    files = File.objects.all()
    return render(request, 'files/file_list.html', {'files': files})

def file_detail(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    comments = Comment.objects.filter(file=file)
    return render(request, 'files/file_detail.html', {'file': file, 'comments': comments})

def add_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            return redirect('file_detail', file_id=file.pk)
    else:
        form = FileForm()
    return render(request, 'files/add_file.html', {'form': form})

def delete_file(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    if request.method == 'POST':
        file.delete()
        return redirect('file_list')
    return render(request, 'files/delete_file.html', {'file': file})
    
def add_comment(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.file = file
            comment.save()
            return redirect('file_detail', file_id=file_id)
    else:
        form = CommentForm()
    return render(request, 'files/add_comment.html', {'form': form})

def add_rating(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    if request.method == 'POST':
        rating_value = request.POST['rating']
        Rating.objects.create(file=file, value=rating_value)
        return redirect('file_detail', file_id=file_id)
    

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.uploaded_by = request.user  # присваиваем полю uploaded_by текущего пользователя
            new_file.save()
            return redirect('file_detail', file_id=new_file.pk)
    else:
        form = FileForm()
    return render(request, 'files/upload_file.html', {'form': form})