# ClassroomHub

**Laboratorio 09 — Formularios y CRUD con Django: vistas, ModelForm y permisos**

**Aprendiz:** Juan Manuel Quintero Murcia  
**Ficha:** 3388087  
**Programa:** Análisis y Desarrollo de Software  
**Repositorio:** [ClassroomHub](https://github.com/juanlsk29/ClassroomHub)  
**Rama de entrega:** [`laboratorio-9`](https://github.com/juanlsk29/ClassroomHub/tree/laboratorio-9)

## 1. Descripción del proyecto

ClassroomHub es una aplicación web educativa desarrollada con Django que permite consultar y gestionar recursos organizados por categorías. El proyecto conserva la información en MariaDB y utiliza el sistema de autenticación, sesiones, grupos y permisos de Django.

Su desarrollo se ha realizado de manera progresiva:

| Laboratorio | Avance |
|---|---|
| 06 | Creación de rutas, vistas, plantillas y navegación entre páginas públicas. |
| 07 | Integración de MariaDB, modelos `Category` y `Resource`, migraciones, consultas mediante el ORM y administración de datos con Django Admin. |
| 08 | Registro de usuarios, inicio y cierre de sesión, panel privado, contador de visitas, revisión del catálogo mediante permisos y resumen privado. |
| 09 | Formularios con `ModelForm`, detalle público, creación, actualización y eliminación de recursos mediante vistas genéricas, permisos por operación y búsqueda pública por título. |

En el Laboratorio 09, las cuentas autorizadas pueden gestionar recursos desde una interfaz propia de ClassroomHub. Ya no es necesario utilizar Django Admin para cada modificación del catálogo.

Los visitantes continúan teniendo acceso a la lista, el detalle y la búsqueda. Las categorías siguen administrándose exclusivamente desde Django Admin.

## 2. Tecnologías y versiones

| Componente | Tecnología o versión |
|---|---|
| Lenguaje | Python 3.14.5 |
| Framework | Django 6.1.3 |
| Motor de base de datos | MariaDB 13.0.2 |
| Controlador SQL | mysqlclient 2.3.0 |
| Variables de entorno | python-dotenv 1.2.4 |
| Interfaz | HTML, CSS y plantillas de Django |
| Formularios | `forms.Form`, `forms.ModelForm` y `UserCreationForm` |
| Vistas genéricas | `DetailView`, `CreateView`, `UpdateView` y `DeleteView` |
| Autenticación | `django.contrib.auth` |
| Autorización | Permisos, grupos, decoradores y mixins |
| Sesiones | `django.contrib.sessions` |
| Administración | Django Admin |
| Pruebas | `TestCase` y `Client` de Django |
| Control de versiones | Git y GitHub |

Django utiliza `django.db.backends.mysql` para conectarse a MariaDB. El ORM permite consultar y modificar los registros mediante Python.

### Entorno utilizado

En la ejecución registrada del computador personal, el intérprete utilizado fue:

```text
C:\Python314\python.exe
```

Aunque la terminal mostraba el indicador `(.venv)`, la comprobación con `where python` y las ubicaciones de los paquetes indicaron que se estaba utilizando el intérprete global.

El proyecto y las pruebas funcionaron correctamente con ese entorno. Para reproducir la instalación en otro equipo, se puede preparar un entorno virtual local con las dependencias de `requirements.txt`.

## 3. Estructura del proyecto

Los principales archivos se organizan de la siguiente manera:

| Ubicación | Contenido |
|---|---|
| Raíz | `manage.py`, `requirements.txt`, `README.md`, `.gitignore`, `.env.example` y configuración local `.env`. |
| `config/` | `__init__.py`, `settings.py`, `urls.py`, `asgi.py` y `wsgi.py`. |
| `pages/` | `__init__.py`, `admin.py`, `apps.py`, `models.py`, `forms.py`, `views.py`, `urls.py` y `tests.py`. |
| `pages/migrations/` | `__init__.py`, `0001_initial.py` y `0002_alter_category_id_alter_resource_id.py`. |
| `pages/templates/pages/` | Plantillas de navegación, catálogo, autenticación, panel, revisión y CRUD. |

### Plantillas

| Plantilla | Responsabilidad |
|---|---|
| `base.html` | Estructura común, navegación y cierre de sesión. |
| `home.html` | Página de inicio. |
| `about.html` | Información sobre el proyecto. |
| `faq.html` | Preguntas frecuentes. |
| `resources.html` | Catálogo público y búsqueda por título. |
| `resource_detail.html` | Detalle de un recurso y enlaces según permisos. |
| `resource_form.html` | Formulario compartido por creación y edición. |
| `resource_confirm_delete.html` | Confirmación de eliminación. |
| `signup.html` | Registro de cuentas comunes. |
| `login.html` | Inicio de sesión. |
| `dashboard.html` | Panel privado y contador de visitas. |
| `dashboard_summary.html` | Total de recursos y total disponible. |
| `review.html` | Revisión del catálogo con permiso de lectura. |

### Responsabilidades principales

| Archivo | Responsabilidad |
|---|---|
| `config/settings.py` | Configuración de base de datos, aplicaciones, middleware, plantillas y autenticación. |
| `config/urls.py` | Conexión de Django Admin y las rutas de `pages`. |
| `pages/models.py` | Definición de categorías, recursos y su relación. |
| `pages/forms.py` | Campos editables y validación de `ResourceForm`. |
| `pages/views.py` | Páginas anteriores, búsqueda y vistas CRUD. |
| `pages/urls.py` | Rutas públicas, privadas y de gestión. |
| `pages/admin.py` | Administración de categorías y recursos. |
| `pages/tests.py` | Pruebas anteriores, CRUD, permisos, validación, CSRF y búsqueda. |
| `requirements.txt` | Dependencias utilizadas por el proyecto. |
| `.env.example` | Referencia para configurar la conexión local. |

## 4. Instalación y configuración

### Requisitos previos

- Python compatible con las dependencias del proyecto.
- MariaDB en ejecución.
- Git instalado.
- Acceso a la base existente y al usuario SQL de la aplicación.
- Una terminal ubicada en la carpeta que contiene `manage.py`.

### Clonar la rama del laboratorio

Para obtener una nueva copia del código:

```bat
git clone --branch laboratorio-9 https://github.com/juanlsk29/ClassroomHub.git laboratorio-09
cd laboratorio-09
```

Si ya se tiene el proyecto local, se utiliza esa carpeta sin clonarlo nuevamente.

### Preparar un entorno virtual

Para una instalación nueva:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

En PowerShell, la activación se realiza con:

```powershell
.\.venv\Scripts\Activate.ps1
```

Los entornos virtuales se crean en cada equipo; no se reutilizan copiando una carpeta de otro computador.

### Comprobar el intérprete y las dependencias

En CMD:

```bat
where python
python --version
python -m django --version
python -m pip show mysqlclient python-dotenv
```

Si se utiliza un entorno virtual, la primera ruta de `where python` debe corresponder al intérprete de ese entorno.

### Continuidad del proyecto

El Laboratorio 09 continúa el proyecto de los laboratorios anteriores.

No se ejecutan nuevamente:

```text
django-admin startproject
python manage.py startapp
```

Tampoco se sustituye MariaDB por SQLite ni se eliminan tablas para comenzar el CRUD.

## 5. Configuración de MariaDB

### Base existente

Se reutiliza la base que ya contiene el catálogo, las cuentas, los grupos y las sesiones de los laboratorios anteriores.

| Parámetro | Valor |
|---|---|
| Base de desarrollo | `classroom_hub` |
| Usuario SQL | `classroomhub_user` |
| Host | `127.0.0.1` |
| Puerto | `3307` |
| Motor | MariaDB 13.0.2 |
| Base de pruebas | `test_classroom_hub` |

No es necesario crear nuevamente la base ni el usuario SQL en el computador utilizado para esta entrega.

Clonar el repositorio descarga el código, pero no copia automáticamente los registros de MariaDB.

### Variables de entorno

El archivo `.env` conserva la configuración de conexión:

```dotenv
DB_NAME=classroom_hub
DB_USER=classroomhub_user
DB_PASSWORD=replace_with_a_private_password
DB_HOST=127.0.0.1
DB_PORT=3307
```

Esta es la configuración utilizada en el entorno escolar local. En otra instalación, los valores deben coincidir con su servidor y su usuario SQL.

La cuenta `classroomhub_user` conecta Django con MariaDB. Es independiente de las cuentas utilizadas para iniciar sesión en ClassroomHub.

### Comprobar la conexión

Ejecutar:

```bat
python manage.py shell
```

Dentro del shell:

```python
from django.db import connection

cursor = connection.cursor()
cursor.execute("SELECT DATABASE(), VERSION(), @@port")
print(cursor.fetchone())
cursor.close()
```

Resultado comprobado en el equipo:

```text
('classroom_hub', '13.0.2-MariaDB', 3307)
```

Para salir:

```python
exit()
```

### Permisos para las pruebas

El usuario SQL necesita acceso al esquema de pruebas. Si ese permiso no existe, una cuenta administradora de MariaDB puede concederlo con:

```sql
GRANT ALL PRIVILEGES ON test_classroom_hub.*
TO 'classroomhub_user'@'127.0.0.1';
```

La base de pruebas es descartable y permanece separada de la base de desarrollo.

## 6. Modelos y relaciones

El laboratorio reutiliza `Category` y `Resource` sin añadir nuevos modelos.

### Modelo `Category`

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Clave primaria | Identificador de la categoría. |
| `name` | `CharField(max_length=80, unique=True)` | Nombre único. |
| `description` | `TextField(blank=True)` | Descripción opcional. |

Las categorías se ordenan por nombre. Su representación mediante `__str__()` devuelve el nombre.

### Modelo `Resource`

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Clave primaria | Identificador del recurso. |
| `title` | `CharField(max_length=150)` | Título obligatorio. |
| `description` | `TextField(blank=True)` | Descripción opcional. |
| `available` | `BooleanField(default=True)` | Disponibilidad. |
| `category` | `ForeignKey` | Categoría asociada. |
| `created_at` | `DateTimeField(auto_now_add=True)` | Fecha automática de creación. |
| `resource_type` | `CharField(max_length=40, blank=True)` | Tipo de recurso opcional. |

Los recursos se ordenan por título. Su representación mediante `__str__()` devuelve el título.

### Relación entre los modelos

La relación es uno a muchos:

- Una categoría puede contener varios recursos.
- Cada recurso pertenece a una categoría.
- `related_name="resources"` permite consultar `category.resources.all()`.
- `on_delete=models.PROTECT` impide eliminar una categoría mientras tenga recursos asociados.
- Eliminar un recurso no elimina su categoría.

### Usuarios, grupos y sesiones

Se conserva el modelo de usuario de Django, accesible mediante `get_user_model()`.

Las aplicaciones de autenticación y sesiones administran sus propias tablas. No se añaden campos de usuario ni modelos de autenticación personalizados para implementar el CRUD.

## 7. Migraciones

### Estado de las migraciones de `pages`

```bat
python manage.py showmigrations pages
```

Resultado:

```text
pages
 [X] 0001_initial
 [X] 0002_alter_category_id_alter_resource_id
```

| Migración | Responsabilidad |
|---|---|
| `0001_initial` | Crea `Category` y `Resource`. En este proyecto ya incluye `resource_type`. |
| `0002_alter_category_id_alter_resource_id` | Actualiza los tipos de los identificadores de ambos modelos. |

### Comprobar cambios pendientes

```bat
python manage.py makemigrations --check --dry-run
```

Resultado:

```text
No changes detected
```

### Consultar operaciones pendientes

```bat
python manage.py migrate --plan
```

En la base utilizada no había operaciones pendientes.

El Laboratorio 09 añade formularios, vistas, rutas, plantillas y pruebas sobre modelos existentes. Por eso no requiere una migración nueva.

En otra instalación, las migraciones pendientes se revisan antes de ejecutar:

```bat
python manage.py migrate
```

## 8. Arquitectura MTV

### Model

`Category` y `Resource` representan los datos del catálogo y sus relaciones. El ORM permite consultar, crear, actualizar y eliminar registros persistidos en MariaDB.

### Template

Las plantillas generan la interfaz HTML.

`base.html` mantiene la navegación común. Los enlaces de gestión aparecen según los permisos del usuario:

- `Add resource` requiere `pages.add_resource`.
- `Edit resource` requiere `pages.change_resource`.
- `Delete resource` requiere `pages.delete_resource`.
- `Review` requiere `pages.view_resource`.

### View

Las vistas reciben las solicitudes, comprueban el acceso y generan las respuestas.

Se combinan vistas basadas en funciones y vistas genéricas basadas en clases:

| Vista | Tipo | Responsabilidad |
|---|---|---|
| `home` | Función | Página de inicio. |
| `resources` | Función | Catálogo y búsqueda. |
| `signup` | Función | Registro sin privilegios. |
| `dashboard` | Función | Panel y contador de visitas. |
| `dashboard_summary` | Función | Conteos privados del catálogo. |
| `resource_review` | Función | Revisión protegida. |
| `ResourceDetailView` | `DetailView` | Detalle público. |
| `ResourceCreateView` | `CreateView` | Creación con permiso. |
| `ResourceUpdateView` | `UpdateView` | Actualización con permiso. |
| `ResourceDeleteView` | `DeleteView` | Confirmación y eliminación con permiso. |

### Formularios

`ResourceForm` conecta los campos editables de `Resource` con los formularios HTML.

Las vistas de creación y edición reutilizan tanto el formulario como la plantilla, evitando duplicar reglas de validación.

## 9. Formularios, validación y procesamiento de solicitudes

### Diferencia entre GET y POST

| Método | Uso |
|---|---|
| GET | Consultar el catálogo, buscar, mostrar detalles y presentar formularios. |
| POST | Enviar datos para crear, editar o eliminar recursos. |

Una visita a una URL de eliminación no borra el recurso. La eliminación requiere el envío del formulario de confirmación.

### Formularios con y sin datos

- Un formulario sin datos asociados está sin vincular: `is_bound` es `False`.
- Un formulario construido con datos está vinculado: `is_bound` es `True`.
- `is_valid()` comprueba si los datos cumplen las reglas.
- Después de una validación correcta, `cleaned_data` contiene los valores normalizados.
- Los errores se consultan mediante `errors`.

Validar un formulario no guarda automáticamente el registro. El guardado ocurre cuando se ejecuta `save()`.

### Implementación de `ResourceForm`

```python
from django import forms

from .models import Resource


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = [
            "title",
            "description",
            "resource_type",
            "category",
            "available",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if len(title) < 3:
            raise forms.ValidationError(
                "Title must contain at least 3 characters."
            )

        return title
```

### Campos permitidos

| Campo | Editable |
|---|---|
| `title` | Sí |
| `description` | Sí |
| `resource_type` | Sí |
| `category` | Sí |
| `available` | Sí |
| `id` | No |
| `created_at` | No |

La lista explícita de campos evita exponer automáticamente campos internos al ampliar el modelo.

### Validaciones

- El título es obligatorio.
- El título admite como máximo 150 caracteres.
- El título debe contener al menos tres caracteres después de normalizar espacios exteriores.
- La categoría debe corresponder a un registro existente.
- El tipo de recurso admite como máximo 40 caracteres.
- `available` se procesa como un valor booleano.
- Los errores se muestran en el formulario sin guardar información inválida.

La longitud mínima del título se valida en `ResourceForm`. Una inserción directa mediante el ORM no ejecuta automáticamente `clean_title()`.

### Protección CSRF

Los formularios POST incluyen:

```html
{% csrf_token %}
```

Se conserva `CsrfViewMiddleware`. Las pruebas con `Client(enforce_csrf_checks=True)` comprueban el rechazo de solicitudes sin token.

### Post/Redirect/Get

Después de un guardado correcto:

1. El navegador envía POST.
2. Django comprueba permisos y valida el formulario.
3. Se guarda el registro.
4. La respuesta redirige a `pages:resources`.
5. El navegador solicita el catálogo mediante GET.

La recarga del catálogo no vuelve a enviar el formulario anterior.

## 10. Implementación del CRUD

### Consulta pública

`ResourceDetailView` presenta un recurso utilizando la PK de la URL.

```python
class ResourceDetailView(DetailView):
    model = Resource
    template_name = "pages/resource_detail.html"
    context_object_name = "resource"
```

Si el recurso no existe, devuelve HTTP 404.

Los títulos del catálogo enlazan al detalle mediante nombres de rutas y `resource.pk`.

### Creación

```python
class ResourceCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView,
):
    model = Resource
    form_class = ResourceForm
    template_name = "pages/resource_form.html"
    permission_required = "pages.add_resource"
    success_url = reverse_lazy("pages:resources")
```

La creación exige autenticación y `pages.add_resource`.

Un formulario válido crea un registro y redirige al catálogo. Uno inválido vuelve a mostrarse con errores.

### Actualización

```python
class ResourceUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView,
):
    model = Resource
    form_class = ResourceForm
    template_name = "pages/resource_form.html"
    permission_required = "pages.change_resource"
    success_url = reverse_lazy("pages:resources")
```

`UpdateView` obtiene el recurso existente y presenta sus datos.

El guardado modifica esa misma fila:

- Conserva la PK.
- No crea un duplicado.
- Permite cambiar título, descripción, tipo, categoría y disponibilidad.
- Si la validación falla, conserva los valores anteriores en la base.

### Eliminación

```python
class ResourceDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView,
):
    model = Resource
    template_name = "pages/resource_confirm_delete.html"
    permission_required = "pages.delete_resource"
    success_url = reverse_lazy("pages:resources")
```

El flujo de la interfaz es:

1. GET presenta el recurso y solicita confirmación.
2. `Cancel` regresa al detalle sin modificar datos.
3. `Confirm deletion` envía POST con CSRF.
4. La vista comprueba autorización y elimina el recurso.
5. Se redirige al catálogo.

La eliminación conserva la categoría y los demás recursos.

## 11. Autenticación, grupos y permisos

### Conceptos

| Concepto | Aplicación |
|---|---|
| Identificación | El usuario indica el nombre de su cuenta. |
| Autenticación | Django comprueba las credenciales y establece la sesión. |
| Autorización | Django comprueba si la cuenta puede ejecutar una operación. |

Iniciar sesión no concede automáticamente permisos para modificar recursos.

### Permisos por operación

| Operación | Permiso |
|---|---|
| Revisión del catálogo | `pages.view_resource` |
| Creación | `pages.add_resource` |
| Edición | `pages.change_resource` |
| Eliminación | `pages.delete_resource` |

### Grupos

| Grupo | Permisos sobre `Resource` |
|---|---|
| `Catalog reviewers` | `view_resource` |
| `Catalog editors` | `view_resource`, `add_resource`, `change_resource`, `delete_resource` |

El permiso de creación no concede por sí solo autorización para editar o eliminar.

### Matriz de acceso

| Operación | Visitante | Cuenta común | Revisor | Editor |
|---|---|---|---|---|
| Consultar lista | Sí | Sí | Sí | Sí |
| Consultar detalle | Sí | Sí | Sí | Sí |
| Buscar por título | Sí | Sí | Sí | Sí |
| Entrar al panel | No | Sí | Sí | Sí |
| Consultar resumen privado | No | Sí | Sí | Sí |
| Abrir revisión | No | No | Sí | Sí |
| Crear recursos | No | No | No | Sí |
| Editar recursos | No | No | No | Sí |
| Eliminar recursos | No | No | No | Sí |

### Comportamiento de las vistas protegidas

- Visitante anónimo: redirección al login.
- Cuenta autenticada sin permiso: HTTP 403.
- Cuenta autorizada: acceso a la operación.
- Cuenta autorizada que solicita un recurso inexistente: HTTP 404.

`LoginRequiredMixin` se coloca antes de `PermissionRequiredMixin`.

### Cuentas reutilizadas

| Cuenta | Función |
|---|---|
| `pc` | Administración mediante Django Admin; cuenta staff y superusuaria. |
| `Juan` | Editor mediante `Catalog editors`, sin staff ni superusuario. |
| `reader_demo` | Revisor mediante `Catalog reviewers`, sin privilegios de edición. |

Se reutilizaron las cuentas existentes. No fue necesario crear cuentas permanentes adicionales para completar el laboratorio.

### Registro público

El registro conserva `UserCreationForm` y crea cuentas comunes.

No permite asignar:

- Grupos privilegiados.
- Permisos de gestión.
- Estado de staff.
- Estado de superusuario.

Los grupos y permisos se asignan administrativamente.

### Visibilidad de enlaces

Ocultar enlaces mejora la interfaz, pero no constituye la protección principal.

Las vistas comprueban permisos aunque una persona escriba directamente la URL o envíe un POST manual.

## 12. Rutas principales

| Método | Ruta | Acceso y función |
|---|---|---|
| GET | `/` | Inicio público. |
| GET | `/resources/` | Catálogo público. |
| GET | `/resources/?q=texto` | Búsqueda pública. |
| GET | `/resources/<pk>/` | Detalle público. |
| GET | `/resources/new/` | Formulario de creación con `add_resource`. |
| POST | `/resources/new/` | Guardar un recurso con `add_resource` y CSRF. |
| GET | `/resources/<pk>/edit/` | Formulario de edición con `change_resource`. |
| POST | `/resources/<pk>/edit/` | Guardar cambios con `change_resource` y CSRF. |
| GET | `/resources/<pk>/delete/` | Confirmación con `delete_resource`. |
| POST | `/resources/<pk>/delete/` | Eliminar con `delete_resource` y CSRF. |
| GET | `/resources/review/` | Revisión con `view_resource`. |
| GET | `/about/` | Información del proyecto. |
| GET | `/faq/` | Preguntas frecuentes. |
| GET, POST | `/accounts/signup/` | Registro de cuentas comunes. |
| GET, POST | `/accounts/login/` | Inicio de sesión. |
| POST | `/accounts/logout/` | Cierre de sesión con CSRF. |
| GET | `/dashboard/` | Panel privado y contador de visitas. |
| GET | `/dashboard/summary/` | Conteos privados del catálogo. |
| Según operación | `/admin/` | Administración para personal autorizado. |

`<pk>` representa el identificador real del recurso.

### Nombres de rutas del CRUD

| Nombre | Ruta |
|---|---|
| `pages:resources` | `/resources/` |
| `pages:resource-detail` | `/resources/<pk>/` |
| `pages:resource-create` | `/resources/new/` |
| `pages:resource-update` | `/resources/<pk>/edit/` |
| `pages:resource-delete` | `/resources/<pk>/delete/` |

Las redirecciones de las vistas genéricas utilizan `reverse_lazy("pages:resources")`.

## 13. Django Admin y configuración de grupos

### Crear categorías

1. Iniciar sesión en `/admin/` con la cuenta administradora existente.
2. Abrir **Categories**.
3. Seleccionar **Add**.
4. Introducir un nombre único.
5. Añadir una descripción opcional.
6. Guardar.

Las categorías quedan disponibles en los formularios de recursos.

### Configurar revisores

1. Abrir **Groups**.
2. Crear o seleccionar `Catalog reviewers`.
3. Asignar únicamente **Can view resource** de la aplicación `pages`.
4. Guardar.
5. Abrir **Users** y seleccionar la cuenta revisora.
6. Añadirla al grupo.
7. Mantener desactivados **Staff status** y **Superuser status**.
8. Guardar.

### Configurar editores

1. Abrir **Groups**.
2. Crear o seleccionar `Catalog editors`.
3. Asignar los permisos de `Resource`:
   - **Can view resource**.
   - **Can add resource**.
   - **Can change resource**.
   - **Can delete resource**.
4. Guardar.
5. Abrir **Users** y seleccionar una cuenta existente.
6. Añadirla al grupo.
7. Mantener desactivados **Staff status** y **Superuser status**.
8. Guardar.

Las cuentas editoras pueden utilizar el CRUD público sin acceder a Django Admin.

Los grupos y sus asignaciones residen en MariaDB. En otra base deben configurarse administrativamente.

## 14. Consultas mediante el ORM

### Consultar recursos y categorías

Desde:

```bat
python manage.py shell
```

Ejecutar:

```python
from pages.models import Category, Resource

resources = Resource.objects.select_related("category").all()
available_resources = Resource.objects.filter(available=True)

print(list(resources.values("id", "title", "category__name")))
print("Disponibles:", available_resources.count())

category = Category.objects.first()

if category is not None:
    print(category.name)
    print(list(category.resources.values("id", "title")))
```

El catálogo y la revisión utilizan `select_related("category")` para consultar también la información relacionada de la categoría.

### Comprobar una actualización

```python
from pages.models import Resource

resource_id = int(input("ID del recurso: "))
resource = Resource.objects.get(pk=resource_id)

print(
    resource.pk,
    resource.title,
    resource.description,
    resource.category.name,
    resource.resource_type,
    resource.available,
)
```

Se compara la PK antes y después de editar. Debe permanecer igual.

### Consultar grupos y permisos

```python
from django.contrib.auth import get_user_model

User = get_user_model()
account = User.objects.get(username="Juan")

print(account.is_staff)
print(account.is_superuser)
print(list(account.groups.values_list("name", flat=True)))

print(account.has_perm("pages.view_resource"))
print(account.has_perm("pages.add_resource"))
print(account.has_perm("pages.change_resource"))
print(account.has_perm("pages.delete_resource"))
```

La cuenta editora conserva `False` para staff y superusuario, pero dispone de los cuatro permisos mediante su grupo.

### Resumen privado

```python
total_resources = Resource.objects.count()
available_resources = Resource.objects.filter(available=True).count()
```

Estos conteos se muestran en `/dashboard/summary/`, que requiere autenticación.

## 15. Reto adicional: búsqueda pública

Se implementó una búsqueda sencilla por título utilizando GET.

### Implementación

```python
def resources(request):
    query = request.GET.get("q", "").strip()

    resources_list = Resource.objects.select_related("category").all()

    if query:
        resources_list = resources_list.filter(title__icontains=query)

    context = {
        "resources": resources_list,
        "query": query,
    }

    return render(request, "pages/resources.html", context)
```

### Comportamiento

| Caso | Resultado |
|---|---|
| Término con coincidencias | Se muestran los recursos coincidentes. |
| Término sin coincidencias | Se muestra un mensaje de resultado vacío. |
| Término vacío | Se muestra todo el catálogo. |
| Término con espacios exteriores | Se normaliza antes de buscar. |
| Opción `Clear search` | Regresa al catálogo sin filtro. |

Ejemplo:

```text
http://127.0.0.1:8000/resources/?q=Quijote
```

La búsqueda permanece pública y no modifica registros.

## 16. Pruebas automatizadas

Las pruebas se encuentran en `pages/tests.py`.

Se conservaron las 30 pruebas anteriores y se añadieron 37 pruebas para el laboratorio actual.

### Distribución

| Bloque | Cantidad | Cobertura |
|---|---:|---|
| Pruebas anteriores | 30 | Catálogo, modelos, autenticación, sesiones, revisión y resumen privado. |
| CRUD de la actividad | 30 | Detalle, creación, edición, eliminación, permisos, validación y CSRF. |
| Comprobaciones adicionales | 4 | Restricciones de revisores, CSRF de eliminación, permisos independientes y categoría inválida al editar. |
| Búsqueda | 3 | Resultados, ausencia de resultados y término vacío. |
| **Total** | **67** | **Funcionalidades anteriores y CRUD completo con búsqueda.** |

La clase `ResourceCrudTests` contiene 34 pruebas: las 30 del bloque CRUD y cuatro adicionales.

`ResourceSearchTests` contiene tres pruebas.

El enunciado menciona 27 pruebas CRUD, pero el código proporcionado en la actividad contiene 30. El total de esta implementación considera los métodos realmente incluidos y conserva las dos pruebas adicionales del resumen privado del laboratorio anterior.

### Casos cubiertos

| Funcionalidad | Comprobaciones |
|---|---|
| Detalle | Acceso público, datos del recurso, categoría y respuesta 404. |
| Catálogo | Enlaces al detalle y aparición de registros nuevos. |
| Creación | Acceso autorizado, redirección, persistencia y aumento del conteo. |
| Validación | Título corto, categoría inexistente y lista explícita de campos. |
| Actualización | Formulario existente, cambios persistidos, misma PK y ausencia de duplicados. |
| Edición inválida | Conservación de título, descripción, categoría y disponibilidad anteriores. |
| Eliminación | GET no elimina; POST autorizado elimina solo el recurso elegido. |
| Relaciones | La categoría y otros recursos sobreviven a la eliminación. |
| Autenticación | Visitantes enviados al login. |
| Autorización | Cuentas comunes y revisores rechazados según operación. |
| Independencia de permisos | Poder crear no implica poder editar o eliminar. |
| CSRF | Rechazo de creación y eliminación sin token cuando se exige su comprobación. |
| Editor | Gestión sin staff ni superusuario y acceso a revisión. |
| Búsqueda | Coincidencias, resultado vacío, término vacío y ausencia de modificaciones. |

### Ejecutar las pruebas

```bat
python manage.py test pages
```

Para ver cada caso:

```bat
python manage.py test pages --verbosity 2
```

### Base de pruebas

Django utiliza `test_classroom_hub`, separada de `classroom_hub`.

Durante la ejecución:

1. Se prepara la base de pruebas.
2. Se aplican las migraciones.
3. Se crean datos ficticios para los casos.
4. Se ejecutan las comprobaciones.
5. Se elimina la base de pruebas al terminar una ejecución normal.

Las cuentas `crud_reader`, `crud_editor` y `crud_reviewer` pertenecen a las pruebas. No se crean como cuentas permanentes en la base de desarrollo.

### Resultado final

**67 pruebas aprobadas y 0 fallos.**

Se conservaron las funcionalidades de los laboratorios anteriores y se verificó el comportamiento del CRUD y la búsqueda.

## 17. Comprobaciones manuales

| Caso | Acción | Resultado verificado |
|---|---|---|
| P01 | Abrir el catálogo sin sesión. | Catálogo público visible. |
| P02 | Abrir un detalle existente. | Datos del recurso y su categoría. |
| P03 | Abrir un detalle inexistente. | HTTP 404. |
| P04 | Abrir creación sin sesión. | Redirección al login. |
| P05 | Abrir creación como cuenta común. | HTTP 403. |
| P06 | Abrir creación como revisor. | HTTP 403. |
| P07 | Crear como editor. | Guardado y redirección al catálogo. |
| P08 | Enviar un título de dos caracteres. | Error sin guardado. |
| P09 | Validar una categoría inexistente. | Error de categoría. |
| P10 | Abrir edición como cuenta común. | HTTP 403. |
| P11 | Editar como editor. | Cambios guardados sobre la misma PK. |
| P12 | Enviar una edición inválida. | Valores anteriores conservados. |
| P13 | Abrir confirmación de eliminación. | El recurso continúa existiendo. |
| P14 | Abrir eliminación sin permiso. | HTTP 403. |
| P15 | Confirmar eliminación como editor. | Solo desaparece el recurso elegido. |
| P16 | Abrir el detalle del recurso eliminado. | HTTP 404. |
| P17 | Consultar el catálogo tras cada operación. | Datos actualizados. |
| P18 | Reiniciar Django. | Persistencia de cambios y eliminaciones. |
| P19 | Abrir revisión como `reader_demo`. | Lectura autorizada. |
| P20 | Ejecutar las pruebas. | Base aislada y suite aprobada. |
| P21 | Buscar un título existente. | Coincidencias visibles. |
| P22 | Buscar un título inexistente. | Mensaje sin coincidencias. |
| P23 | Buscar con término vacío. | Catálogo completo. |

### Recursos de práctica

Se utilizaron recursos de prueba para comprobar edición y eliminación, conservando los registros históricos como `Quijote`.

La eliminación se comprobó con un recurso temporal. Se verificó que cancelar no lo borraba y que confirmar no afectaba su categoría ni otros registros.

### Ejercicio de permiso inexistente

Se cambió temporalmente el permiso de `ResourceUpdateView` por uno inexistente y se comprobó el rechazo con una cuenta no superusuaria.

Después se restauró:

```python
permission_required = "pages.change_resource"
```

### Cuenta común sin crear otro usuario

Para comprobar el comportamiento de una cuenta común se retiró temporalmente `Catalog editors` de `Juan`.

Al finalizar se restauró su pertenencia al grupo. `reader_demo` conservó su función de revisor.

## 18. Ejecución del proyecto

En el computador utilizado:

```bat
cd /d C:\Users\PC\Desktop\laboratorio-09
python manage.py check
python manage.py runserver
```

En una instalación con entorno virtual local, se activa antes de ejecutar los comandos.

Abrir:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Para detener el servidor:

```text
Ctrl + C
```

### Flujo de uso como editor

1. Iniciar sesión con la cuenta editora.
2. Abrir **Resources**.
3. Pulsar **Add resource**.
4. Completar los campos y guardar.
5. Abrir el detalle desde el título.
6. Seleccionar **Edit resource** para modificarlo.
7. Guardar y verificar los cambios.
8. Seleccionar **Delete resource** para abrir la confirmación.
9. Cancelar o confirmar la eliminación.
10. Cerrar sesión mediante **Log out**.

### Flujo de uso como visitante

1. Abrir el catálogo.
2. Consultar un detalle.
3. Buscar por título.
4. Limpiar el filtro.
5. Comprobar que las operaciones de gestión requieren autenticación.

## 19. Dificultades encontradas y soluciones

### Identificación del entorno de ejecución

El indicador de la terminal sugería un entorno virtual activo, pero `where python` y las ubicaciones de los paquetes mostraron el intérprete global.

Se comprobó qué Python ejecutaba realmente el proyecto y se continuó con el entorno compatible que superó las pruebas.

### Conservación de la base histórica

Se verificaron el nombre de la base, la versión del motor y el puerto antes de modificar el proyecto.

Esto permitió reutilizar recursos, categorías y usuarios sin recrear tablas.

### Diferencia entre las migraciones del ejemplo y el proyecto

El enunciado describe la incorporación de `resource_type` en una etapa anterior. En esta copia, el campo ya existe en `0001_initial`.

Se conservó el historial real y no se generó una migración redundante.

### Integración de funcionalidades anteriores

Los ejemplos generales no incluían todas las extensiones del proyecto, como FAQ y resumen privado.

Se conservaron sus vistas, rutas, plantillas y pruebas al integrar el CRUD.

### Errores al pegar bloques en el shell

Durante un ejercicio apareció un error de sintaxis por no finalizar correctamente una definición de clase antes de ejecutar otras instrucciones.

Se separaron los bloques y se cerró la definición con una línea vacía.

### Interpretación de respuestas 403

Las solicitudes de cuentas sin permisos generaron respuestas 403 y mensajes de `PermissionDenied`.

Se comprobó que eran el comportamiento esperado de autorización, no errores que debieran resolverse retirando los permisos.

### Enlaces a operaciones todavía no implementadas

En el primer avance se omitieron temporalmente los enlaces de edición y eliminación.

Se añadieron cuando sus rutas y vistas estuvieron disponibles, evitando errores `NoReverseMatch`.

### Visualización de diferencias en Git

El comando de diferencias abrió el paginador de Git.

Para consultar la salida directamente en la terminal se utilizó:

```bat
git --no-pager diff --cached --stat
```

## 20. Respuestas a las preguntas del laboratorio

### 1. ¿Qué diferencia existe entre un Form y un ModelForm?

`Form` permite definir campos y validaciones de forma independiente. Si sus datos deben guardarse en un modelo, esa lógica se implementa manualmente.

`ModelForm` obtiene los campos y parte de las validaciones desde el modelo y ofrece `save()` para crear o actualizar una instancia.

### 2. ¿Por qué conviene declarar explícitamente Meta.fields?

Porque establece qué campos puede modificar una persona y evita que un campo interno añadido posteriormente quede expuesto automáticamente.

### 3. ¿Qué ocurre cuando ResourceForm.is_valid() devuelve False?

El formulario contiene errores. Se presenta nuevamente para corregirlos y no se guarda el recurso.

### 4. ¿Qué ventajas aporta CreateView?

Gestiona el formulario inicial, el procesamiento de POST, la validación, el guardado y la redirección, reduciendo código repetido.

### 5. ¿Por qué UpdateView necesita recuperar el objeto existente?

Porque debe aplicar los cambios sobre una fila concreta, conservar su identificador y presentar sus valores iniciales.

### 6. ¿Por qué DeleteView muestra una confirmación por GET y elimina por POST?

GET permite consultar y cancelar sin modificar datos. POST representa la acción de eliminación y permite aplicar las comprobaciones de autorización y CSRF.

### 7. ¿Qué ventaja aporta reverse_lazy()?

Retrasa la resolución de la URL hasta que se necesita, por lo que puede utilizarse en atributos de clase sin resolver las rutas durante la importación.

### 8. ¿Por qué una cuenta autenticada no puede editar sin pages.change_resource?

La autenticación identifica la cuenta. La autorización determina qué operaciones tiene permitidas. Son comprobaciones distintas.

### 9. ¿Qué diferencia hay entre Catalog reviewers y Catalog editors?

`Catalog reviewers` tiene permiso de lectura del recurso. `Catalog editors` incorpora permisos para consultar, crear, actualizar y eliminar.

### 10. ¿Por qué los enlaces condicionales no sustituyen los permisos de la vista?

Porque una persona puede escribir una dirección o enviar una solicitud directamente. La vista debe rechazar la operación aunque no se haya utilizado un enlace de la interfaz.

### 11. ¿Qué sucede cuando el ID de un recurso no existe?

El detalle devuelve 404. En las operaciones protegidas, primero se verifica el acceso; si la cuenta está autorizada y el recurso no existe, se devuelve 404.

### 12. ¿Cómo se comprueba que una actualización conserva la PK?

Se compara el identificador antes y después de guardar y se verifica que la cantidad de recursos no aumentó.

### 13. ¿Por qué la base de pruebas no puede contener datos importantes?

Porque el ejecutor puede crearla y eliminarla. Debe ser independiente de la base de desarrollo y contener únicamente datos de prueba.

### 14. ¿Qué limitaciones quedan antes de exponer un CRUD real en Internet?

Se necesita preparar el despliegue: desactivar DEBUG, configurar hosts, HTTPS, secretos, cookies, servidor de aplicación, respaldo de datos, registros operativos y revisión de reglas de acceso.

El servidor `runserver` se utiliza para desarrollo.

## 21. Funcionalidades implementadas

### Catálogo y persistencia

- Conexión a MariaDB.
- Modelos `Category` y `Resource`.
- Relación protegida entre categorías y recursos.
- Lista pública con información relacionada.
- Detalle público por PK.
- Búsqueda pública por título.
- Persistencia después de reiniciar Django.

### Autenticación y sesiones

- Registro con `UserCreationForm`.
- Login con `LoginView`.
- Logout mediante POST.
- Panel privado.
- Contador de visitas.
- Resumen privado.
- Revisión según permiso.

### Gestión de recursos

- Formulario con campos explícitos.
- Validación de título.
- Creación con permiso.
- Edición con permiso y conservación de PK.
- Confirmación de eliminación.
- Eliminación autorizada mediante POST en la interfaz.
- Plantilla compartida para crear y editar.
- Enlaces condicionados por permisos.

### Verificación

- Conservación de las 30 pruebas anteriores.
- Pruebas CRUD y permisos.
- Pruebas CSRF.
- Pruebas de búsqueda.
- Comprobación de permisos independientes.
- Comprobación de datos intactos después de rechazos.
- Total de 67 pruebas aprobadas.

## 22. Alcance y posibles mejoras

El laboratorio implementa un CRUD de recursos sobre los modelos existentes y conserva el sistema de usuarios de Django.

Las categorías continúan gestionándose desde Django Admin.

Quedan fuera del alcance de esta entrega:

- CRUD público de categorías.
- Carga de archivos.
- API REST.
- Interfaces JavaScript avanzadas.
- Paginación.
- Filtros avanzados.
- Papelera y restauración de recursos.
- Recuperación de contraseñas por correo.
- Autenticación multifactor.
- Despliegue en producción.

La búsqueda sencilla por título sí se implementó como reto adicional.

## 23. Verificación final del Laboratorio 09

### Configuración

```bat
python manage.py check
```

Resultado:

```text
System check identified no issues (0 silenced).
```

### Sin cambios pendientes en los modelos

```bat
python manage.py makemigrations --check --dry-run
```

Resultado:

```text
No changes detected
```

### Pruebas

```bat
python manage.py test pages --verbosity 2
```

Resultado final confirmado:

| Comprobación | Resultado |
|---|---|
| Total de pruebas | 67 |
| Pruebas aprobadas | 67 |
| Fallos | 0 |
| Base de pruebas | `test_classroom_hub` |
| Base de desarrollo | `classroom_hub`, separada de las pruebas |

### Roles finales

- `pc` conserva su función administradora.
- `Juan` pertenece a `Catalog editors`.
- `Juan` no es staff ni superusuario.
- `reader_demo` pertenece a `Catalog reviewers`.
- El registro público no asigna privilegios.
- `ResourceUpdateView` utiliza `pages.change_resource`.

### Persistencia

Los registros creados y modificados permanecen después de reiniciar Django. Los recursos eliminados no reaparecen.

## 24. Estrategia de control de versiones

El desarrollo del Laboratorio 09 se organiza en dos commits sobre la rama `laboratorio-9`.

| Etapa | Commit o mensaje | Contenido |
|---|---|---|
| Primera parte | `70cd77d` — `feat: agregar formulario, detalle publico y creacion de recursos con permisos` | ModelForm, validación, detalle público, creación protegida, navegación y documentación inicial. |
| Segunda parte | `feat: completar CRUD, busqueda y pruebas del laboratorio 9` | Edición, eliminación, búsqueda, pruebas completas y documentación final. |

La publicación del primer commit fue comprobada en `origin/laboratorio-9`.

El segundo avance reúne la implementación final validada. Su identificador se consulta en el historial de Git una vez creado.

### Consultar rama, estado e historial

```bat
git branch --show-current
git status
git --no-pager log -2 --oneline
```

### Publicar avances

```bat
git push origin laboratorio-9
```

La entrega se desarrolla en `laboratorio-9`, conservando las ramas de los laboratorios anteriores.

Los grupos, sus asignaciones y los registros del catálogo se almacenan en MariaDB; no forman parte automáticamente del contenido de un commit.

## 25. Conclusiones

El Laboratorio 09 amplió ClassroomHub desde un catálogo con autenticación y revisión hasta una aplicación con gestión de recursos desde su propia interfaz.

`ModelForm` permitió reutilizar la definición del modelo y centralizar las validaciones. Las vistas genéricas simplificaron la consulta, creación, actualización y eliminación, mientras los permisos separaron la autenticación de la autorización por operación.

La actualización conserva el identificador del recurso. La eliminación diferencia la consulta de la confirmación y el envío que modifica la base. Los formularios inválidos y las solicitudes no autorizadas no alteran los registros.

Las 67 pruebas aprobadas verifican tanto las funcionalidades nuevas como la continuidad del catálogo, las sesiones, la revisión y el resumen privado. La búsqueda opcional completa una interfaz pública de consulta sin modificar el alcance de los permisos de gestión.

## 26. Estado final

| Componente | Estado |
|---|---|
| Catálogo persistente | Conservado y ampliado. |
| Base de datos | MariaDB existente reutilizada. |
| Modelos y migraciones | Conservados, sin cambios pendientes. |
| Autenticación | Registro, login y logout operativos. |
| Sesiones | Panel y contador conservados. |
| Revisión | Protegida mediante `pages.view_resource`. |
| Formulario | Campos explícitos y validación del título. |
| Detalle | Público, con respuesta 404 cuando corresponde. |
| Creación | Protegida mediante `pages.add_resource`. |
| Edición | Protegida mediante `pages.change_resource`, sin duplicados. |
| Eliminación | Confirmación y POST protegido mediante permiso y CSRF. |
| Categorías | Administradas desde Django Admin. |
| Búsqueda | Pública, por título y de solo lectura. |
| Usuarios | Cuentas existentes reutilizadas. |
| Pruebas | 67 aprobadas y 0 fallos. |
| Documentación | Instalación, configuración, rutas, permisos, pruebas y decisiones incluidas. |
| Rama de entrega | `laboratorio-9`. |