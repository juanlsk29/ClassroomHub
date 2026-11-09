# ClassroomHub

**Laboratorio 08 — Autenticación, sesiones y control de acceso**  
**Repositorio:** [ClassroomHub](https://github.com/juanlsk29/ClassroomHub)  
**Rama de entrega:** [`laboratorio-8`](https://github.com/juanlsk29/ClassroomHub/tree/laboratorio-8)

## 1. Descripción del proyecto

ClassroomHub es una aplicación web educativa desarrollada con Django que permite consultar recursos de programación y desarrollo de software. El proyecto se ha ampliado en tres etapas.

| Laboratorio | Avance |
|---|---|
| 06 | Creación de rutas, vistas y plantillas HTML, con navegación entre páginas. |
| 07 | Integración de MariaDB, modelos `Category` y `Resource`, migraciones, consultas mediante el ORM y administración de datos con Django Admin. |
| 08 | Registro de usuarios, inicio y cierre de sesión, panel privado, revisión del catálogo mediante permisos y resumen privado de recursos. |

El Laboratorio 08 distingue tres tipos de acceso. Cualquier visitante puede consultar el catálogo general. Una cuenta autenticada puede entrar al panel y al resumen privado. Una cuenta con el permiso `pages.view_resource` puede consultar además la página de revisión.

## 2. Tecnologías y versiones

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.14.5 |
| Framework | Django 6.1.3, versión documentada en el Laboratorio 07 |
| Motor de base de datos | MariaDB 13.0.2, instalación documentada en el Laboratorio 07 |
| Interfaz | HTML, CSS y plantillas de Django |
| Entorno virtual | `venv` |
| Controlador SQL | `mysqlclient` |
| Variables de entorno | `python-dotenv` |
| Administración | Django Admin |
| Autenticación y autorización | `django.contrib.auth` |
| Sesiones | `django.contrib.sessions` |
| Pruebas automatizadas | `TestCase` y `Client` de Django |
| Control de versiones | Git y GitHub |

Django utiliza `django.db.backends.mysql` para conectarse a MariaDB. El ORM permite consultar los modelos mediante código Python y delega en Django la generación de las consultas SQL.

## 3. Estructura del proyecto

```text
laboratorio-08/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── pages/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_alter_category_id_alter_resource_id.py
│   ├── templates/
│   │   └── pages/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── resources.html
│   │       ├── about.html
│   │       ├── faq.html
│   │       ├── signup.html
│   │       ├── login.html
│   │       ├── dashboard.html
│   │       ├── dashboard_summary.html
│   │       └── review.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

El archivo `.env` y la carpeta `.venv` se preparan en cada equipo y se excluyen de Git.

### Responsabilidades principales

| Archivo o directorio | Responsabilidad |
|---|---|
| `config/settings.py` | Configura la base de datos, las aplicaciones instaladas, el middleware y los destinos de autenticación. |
| `config/urls.py` | Conecta Django Admin y las rutas de la aplicación `pages`. |
| `pages/models.py` | Define las categorías, los recursos y la relación entre ambos. |
| `pages/views.py` | Atiende las solicitudes del catálogo, el registro, el panel, el resumen y la revisión. |
| `pages/urls.py` | Define las rutas públicas y privadas y conecta `LoginView` y `LogoutView`. |
| `pages/admin.py` | Configura la administración de categorías y recursos. |
| `pages/templates/pages/` | Contiene las plantillas HTML y la navegación compartida. |
| `pages/migrations/` | Conserva el historial de cambios de los modelos de la aplicación. |
| `pages/tests.py` | Contiene las pruebas del catálogo, autenticación, sesiones, permisos y resumen privado. |
| `requirements.txt` | Registra las dependencias necesarias para instalar el proyecto. |
| `.env.example` | Sirve como referencia para crear la configuración local. |

## 4. Instalación y configuración

### Requisitos previos

- Una instalación de Python compatible con las dependencias del proyecto.
- MariaDB o MySQL en ejecución.
- Git y una terminal de comandos.
- Acceso para configurar una base de desarrollo y una cuenta SQL local.

### Clonar la rama del laboratorio

```bat
git clone --branch laboratorio-8 https://github.com/juanlsk29/ClassroomHub.git laboratorio-08
cd laboratorio-08
```

### Crear y activar el entorno virtual

En Windows CMD:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

En PowerShell, el comando de activación es:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar las dependencias

Con el entorno virtual activo:

```bat
python -m pip install -r requirements.txt
python -m django --version
```

Si ya existe un entorno virtual funcional en la carpeta del proyecto, basta con activarlo e instalar las dependencias que falten.

## 5. Configuración de MariaDB

### Crear la base de desarrollo

Desde una cuenta administradora del motor de base de datos:

```sql
CREATE DATABASE IF NOT EXISTS classroom_hub
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

### Crear la cuenta SQL de la aplicación

Si ya existe el usuario del Laboratorio 07, se puede reutilizar. Para una instalación nueva:

```sql
CREATE USER 'classroomhub_user'@'127.0.0.1'
IDENTIFIED BY 'CONTRASENA_PRIVADA';

GRANT ALL PRIVILEGES ON classroom_hub.*
TO 'classroomhub_user'@'127.0.0.1';

GRANT ALL PRIVILEGES ON test_classroom_hub.*
TO 'classroomhub_user'@'127.0.0.1';
```

Reemplaza `CONTRASENA_PRIVADA` por una clave local. Los permisos se limitan a los esquemas de desarrollo y pruebas. El ejecutor de Django crea y elimina el esquema de pruebas durante una ejecución normal.

### Configurar las variables de entorno

En CMD, si todavía no existe `.env`:

```bat
copy .env.example .env
```

Ejemplo de configuración local:

```env
DB_NAME=classroom_hub
DB_USER=classroomhub_user
DB_PASSWORD=CONTRASENA_PRIVADA
DB_HOST=127.0.0.1
DB_PORT=3307
```

El puerto `3307` corresponde a la instalación independiente de MariaDB documentada en el Laboratorio 07. Ajusta el valor si el servidor de tu equipo escucha en otro puerto.

La cuenta `classroomhub_user` conecta Django con MariaDB. Las cuentas de ClassroomHub se crean mediante el formulario **Sign up** y se administran con el sistema de usuarios de Django. Guarda las credenciales reales solo en la configuración local y conserva `.env` en `.gitignore`.

## 6. Modelos y relaciones

### Modelo `Category`

Representa las categorías del catálogo.

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Clave primaria | Identificador de la categoría. |
| `name` | `CharField` | Nombre único de la categoría. |
| `description` | `TextField` | Descripción opcional. |

Las categorías se ordenan alfabéticamente por nombre.

### Modelo `Resource`

Representa un recurso educativo almacenado en el catálogo.

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Clave primaria | Identificador del recurso. |
| `title` | `CharField` | Título del recurso. |
| `description` | `TextField` | Descripción opcional. |
| `available` | `BooleanField` | Indica si el recurso está disponible. |
| `category` | `ForeignKey` | Categoría a la que pertenece el recurso. |
| `created_at` | `DateTimeField` | Fecha de creación. |
| `resource_type` | `CharField` | Tipo de recurso, de diligenciamiento opcional. |

### Relación entre los modelos

`Category` y `Resource` tienen una relación **uno a muchos**. Una categoría puede contener varios recursos y cada recurso pertenece a una categoría. La clave foránea utiliza `on_delete=models.PROTECT` para impedir que se elimine una categoría con recursos asociados. `related_name="resources"` permite acceder a ellos mediante `category.resources`.

### Usuarios, grupos y sesiones

El Laboratorio 08 usa el modelo estándar de Django, accesible mediante `get_user_model()`. Las aplicaciones `auth`, `contenttypes` y `sessions` administran las tablas de usuarios, grupos, permisos y sesiones. La relación entre cuentas y grupos permite conceder el permiso de revisión sin modificar los modelos del catálogo.

## 7. Migraciones de la base de datos

### Aplicar las migraciones

```bat
python manage.py migrate
```

### Consultar su estado

```bat
python manage.py showmigrations auth contenttypes sessions pages
```

En la comprobación del Laboratorio 08, todas las migraciones consultadas aparecieron con `[X]`.

| Aplicación | Migraciones aplicadas |
|---|---|
| `auth` | De `0001_initial` a `0012_alter_user_first_name_max_length`. |
| `contenttypes` | `0001_initial` y `0002_remove_content_type_name`. |
| `sessions` | `0001_initial`. |
| `pages` | `0001_initial` y `0002_alter_category_id_alter_resource_id`. |

La primera migración de `pages` crea los modelos del catálogo. La segunda actualiza los identificadores de `Category` y `Resource`. El campo `resource_type` ya figuraba en la migración inicial de este proyecto.

### Comprobar la sincronización

```bat
python manage.py makemigrations --check --dry-run
```

Resultado obtenido:

```text
No changes detected
```

El Laboratorio 08 reutiliza los modelos y las migraciones existentes. Las tablas de autenticación y sesiones se gestionan con las migraciones incluidas en Django.

## 8. Arquitectura MTV y funcionamiento de las vistas

### Model

`Category` y `Resource` representan los datos del catálogo. Django aporta los modelos de usuario, grupo y permiso y el almacenamiento de sesiones.

### Template

`base.html` define la estructura común de las páginas. La navegación muestra **Log in** y **Sign up** para visitantes. Las cuentas autenticadas ven **Dashboard** y **Log out**. **Review** aparece cuando la cuenta tiene `pages.view_resource`.

### View

Las vistas reciben la solicitud, comprueban el acceso cuando corresponde y devuelven una respuesta. `resources()` consulta los recursos mediante el ORM y los envía a `resources.html`. `resource_review()` también consulta el catálogo y protege la operación mediante dos decoradores.

### Identificación, autenticación y autorización

| Concepto | Aplicación en ClassroomHub |
|---|---|
| Identificación | La persona indica qué cuenta quiere utilizar mediante su nombre de usuario. |
| Autenticación | Django verifica las credenciales y establece la identidad de la cuenta para las solicitudes siguientes. |
| Autorización | Django comprueba si esa cuenta tiene el permiso necesario para consultar la página de revisión. |

### Registro e inicio de sesión

1. `signup()` presenta `UserCreationForm` y procesa su envío por POST.
2. El formulario valida el nombre de usuario y las contraseñas. Cuando los datos son válidos, guarda una cuenta común con una contraseña procesada mediante un hash y redirige a login.
3. `LoginView` verifica las credenciales y abre la sesión. Si existe un destino `next` válido, lo usa para la redirección. En los demás casos abre el panel.
4. `request.user` identifica a la cuenta de la solicitud. `request.session` almacena el contador de visitas al panel.
5. `LogoutView` recibe el formulario POST, invalida la sesión y redirige a la página de inicio.

Los formularios de registro, login y logout incluyen `{% csrf_token %}`. El middleware de sesiones permite recuperar la sesión a partir de su cookie, y el middleware de autenticación establece `request.user`. `SessionMiddleware` debe ejecutarse antes de `AuthenticationMiddleware`.

### Destinos de autenticación

| Ajuste | Ruta nombrada | Función |
|---|---|---|
| `LOGIN_URL` | `pages:login` | Envía al login a un visitante que solicita una vista privada. |
| `LOGIN_REDIRECT_URL` | `pages:dashboard` | Define el destino predeterminado tras un login correcto. |
| `LOGOUT_REDIRECT_URL` | `pages:home` | Define el destino tras cerrar sesión. |

## 9. Rutas principales

| Ruta | Acceso | Descripción |
|---|---|---|
| `/` | Público | Página de inicio. |
| `/resources/` | Público | Listado de recursos almacenados en MariaDB. |
| `/about/` | Público | Información sobre el propósito del proyecto. |
| `/faq/` | Público | Preguntas frecuentes, página heredada del proyecto. |
| `/accounts/signup/` | Visitante | Formulario para crear una cuenta común. |
| `/accounts/login/` | Público | Formulario de inicio de sesión. |
| `/accounts/logout/` | POST con CSRF | Cierre de sesión mediante el botón del menú. Una solicitud GET devuelve HTTP `405`. |
| `/dashboard/` | Cuenta autenticada | Panel privado con nombre de usuario y contador de visitas. |
| `/dashboard/summary/` | Cuenta autenticada | Resumen de solo lectura con el total de recursos y el total disponible. |
| `/resources/review/` | Cuenta autenticada con `pages.view_resource` | Página de revisión del catálogo de solo lectura. |
| `/admin/` | Personal autorizado | Administración de categorías, recursos, usuarios y grupos. |

Las rutas de `pages` utilizan nombres como `pages:dashboard`, `pages:dashboard-summary` y `pages:resource-review` para generar enlaces y redirecciones desde el código y las plantillas.

## 10. Django Admin, usuarios y permisos

### Administración del catálogo

Django Admin permite crear, consultar, actualizar y eliminar categorías y recursos de acuerdo con los permisos de la cuenta administradora. Los cambios quedan almacenados en MariaDB y se reflejan en `/resources/`. El panel también ofrece búsquedas y filtros según la configuración de `pages/admin.py`.

### Crear una cuenta común

1. Abre `/accounts/signup/` sin iniciar sesión.
2. Escribe un nombre de usuario y confirma la contraseña.
3. Envía el formulario. Si los datos son válidos, Django crea la cuenta y abre el login.
4. Ingresa con esa cuenta para comprobar el acceso al panel.

### Crear el grupo `Catalog reviewers`

1. Si necesitas una cuenta administradora, ejecuta `python manage.py createsuperuser`.
2. Abre `/admin/` e inicia sesión con la cuenta administradora.
3. En **Groups**, crea un grupo con el nombre `Catalog reviewers`.
4. Asigna únicamente **Can view resource** del modelo `Resource` de la aplicación `pages`. El permiso se identifica en código como `pages.view_resource`.
5. En **Users**, abre la cuenta común que usarás como revisora y agrégala al grupo. Mantén desactivados **Staff status** y **Superuser status** para esa cuenta.
6. Guarda los cambios e inicia sesión en ClassroomHub con la cuenta revisora para consultar `/resources/review/`.

El grupo y sus asignaciones se guardan en la base de datos. Repite esta configuración en cada instalación nueva.

### Comportamiento por tipo de acceso

| Ruta | Visitante anónimo | Cuenta común sin permiso | Cuenta revisora |
|---|---|---|---|
| `/resources/` | HTTP `200` | HTTP `200` | HTTP `200` |
| `/dashboard/` | Redirección al login | HTTP `200` | HTTP `200` |
| `/dashboard/summary/` | Redirección al login | HTTP `200` | HTTP `200` |
| `/resources/review/` | Redirección al login | HTTP `403` | HTTP `200` |

En `resource_review`, `@login_required` se aplica antes de `@permission_required("pages.view_resource", raise_exception=True)`. La vista comprueba el permiso incluso cuando alguien escribe la URL directamente.

## 11. Consultas mediante el ORM

### Consultar recursos y categorías

```python
from pages.models import Category, Resource

resources = Resource.objects.select_related("category").all()
available_resources = Resource.objects.filter(available=True)
category = Category.objects.get(name="Programming")
category_resources = category.resources.all()
```

`select_related("category")` permite recuperar los datos de la categoría junto con cada recurso. El catálogo público y la vista de revisión utilizan esta relación para presentar la información.

### Contar recursos en el resumen privado

```python
total_resources = Resource.objects.count()
available_resources = Resource.objects.filter(available=True).count()
```

El primer conteo incluye todos los registros. El segundo incluye los que tienen `available=True`. La vista entrega los dos valores a `dashboard_summary.html` y solo requiere una sesión autenticada.

### Consultar usuarios y permisos

Desde `python manage.py shell` se puede inspeccionar una cuenta existente. Reemplaza el nombre de ejemplo por una cuenta registrada en tu instalación.

```python
from django.contrib.auth import get_user_model

User = get_user_model()
account = User.objects.get(username="nombre_de_usuario")

print(account.is_staff)
print(account.is_superuser)
print(account.groups.count())
print(account.has_perm("pages.view_resource"))
```

`create_user()` y `set_password()` son las herramientas de Django para crear cuentas o cambiar contraseñas desde Python. El registro web usa `UserCreationForm`, que aplica el procesamiento de contraseñas al guardar la cuenta.

## 12. Pruebas automatizadas

Las pruebas se encuentran en `pages/tests.py`. El Laboratorio 08 conserva las diez pruebas del catálogo y agrega dieciocho de autenticación y permisos y dos del reto adicional.

| Bloque | Cantidad | Cobertura |
|---|---:|---|
| Laboratorio 07 | 10 | Páginas, navegación, respuestas HTTP, datos del catálogo, modelos y relaciones. |
| `AuthenticationTests` | 12 | Registro, formularios inválidos, credenciales, redirecciones, contador de sesión, logout y CSRF. |
| `ResourceReviewPermissionTests` | 6 | Acceso anónimo, rechazo de cuentas sin permiso, acceso de revisores y continuidad del catálogo público. |
| `DashboardSummaryTests` | 2 | Redirección de visitantes y conteos correctos para una cuenta autenticada común. |
| **Total** | **30** | **Catálogo, autenticación, sesiones, permisos y resumen privado.** |

### Casos cubiertos en el Laboratorio 08

| Funcionalidad | Casos verificados |
|---|---|
| Registro | Se muestra el formulario. Una cuenta válida se crea sin privilegios administrativos y su contraseña se puede verificar. Las contraseñas distintas y los nombres duplicados se rechazan. |
| Login | Las credenciales incorrectas no abren una sesión. Las correctas redirigen al panel o al destino local indicado en `next`. |
| Panel | Un visitante recibe una redirección al login. Las visitas consecutivas en una sesión incrementan el contador. |
| Logout | GET devuelve HTTP `405`. POST cierra la sesión y una nueva solicitud al panel requiere autenticación. |
| CSRF | El cliente con verificación CSRF activa rechaza con HTTP `403` un POST de login sin token. |
| Revisión | El visitante va al login. La cuenta común recibe HTTP `403`, incluso al escribir la URL. El revisor recibe HTTP `200` sin convertirse en personal administrativo. |
| Catálogo público | La página muestra recursos a visitantes sin sesión. |
| Resumen privado | El visitante va al login. Una cuenta común autenticada puede ver el total y el número de recursos disponibles. |

### Ejecutar las pruebas

```bat
python manage.py test pages
```

Para ver el nombre y resultado de cada prueba:

```bat
python manage.py test pages -v 2
```

### Base de pruebas

El esquema de pruebas configurado para el proyecto es `test_classroom_hub`. Debe estar separado de `classroom_hub`, que contiene los datos de desarrollo. Las pruebas crean sus propios recursos, usuarios y grupos. La salida de la ejecución confirmó la creación y eliminación de la base temporal asociada al alias `default`.

## 13. Ejecución del proyecto

Desde la carpeta que contiene `manage.py`, activa el entorno virtual y confirma que MariaDB esté iniciado. Después ejecuta:

```bat
python manage.py check
python manage.py migrate
python manage.py runserver
```

Abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador. Para detener el servidor, pulsa `Ctrl + C` en la terminal.

### Probar una sesión completa

1. Abre **Sign up** y crea una cuenta común.
2. Entra a **Log in** e inicia sesión con esa cuenta.
3. Abre **Dashboard**. La primera visita muestra `1`. Una recarga debe mostrar `2`.
4. Abre **View resource summary** y comprueba ambos conteos.
5. Pulsa **Log out**. El navegador debe volver al inicio.
6. Intenta abrir `/dashboard/` sin sesión. Django debe enviarte al login.
7. Inicia sesión otra vez y comprueba que el contador empiece en `1`.

## 14. Dificultades encontradas y soluciones

### Configuración heredada de MariaDB

En el Laboratorio 07 se pasó de la instalación de MariaDB incluida en XAMPP a una instalación independiente en el puerto `3307`. Esta configuración permitió conservar la conexión del catálogo y preparar los permisos del esquema de pruebas. El Laboratorio 08 reutiliza esa configuración.

### Consulta de una cuenta inexistente

Durante el reto de registro se ejecutó `User.objects.get()` con un nombre de ejemplo. Django devolvió `User.DoesNotExist` y los intentos de consultar `account` produjeron `NameError` porque la variable no se había asignado.

Se listaron los nombres existentes mediante `values_list("username", flat=True)`, se consultó la cuenta registrada y se ejecutaron las instrucciones en líneas separadas. El resultado fue `False False 0` para `is_staff`, `is_superuser` y cantidad de grupos.

### Publicación en la rama del laboratorio

El primer intento de push devolvió `src refspec laboratorio-8 does not match any`. El commit ya existía localmente, pero la rama de destino aún no estaba disponible en esa copia y `origin` apuntaba al repositorio anterior.

Se actualizó `origin` para apuntar a `ClassroomHub`, se obtuvo la rama `laboratorio-8` y se incorporó el commit existente. La comprobación de Git mostró el mismo commit en `laboratorio-8` y `origin/laboratorio-8`.

## 15. Funcionalidades implementadas

### Catálogo persistente

- Navegación mediante rutas, vistas y plantillas de Django.
- Conexión a MariaDB mediante variables de entorno.
- Modelos `Category` y `Resource` con relación uno a muchos.
- Consultas dinámicas mediante el ORM.
- Administración de categorías y recursos mediante Django Admin.
- Migraciones y pruebas del catálogo en un esquema independiente.

### Autenticación y control de acceso

- Registro de cuentas comunes mediante `UserCreationForm`.
- Inicio de sesión con `LoginView` y manejo del destino `next`.
- Cierre de sesión mediante `LogoutView` con POST y CSRF.
- Navegación según el estado de autenticación y el permiso de revisión.
- Panel protegido con `@login_required` y contador en `request.session`.
- Revisión de solo lectura protegida con `pages.view_resource`.
- Grupo `Catalog reviewers` para asignar el permiso a cuentas de prueba.
- Resumen privado con el total de recursos y el total disponible.
- Pruebas de registro, credenciales, sesión, CSRF y permisos.

## 16. Alcance y posibles mejoras

El Laboratorio 08 concentra la administración de datos en Django Admin. Desde la interfaz web, las cuentas pueden consultar el catálogo público y, según su acceso, el panel, el resumen y la página de revisión.

Los formularios CRUD fuera de Django Admin, la recuperación de contraseñas por correo, la autenticación multifactor y los proveedores externos de identidad quedan fuera del alcance de esta etapa. Entre las ampliaciones del catálogo se contemplan búsqueda, filtros, paginación y formularios de edición sujetos a permisos específicos.

## 17. Conclusiones

El Laboratorio 08 amplió ClassroomHub con el sistema de usuarios y sesiones de Django sobre el catálogo persistente del Laboratorio 07. El panel y el resumen privado requieren una sesión autenticada. La página de revisión añade una comprobación de permiso para separar el acceso de las cuentas comunes y el de las cuentas revisoras.

El uso de `UserCreationForm`, `LoginView` y `LogoutView` permitió aprovechar las herramientas de validación y autenticación del framework. Las pruebas automatizadas comprobaron los flujos de registro y sesión, las restricciones de acceso y la continuidad del catálogo público.

## 18. Verificación final del Laboratorio 08

### 18.1. Estado de las migraciones

Se ejecutó:

```bat
python manage.py showmigrations auth contenttypes sessions pages
```

Todas las migraciones de las cuatro aplicaciones aparecieron aplicadas. La comprobación `python manage.py makemigrations --check --dry-run` devolvió `No changes detected`.

### 18.2. Comprobación de configuración

```text
System check identified no issues (0 silenced).
```

### 18.3. Registro de una cuenta sin privilegios

En el shell de Django se verificaron los valores de `is_staff`, `is_superuser` y la cantidad de grupos de la cuenta usada para el reto.

```text
False False 0
```

### 18.4. Resultado de las pruebas automatizadas

```text
Found 30 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..............................
----------------------------------------------------------------------
Ran 30 tests in 73.847s

OK
Destroying test database for alias 'default'...
```

**Resultado final: 30 pruebas aprobadas y 0 fallos.** El total incluye las 28 pruebas de la entrega base y las dos pruebas del resumen privado.

## 19. Estrategia de control de versiones

El proyecto continúa en el repositorio personal `juanlsk29/ClassroomHub`. La rama `laboratorio-8` parte del trabajo del Laboratorio 07 y reúne los cambios de autenticación y autorización en dos etapas.

| Etapa | Commit | Estado al documentar |
|---|---|---|
| Base del Laboratorio 07 | `f2b794f` — `feat: mostrar recursos persistidos` | Presente en el historial. |
| Primera parte del Laboratorio 08 | `ee3d347` — `feat: agregar registro, inicio y cierre de sesión y panel privado` | Publicado en `origin/laboratorio-8`. |
| Segunda parte del Laboratorio 08 | `feat: agregar revisión del catálogo, resumen privado y pruebas de acceso` | Pendiente de crear al redactar el README. |

El segundo commit reúne la vista de revisión, el resumen privado, las pruebas nuevas y esta documentación. Los grupos, las cuentas y sus asignaciones se configuran en la base de datos de cada instalación. Las credenciales, el archivo `.env`, las cookies de sesión y los datos privados de usuarios quedan fuera del repositorio.

## 20. Estado final del Laboratorio 08

| Componente | Estado |
|---|---|
| Catálogo persistente | Conserva los modelos y la conexión a MariaDB del Laboratorio 07. |
| Autenticación | Registro, login y logout integrados con las herramientas de Django. |
| Sesiones | Panel privado con contador de visitas. |
| Autorización | Revisión protegida mediante `pages.view_resource`. |
| Reto adicional | Resumen privado con conteos del ORM y dos pruebas. |
| Migraciones | Aplicadas en `auth`, `contenttypes`, `sessions` y `pages`. |
| Verificación de Django | Cero problemas y ningún cambio pendiente de migración. |
| Pruebas automatizadas | 30 aprobadas. |
| Rama de entrega | `laboratorio-8`. |