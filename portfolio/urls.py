from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('apresentacao', views.apresentacao_page_view, name='apresentacao'),
    path('apresentacao/licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('apresentacao/escolas', views.escolas_page_view, name='escolas'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('blog', views.blog_page_view, name='blog'),
    path('blog/novapublicacao', views.nova_publicacao_page_view, name='novapublicacao'),
    path('blog/editar/<int:publicacao_id>', views.editar_publicacao_page_view, name='editarpublicacao'),
    path('blog/apagar/<int:publicacao_id>', views.apagar_publicacao_page_view, name='apagarpublicacao'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('quiz', views.quiz_view_page, name='quiz')
]