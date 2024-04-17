
from django.shortcuts import render, redirect, get_object_or_404
from .models import Kategoribuku
from buku.models import Buku
from .forms import KategoribukuForm
from django.contrib import messages

# FItur Peminjam
def Peminjam_Kategoribuku_list(request):
    query = request.GET.get('search') 
    kategoris = Kategoribuku.objects.all()
    if query:
        kategoris = kategoris.filter(namakategori__icontains=query) 
    return render(request, 'peminjam/peminjam_daftar_kategori.html', {'kategoris': kategoris})

def lihat_buku_per_kategori(request, kategori_id):
    kategori = Kategoribuku.objects.get(pk=kategori_id)
    bukus = Buku.objects.filter(kategoriid=kategori_id)
    return render(request, 'buku/peminjam_daftar_buku.html', {'kategori': kategori, 'bukus': bukus})

# FItur Admin
def Kategoribuku_list(request):
    query = request.GET.get('search') 
    kategoris = Kategoribuku.objects.all()
    if query:
        kategoris = kategoris.filter(namakategori__icontains=query) 
    return render(request, 'admin/daftar_kategori.html', {'kategoris': kategoris})

def create_Kategoribuku(request):
    if request.method == 'POST':
        form = KategoribukuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategoribuku telah berhasil ditambah!')
            return redirect('Kategoribuku:read')
    else:
        form = KategoribukuForm()
    return render(request, 'admin/kategori_form.html', {'form': form})

def update_Kategoribuku(request, kategoriid):
    kategoribuku = get_object_or_404(Kategoribuku, kategoriid=kategoriid)
    if request.method == 'POST':
        form = KategoribukuForm(request.POST, instance=kategoribuku)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategoribuku telah berhasil diubah!')
            return redirect('Kategoribuku:read')
    else:
        form = KategoribukuForm(instance=kategoribuku)

    return render(request, 'admin/kategori_form.html', {'form': form})

def delete_Kategoribuku(request, kategoriid):
    kategoribuku = get_object_or_404(Kategoribuku, kategoriid=kategoriid)
    kategoribuku.delete()
    return redirect('Kategoribuku:read')

# Menghitung total data kategori
def total_data_kategori(request):
    total = Kategoribuku.objects.all().count()# Memanggil fungsi tanpa argumen
    return total

# FItur Petugas
def petugas_Kategoribuku_list(request):
    query = request.GET.get('search') 
    kategoris = Kategoribuku.objects.all()
    if query:
        kategoris = kategoris.filter(namakategori__icontains=query) 
    return render(request, 'petugas/petugas_daftar_kategori.html', {'kategoris': kategoris})

def create_Kategoribuku_petugas(request):
    if request.method == 'POST':
        form = KategoribukuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategoribuku telah berhasil ditambah!')
            return redirect('Kategoribuku:read_petugas')
    else:
        form = KategoribukuForm()
    return render(request, 'petugas/petugas_kategori_form.html', {'form': form})

def update_Kategoribuku_petugas(request, kategoriid):
    kategoribuku = get_object_or_404(Kategoribuku, kategoriid=kategoriid)
    if request.method == 'POST':
        form = KategoribukuForm(request.POST, instance=kategoribuku)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategoribuku telah berhasil diubah!')
            return redirect('Kategoribuku:read_petugas')
    else:
        form = KategoribukuForm(instance=kategoribuku)

    return render(request, 'petugas/petugas_kategori_form.html', {'form': form})

def delete_Kategoribuku_petugas(request, kategoriid):
    kategoribuku = get_object_or_404(Kategoribuku, kategoriid=kategoriid)
    kategoribuku.delete()
    return redirect('Kategoribuku:read_petugas')