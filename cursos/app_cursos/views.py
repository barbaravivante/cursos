from django.http import HttpResponse
from ast import Return
from django.shortcuts import render
from app_cursos.models import Curso, Alumno, Profesor
from app_cursos.forms import Alta_cursos, Alta_alumnos, Alta_profesor, UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.

#CREAR LOS DISTINTOS LINK
def inicio(request):  
    return render( request , "index.html" )

def about(request):  
    return render( request , "about.html" )    

def contacto(request):
    return render( request , "contacto.html" )

def index_admin(request):
     return render( request , "index_admin.html" )      

#LISTADO DE CURSOS
def lista_cursos(request):
    curso = Curso.objects.all()
    datos = {"datos" : curso}
    return render(request , "lista_cursos.html" , datos)       

#LISTADO DE ALUMNOS
def lista_alumnos(request):
    alumno = Alumno.objects.all()
    datos = {"datos" : alumno}
    return render(request , "lista_alumnos.html" , datos)   

#LISTADO DE PROFESORES
def lista_profesor(request):
    profesor = Profesor.objects.all()
    datos = {"datos" : profesor}
    return render(request , "lista_profesores.html" , datos)        

#BUSCAR CURSOS
def buscar_curso(request):
    return render( request , "buscar_curso.html")

#RESULTADO DE LA BUSQUEDA
def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")     


#LISTADO DE CURSOS Administrador
@login_required
def cursos_admin(request):
    curso = Curso.objects.all()
    datos = {"datos" : curso}
    return render(request , "cursos_admin.html" , datos)   

#CREAR CURSOS
@login_required
def alta_cursos(request):

    if request.method == "POST":

        mi_formulario = Alta_cursos( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'])
            curso.save()

            return render( request , "alta_curso.html")

    return render( request, "alta_curso.html")

#CREAR ALUMNOS
@login_required
def alta_alumno(request): 

    if request.method == "POST":

        mi_formulario = Alta_alumnos( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            alumno = Alumno( nombre=datos['nombre'] , camada=datos['camada'], nacimiento=datos['nacimiento'])
            alumno.save()

            return render( request , "alta_alumnos.html")

    return render( request, "alta_alumnos.html")

#LISTADO DE ALUMNOS Administrador
@login_required
def alumnos_admin(request):
    alumno = Alumno.objects.all()
    datos = {"datos" : alumno}
    return render(request , "alumnos_admin.html" , datos) 

#LISTADO DE PROFESORES Administrador
@login_required
def profesor_admin(request):
    profesor = Profesor.objects.all()
    datos = {"datos" : profesor}
    return render(request , "profesor_admin.html" , datos) 


#CREAR PROFESORES
@login_required
def alta_profesor(request): 

    if request.method == "POST":

        mi_formulario = Alta_profesor( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            profesor = Profesor( nombre=datos['nombre'] , camada=datos['camada'], nacimiento=datos['nacimiento'])
            profesor.save()

            return render( request , "alta_profesor.html")

    return render( request, "alta_profesor.html")

#ELIMINAR CURSOS
def elimina_curso( request , id):

    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos_admin.html" , {"cursos": curso})

#ELIMINAR ALUMNO
def elimina_alumno( request , id):

    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    alumno = Alumno.objects.all()

    return render(request , "alumnos_admin.html" , {"alumno": alumno})

#ELIMINAR Profesor
def elimina_profesor( request , id):

    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    profesor = Profesor.objects.all()

    return render(request , "profesor_admin.html" , {"profesor": profesor})    

#EDITAR CURSOS
@login_required
def editar( request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alta_cursos( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

            curso = Curso.objects.all()          
            return render(request , "cursos_admin.html" , {"cursos": curso})
    else:
        mi_formulario = Alta_cursos(initial={'nombre':curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario":mi_formulario, "curso": curso})
   
#EDITAR Alumnos
@login_required
def editar_alumno( request , id):

    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alta_alumnos( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos['nombre']
            alumno.camada = datos['camada']
            alumno.nacimiento = datos['nacimiento']
            alumno.save()

            alumno = Alumno.objects.all()          
            return render(request , "alumnos_admin.html" , {"alumno": alumno})
    else:
        mi_formulario = Alta_alumnos(initial={'nombre':alumno.nombre , "camada":alumno.camada, "nacimiento":alumno.nacimiento})
    
    return render( request , "editar_alumno.html" , {"mi_formulario":mi_formulario, "alumno": alumno})

#EDITAR Profesor
@login_required
def editar_profesor( request , id):

    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alta_profesor( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos['nombre']
            profesor.camada = datos['camada']
            profesor.nacimiento = datos['nacimiento']
            profesor.save()

            profesor = Profesor.objects.all()          
            return render(request , "profesor_admin.html" , {"profesor": profesor})
    else:
        mi_formulario = Alta_profesor(initial={'nombre':profesor.nombre , "camada":profesor.camada, "nacimiento":profesor.nacimiento})
    
    return render( request , "editar_profesor.html" , {"mi_formulario":mi_formulario, "profesor": profesor})

#lOGIN DEL USUARIO ADMIN
def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request,user)
                #avatares = Avatar.objects.filter(user=request.user.id)
                #return render( request , "index_admin.html", {"url":avatares[0].imagen.url}})
                return render( request , "index_admin.html" , {"mensaje":f" {usuario}"})
            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:         
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()

    return render( request , "login.html" , {"form":form})



#Registro de Usuario Admin
def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return render( request , "index_admin.html")
            #return HttpResponse("Usuario creado")
           
    else:
        form = UserCreationForm()
    return render( request , "registro.html" , {"form":form})


#Editar  Usuario Admin
@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            #usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render( request , "index_admin.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render( request , "editar_usuario.html" , {"miFormulario":miFormulario , "usuario":usuario})



