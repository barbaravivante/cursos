from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about" , views.about, name="about"),
    path("lista_cursos" , views.lista_cursos, name="lista_cursos"),
    path("lista_alumnos" , views.lista_alumnos, name="lista_alumnos"),
    path("lista_profesor" , views.lista_profesor, name="lista_profesor"),
    path("buscar_curso" , views.buscar_curso, name="buscar_curso"),
    path("buscar" , views.buscar, name="buscar"),
    path("contacto" , views.contacto, name="contacto"),
    path("alta_cursos" , views.alta_cursos,name="alta_cursos"),
    path("alta_alumno" , views.alta_alumno,name="alta_alumno"),
    path("alta_profesor" , views.alta_profesor,name="alta_profesor"),
    path("index_admin" , views.index_admin,name="index_admin"),
    path("cursos_admin" , views.cursos_admin,name="cursos_admin"),
    path("alumnos_admin" , views.alumnos_admin,name="alumnos_admin"),
    path("profesor_admin" , views.profesor_admin,name="profesor_admin"),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("elimina_alumno/<int:id>" , views.elimina_alumno , name="elimina_alumno"),
    path("elimina_profesor/<int:id>" , views.elimina_profesor , name="elimina_profesor"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("editar_curso" , views.editar ,name="editar_curso"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    path("editar_alumno" , views.editar_alumno ,name="editar_alumno"),
    path("editar_profesor/<int:id>" , views.editar_profesor , name="editar_profesor"),
    path("editar_profesor" , views.editar_profesor ,name="editar_profesor"),
    path("login" , views.login_request , name="login"),
    path("register" , views.register , name="register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="logout"),
    path("editarUsuario" , views.editarUsuario , name="editarUsuario"),
    #path("avatar" , views.login_request , name="avatar")

]
