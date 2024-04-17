from django.urls import path
from . import views

app_name = 'Peminjaman'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('list/', views.Peminjaman_list, name='read'),
    path('create/<str:bukuid>/', views.create_Peminjaman, name='create'),
    path('update/<str:peminjamanid>/', views.update_Peminjaman, name='update'),
    path('delete/<str:peminjamanid>/', views.delete_Peminjaman, name='delete'),

    # Admin roles
    path('admin/list/', views.admin_peminjaman_list, name='admin-read'),
    path('admin/update/<str:peminjamanid>/', views.update_Peminjaman_admin, name='update_admin'),
    path('admin/delete/<str:peminjamanid>/', views.delete_Peminjaman, name='delete_admin'),
    path('laporan/<int:peminjaman_id>/', views.generate_laporan_peminjaman, name='generate_laporan_peminjaman'),
    # konfirmasi peminjaman
    path('konfirmasi-peminjaman/<int:peminjamanid>/', views.konfirmasi_peminjaman, name='konfirmasi_peminjaman'),
    path('konfirmasi-pengembalian/<int:peminjamanid>/', views.konfirmasi_pengembalian, name='konfirmasi_pengembalian'),
    
    # petugas roles
    path('petugas/list/', views.petugas_peminjaman_list, name='petugas-read'),
    path('petugas/update/<str:peminjamanid>/', views.update_Peminjaman_petugas, name='petugas-update'),
    path('petugas/delete/<str:peminjamanid>/', views.delete_Peminjaman_petugas, name='petugas-delete'),
    # konfirmasi peminjaman
    path('petugas/konfirmasi-peminjaman/<int:peminjamanid>/', views.konfirmasi_peminjaman_petugas, name='konfirmasi_peminjaman_petugas'),
    path('petugas/konfirmasi-pengembalian/<int:peminjamanid>/', views.konfirmasi_pengembalian_petugas, name='konfirmasi_pengembalian_petugas'),
]