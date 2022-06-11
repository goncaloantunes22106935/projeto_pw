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
    path('quiz', views.quiz_view_page, name='quiz'),
    path('projetos/tcf', views.projetos_finais_page_view, name='tcf'),
    path('projetos/tcf/adicionar', views.novo_tcf_page_view, name='novotcf'),
    path('projetos/tcf/editar/<int:tcf_id>', views.editar_tcf_page_view, name='editartcf'),
    path('projetos/tcf/apagar/<int:tcf_id>', views.apagar_tcf_page_view, name='apagartcf'),
    path('api', views.api_page_view, name='api')
]
