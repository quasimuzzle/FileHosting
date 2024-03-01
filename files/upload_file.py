from django.shortcuts import render, redirect
from .forms import FileForm

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            return redirect('file_detail', file_id=file.pk)
    else:
        form = FileForm()
    return render(request, 'files/upload_file.html', {'form': form})
