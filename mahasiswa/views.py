from .models import Data_mahasiswa
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BiodataMhs
# Create your views here.


def index(request):
    hasil = Data_mahasiswa.objects.all()
    data = {
        'data': hasil,
    }
    return render(request, "index.html", data)


def tambah(request):
    form = BiodataMhs(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/mahasiswa")
        pass
    return render(request, "tambahdata.html", {'form': form})


def edit(request, npm):
    obj = get_object_or_404(Data_mahasiswa, npm=npm)

    form = BiodataMhs(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/mahasiswa")
    data = {
        'mhs': obj,
    }
    return render(request, 'editdata.html', data)


def hapus(request, npm):
    dt = Data_mahasiswa.objects.get(npm=npm)
    dt.delete()
    return redirect("/mahasiswa")
