from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Buku, Kategoribuku
from .forms import BukuForm
from django.contrib import messages

# Fitur Peminjam
def list_buku_peminjam(request):
    query = request.GET.get('search')  # Ambil query pencarian dari parameter GET 'q'
    bukus = Buku.objects.all()
    if query:
        bukus = bukus.filter(judul__icontains=query)  # Filter buku berdasarkan judul yang mengandung query
    return render(request, 'buku/peminjam_daftar_buku.html', {'bukus': bukus})

# FItur Admin
def list_buku_admin(request):
    query = request.GET.get('search')  # Ambil query pencarian dari parameter GET 'q'
    bukus = Buku.objects.all()
    if query:
        bukus = bukus.filter(judul__icontains=query)
    return render(request, 'buku/daftar_buku.html', {'bukus': bukus})

def create_buku(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Buku telah berhasil ditambah!')
            return redirect('buku:list_admin')
    else:
        form = BukuForm()
    categories = Kategoribuku.objects.all()
    return render(request, 'buku/buku_form.html', {'form': form, 'categories': categories})

def update_buku(request, buku_id):
    buku = get_object_or_404(Buku, pk=buku_id)
    if request.method == 'POST':
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, 'Buku telah berhasil diubah!')
            return redirect('buku:list_admin')
    else:
        form = BukuForm(instance=buku)  # Ini akan mengisi form dengan nilai-nilai yang ada dalam objek buku
        # Ambil semua kategori buku
        categories = Kategoribuku.objects.all()
        return render(request, 'buku/buku_form.html', {'form': form, 'categories': categories})

def delete_buku(request, buku_id):
    buku = get_object_or_404(Buku, pk=buku_id)
    buku.delete()
    return redirect('buku:list_admin')  # Arahkan pengguna kembali ke daftar buku setelah menghapus buku

# Fitur Petugas
def list_buku_petugas(request):
    query = request.GET.get('search')  # Ambil query pencarian dari parameter GET 'q'
    bukus = Buku.objects.all()
    if query:
        bukus = bukus.filter(judul__icontains=query)
    return render(request, 'buku/petugas_daftar_buku.html', {'bukus': bukus})

def create_buku_petugas(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Buku telah berhasil ditambah!')
            return redirect('buku:list_petugas')
    else:
        form = BukuForm()
    categories = Kategoribuku.objects.all()
    return render(request, 'buku/petugas_buku_form.html', {'form': form, 'categories': categories})

def update_buku_petugas(request, buku_id):
    buku = get_object_or_404(Buku, pk=buku_id)
    if request.method == 'POST':
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, 'Buku telah berhasil diubah!')
            return redirect('buku:list_petugas')
    else:
        form = BukuForm(instance=buku)  # Ini akan mengisi form dengan nilai-nilai yang ada dalam objek buku
        # Ambil semua kategori buku
        categories = Kategoribuku.objects.all()
        return render(request, 'buku/petugas_buku_form.html', {'form': form, 'categories': categories})

def delete_buku_petugas(request, buku_id):
    buku = get_object_or_404(Buku, pk=buku_id)
    buku.delete()
    return redirect('buku:list_petugas')  # Arahkan pengguna kembali ke daftar buku setelah menghapus buku

# Fitur Melihat total buku
def total_data_buku_tersedia(request):
    total = Buku.objects.filter(tersedia=True).count()  # Menghitung total buku yang tersedia
    return total

def total_data_buku_tidak(request):
    total = Buku.objects.filter(tersedia=False).count()  # Menghitung total buku yang tersedia
    return total

def total_data_buku(request):
    total = Buku.objects.count()  # Menghitung total buku yang tersedia
    return total