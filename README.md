# ClassroomHub

## 1. Descripción del proyecto

ClassroomHub es una aplicación web educativa desarrollada con Django que permite consultar y administrar recursos relacionados con la programación y el desarrollo de software.

El proyecto inició como una aplicación enfocada en los fundamentos de Django, utilizando rutas, vistas y plantillas HTML. En el Laboratorio 7 se amplió su funcionamiento mediante la integración de una base de datos MariaDB, permitiendo almacenar información de manera persistente y administrarla a través del ORM y Django Admin.

El objetivo principal es aplicar el patrón MTV (Model-Template-View), establecer relaciones entre modelos, gestionar migraciones y comprobar el correcto funcionamiento de la aplicación mediante pruebas automatizadas.

## 2. Tecnologías y versiones

- **Lenguaje:** Python 3.14.5.
- **Framework:** Django 6.1.3.
- **Base de datos:** MariaDB 13.0.2.
- **Frontend:** HTML y CSS.
- **Entorno virtual:** venv.
- **Conector SQL:** mysqlclient.
- **Variables de entorno:** python-dotenv.
- **Administración de datos:** Django Admin.
- **Pruebas automatizadas:** TestCase de Django.
- **Control de versiones:** Git y GitHub.

La aplicación utiliza MariaDB como motor de base de datos y el ORM de Django para realizar operaciones sin escribir directamente las consultas SQL.

## 3. Estructura del proyecto

```text
laboratorio-06/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── pages/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_alter_category_id_alter_resource_id.py
│   │
│   ├── templates/
│   │   └── pages/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── resources.html
│   │       ├── about.html
│   │       └── faq.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .env
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

### Responsabilidades principales

- **config/settings.py:** contiene la configuración general del proyecto y la conexión con MariaDB.
- **config/urls.py:** organiza las rutas principales de Django.
- **pages/models.py:** define los modelos Category y Resource.
- **pages/views.py:** procesa las solicitudes HTTP y consulta los recursos mediante el ORM.
- **pages/urls.py:** define las rutas de la aplicación.
- **pages/admin.py:** configura la administración de categorías y recursos.
- **pages/templates/:** contiene las plantillas HTML de las páginas.
- **pages/migrations/:** almacena los cambios realizados en la estructura de la base de datos.
- **pages/tests.py:** contiene las pruebas automatizadas.
- **manage.py:** permite ejecutar comandos de administración de Django.
- **requirements.txt:** registra las dependencias necesarias para instalar el proyecto.
- **.env:** almacena las variables privadas de configuración.

## 4. Instalación y configuración

### Requisitos previos

Para ejecutar ClassroomHub se necesita:

- Python compatible con Django 6.1.
- MariaDB 10.11 o superior, o una versión compatible de MySQL.
- Git.
- Una terminal de comandos.
- Un entorno virtual de Python.

### Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd laboratorio-06
```

Reemplazar `URL_DEL_REPOSITORIO` por la dirección real del repositorio de GitHub.

### Crear el entorno virtual

```bash
python -m venv .venv
```

### Activar el entorno virtual

En Windows (CMD):

```cmd
.venv\Scripts\activate
```

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

Las dependencias principales del proyecto son Django, mysqlclient y python-dotenv.

## 5. Configuración de MariaDB

### Creación de la base de datos

El proyecto utiliza una base de datos llamada `classroom_hub`.

Desde una cuenta administradora de MariaDB se puede crear mediante:

```sql
CREATE DATABASE IF NOT EXISTS classroom_hub
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

### Creación del usuario SQL

Se utiliza un usuario específico para la aplicación, evitando conectar Django directamente con la cuenta root.

```sql
CREATE USER 'classroomhub_user'@'127.0.0.1'
IDENTIFIED BY 'CONTRASENA_PRIVADA';
```

La contraseña debe reemplazarse por una clave privada elegida durante la configuración.

### Asignación de permisos

```sql
GRANT ALL PRIVILEGES ON classroom_hub.*
TO 'classroomhub_user'@'127.0.0.1';

GRANT ALL PRIVILEGES ON test_classroom_hub.*
TO 'classroomhub_user'@'127.0.0.1';
```

Los permisos de la segunda base permiten que Django ejecute las pruebas automatizadas en una base independiente.

### Configuración de variables de entorno

El archivo `.env` contiene la configuración necesaria para conectar Django con MariaDB.

Ejemplo de configuración:

```env
DB_NAME=classroom_hub
DB_USER=classroomhub_user
DB_PASSWORD=CONTRASENA_PRIVADA
DB_HOST=127.0.0.1
DB_PORT=3307
```

Durante el desarrollo se utilizó una instalación independiente de MariaDB 13.0.2 en el puerto `3307`, separada de la instalación de XAMPP.

El archivo `.env.example` sirve como referencia para configurar el proyecto en otros equipos.

**Importante:** el archivo `.env` no debe subirse al repositorio porque contiene credenciales privadas. Debe permanecer excluido mediante `.gitignore`.

## 6. Modelos y relaciones

En el Laboratorio 7 se implementaron dos modelos principales: `Category` y `Resource`.

### Modelo Category

Representa las categorías utilizadas para organizar los recursos educativos.

Campos principales:

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Clave primaria | Identificador de la categoría |
| `name` | CharField | Nombre único de la categoría |
| `description` | TextField | Descripción opcional |

Las categorías se ordenan alfabéticamente por nombre.

### Modelo Resource

Representa los recursos educativos registrados en ClassroomHub.

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Clave primaria | Identificador del recurso |
| `title` | CharField | Título del recurso |
| `description` | TextField | Descripción opcional |
| `available` | BooleanField | Indica si está disponible |
| `category` | ForeignKey | Categoría relacionada |
| `created_at` | DateTimeField | Fecha de creación |
| `resource_type` | CharField | Tipo de recurso, opcional |

### Relación entre los modelos

La relación entre `Category` y `Resource` es de **uno a muchos (1:N)**.

Esto significa que una categoría puede tener varios recursos, mientras que cada recurso pertenece a una categoría.

La relación utiliza `ForeignKey` con `on_delete=models.PROTECT`, evitando eliminar una categoría cuando todavía tiene recursos asociados.

También se utiliza `related_name="resources"` para consultar los recursos de una categoría.

## 7. Migraciones de la base de datos

Las migraciones permiten mantener sincronizados los modelos de Python con las tablas de MariaDB.

### Generar migraciones

```bash
python manage.py makemigrations
```

### Aplicar migraciones

```bash
python manage.py migrate
```

### Consultar las migraciones

```bash
python manage.py showmigrations pages
```

En el desarrollo de ClassroomHub se aplicaron las siguientes migraciones:

- `0001_initial`: creación inicial de los modelos.
- `0002_alter_category_id_alter_resource_id`: actualización de los campos identificadores de Category y Resource.

### Comprobar sincronización

```bash
python manage.py makemigrations --check --dry-run
```

Resultado obtenido:

```text
No changes detected
```

Esto confirma que los modelos y las migraciones se encuentran sincronizados.

## 8. Arquitectura MTV y funcionamiento de las rutas

ClassroomHub utiliza el patrón MTV de Django, compuesto por tres elementos.

### Model (Modelo)

Se encarga de representar y gestionar los datos almacenados en MariaDB.

Los modelos Category y Resource permiten crear, consultar, actualizar y eliminar registros mediante el ORM de Django.

### Template (Plantilla)

Se encarga de presentar la información mediante HTML.

La plantilla `base.html` contiene elementos compartidos, como la navegación y la estructura general. Las demás páginas reutilizan estos elementos mediante herencia de plantillas.

### View (Vista)

Recibe las solicitudes HTTP, ejecuta la lógica correspondiente y devuelve una respuesta al navegador.

En la ruta `/resources/`, la vista consulta los recursos guardados en MariaDB y envía los resultados a la plantilla `resources.html`.

### Funcionamiento de `/resources/`

1. El navegador solicita `/resources/`.
2. Django identifica la ruta en los archivos de configuración.
3. Se ejecuta la vista `resources()` de `pages/views.py`.
4. La vista consulta el modelo Resource mediante el ORM.
5. Se recuperan los recursos registrados en la base de datos.
6. Los resultados se envían a `resources.html`.
7. Django genera la respuesta HTML y la devuelve al navegador.

De esta manera, los recursos se muestran dinámicamente y no dependen de una lista fija escrita en el código.

## 9. Rutas principales

| Ruta | Descripción |
|---|---|
| `/` | Página principal de ClassroomHub |
| `/resources/` | Listado dinámico de recursos educativos |
| `/about/` | Información sobre el propósito del proyecto |
| `/faq/` | Preguntas frecuentes |
| `/admin/` | Panel de administración de Django |

Las rutas utilizan nombres definidos en Django para facilitar la navegación y evitar depender de direcciones escritas manualmente.

Las direcciones inexistentes generan una respuesta HTTP 404.

## 10. Django Admin y operaciones CRUD

ClassroomHub utiliza Django Admin para administrar las categorías y los recursos registrados en MariaDB.

El panel de administración se encuentra en:

```text
http://127.0.0.1:8000/admin/
```

### Administración de categorías

Permite:

- Registrar nuevas categorías.
- Consultar categorías existentes.
- Modificar nombres y descripciones.
- Eliminar categorías cuando sus relaciones lo permiten.
- Buscar categorías por nombre.

### Administración de recursos

Permite:

- Crear recursos educativos.
- Consultar los registros almacenados.
- Actualizar títulos, descripciones, categorías y disponibilidad.
- Eliminar recursos.
- Filtrar por categoría y disponibilidad.
- Buscar por título, descripción y categoría.

Las operaciones CRUD se realizan desde Django Admin y los cambios quedan almacenados en MariaDB.

Se verificó que los recursos registrados o modificados desde el panel administrativo se reflejan correctamente en la página `/resources/`.

## 11. Consultas mediante el ORM

El ORM (Object-Relational Mapping) de Django permite interactuar con la base de datos utilizando clases y métodos de Python.

Algunos ejemplos de operaciones son:

### Consultar recursos

```python
Resource.objects.all()
```

### Consultar recursos disponibles

```python
Resource.objects.filter(available=True)
```

### Consultar una categoría

```python
Category.objects.get(name="Programming")
```

### Consultar recursos y sus categorías

```python
Resource.objects.select_related("category").all()
```

### Consultar recursos asociados a una categoría

```python
category.resources.all()
```

El ORM facilita la organización del código, la administración de relaciones y la separación entre la lógica de la aplicación y las consultas SQL.

## 12. Pruebas automatizadas

En el Laboratorio 7 se actualizaron las pruebas del proyecto para incluir el funcionamiento de los modelos y de la base de datos.

Se utiliza `TestCase` de Django, que permite ejecutar pruebas con consultas SQL de forma aislada.

### Pruebas implementadas

| N.º | Prueba | Objetivo |
|---|---|---|
| 1 | `test_home_page_renders` | Verificar la página de inicio |
| 2 | `test_about_page_renders` | Verificar la página About |
| 3 | `test_faq_page_uses_correct_template` | Verificar la plantilla de FAQ |
| 4 | `test_home_navigation_links_to_resources` | Verificar la navegación |
| 5 | `test_resources_page_shows_example_data` | Verificar recursos obtenidos desde la base de datos de pruebas |
| 6 | `test_unknown_page_returns_not_found` | Verificar respuesta HTTP 404 |
| 7 | `test_category_string_representation` | Verificar la representación de Category |
| 8 | `test_resource_string_representation` | Verificar la representación de Resource |
| 9 | `test_category_resource_relationship` | Verificar la relación entre modelos |
| 10 | `test_resource_default_availability` | Verificar el valor predeterminado de disponibilidad |

### Ejecutar las pruebas

```bash
python manage.py test pages -v 2
```

### Resultados obtenidos

```text
Found 10 test(s).
System check identified no issues (0 silenced).

Ran 10 tests in 0.118s

OK
```

**Resultado final: 10 pruebas aprobadas y 0 fallos.**

Durante la ejecución, Django creó temporalmente la base `test_classroom_hub`, aplicó las migraciones y eliminó la base de pruebas al finalizar.

Esto permitió comprobar el funcionamiento de la aplicación sin alterar los registros de la base principal.

## 13. Ejecución del proyecto

### Verificar la configuración

```bash
python manage.py check
```

### Comprobar las migraciones

```bash
python manage.py showmigrations pages
```

### Aplicar migraciones pendientes

```bash
python manage.py migrate
```

### Crear un superusuario

Si es la primera vez que se configura la base de datos:

```bash
python manage.py createsuperuser
```

### Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

Para detener el servidor se utiliza `Ctrl + C` en la terminal.

## 14. Dificultades encontradas y soluciones

### Incompatibilidad entre Django y MariaDB

Inicialmente se intentó utilizar MariaDB 10.4.32, incluido en XAMPP.

Sin embargo, Django 6.1.3 requiere MariaDB 10.11 o superior.

**Solución:** se configuró una instalación independiente de MariaDB 13.0.2 en el puerto `3307`, conservando el servidor de XAMPP en el puerto `3306`.

### Problemas de permisos SQL

Al configurar la base de datos se presentaron errores de acceso relacionados con el usuario de la aplicación.

**Solución:** se creó el usuario `classroomhub_user` y se asignaron los permisos necesarios sobre la base principal y la base de pruebas.

### Corrupción de una tabla interna de XAMPP

Durante la configuración del servidor antiguo se detectó corrupción en la tabla interna `mysql.db`.

**Solución:** se verificó su estado mediante `CHECK TABLE`, se realizó la reparación con `REPAIR TABLE` y se comprobó que la tabla quedara en estado correcto.

### Diferencias entre modelos y migraciones

Django detectó modificaciones pendientes en los identificadores de los modelos Category y Resource.

**Solución:** se generó y aplicó la migración `0002_alter_category_id_alter_resource_id.py`, verificando posteriormente que no existieran cambios pendientes.

### Prueba automatizada incompatible con el ORM

Una prueba heredada del Laboratorio 6 falló porque utilizaba `SimpleTestCase`, que no permite consultas a la base de datos por defecto.

**Solución:** se actualizó el archivo `pages/tests.py` para utilizar `TestCase`, se adaptaron las pruebas existentes y se completaron diez pruebas automatizadas, todas aprobadas.

## 15. Funcionalidades implementadas

- Navegación entre páginas mediante rutas de Django.
- Organización del proyecto mediante el patrón MTV.
- Uso de vistas y plantillas HTML.
- Herencia de plantillas mediante `base.html`.
- Conexión de Django con MariaDB.
- Configuración mediante variables de entorno.
- Modelos Category y Resource.
- Relación uno a muchos entre categorías y recursos.
- Migraciones para crear y actualizar las tablas.
- Consultas a la base de datos mediante el ORM.
- Visualización dinámica de recursos educativos.
- Administración de categorías y recursos mediante Django Admin.
- Operaciones CRUD con persistencia en MariaDB.
- Pruebas automatizadas utilizando una base independiente.
- Validación de rutas, plantillas, modelos y relaciones.

## 16. Limitaciones y posibles mejoras

ClassroomHub es una aplicación académica orientada al aprendizaje de Django y la persistencia de datos.

Aunque permite administrar categorías y recursos mediante Django Admin, todavía no cuenta con formularios CRUD públicos independientes del panel administrativo.

Como posibles mejoras futuras se consideran:

- Implementar formularios propios para registrar recursos.
- Incorporar autenticación y perfiles para estudiantes.
- Permitir búsquedas y filtros desde la interfaz pública.
- Agregar paginación al listado de recursos.
- Implementar una API REST.
- Añadir nuevas pruebas automatizadas para operaciones de creación, actualización y eliminación.

Estas funcionalidades corresponden a posibles ampliaciones y no forman parte de lo implementado actualmente.

## 17. Conclusiones

El Laboratorio 7 permitió ampliar ClassroomHub desde una aplicación basada principalmente en rutas, vistas y plantillas hacia un sistema conectado con una base de datos relacional.

Se implementaron modelos, relaciones, migraciones y consultas mediante el ORM de Django, permitiendo que los recursos educativos se almacenen de forma persistente.

Django Admin facilitó la administración de los registros y permitió comprobar las operaciones CRUD.

Finalmente, las diez pruebas automatizadas se ejecutaron correctamente, validando el funcionamiento de las páginas, los modelos y sus relaciones.

El proyecto demuestra la importancia de separar responsabilidades, proteger las credenciales, utilizar migraciones y verificar el funcionamiento del sistema mediante pruebas.

## 18. Verificación final del Laboratorio 7

Durante el desarrollo del Laboratorio 7 se realizaron comprobaciones de funcionamiento para validar la conexión entre Django y MariaDB, las operaciones mediante el ORM, las relaciones entre modelos y la persistencia de información.

### 18.1. Operaciones CRUD mediante el ORM

Se utilizaron los siguientes métodos:

| Método | Operación comprobada |
|---|---|
| `objects.create()` | Creación de categorías y recursos |
| `objects.all()` | Consulta de registros existentes |
| `objects.filter()` | Filtrado de recursos disponibles |
| `objects.get()` | Consulta de un recurso específico |
| `save()` | Actualización de la información de un recurso |
| `delete()` | Eliminación de registros |
| `category` | Acceso a la categoría relacionada |
| `related_name` | Consulta de recursos desde una categoría |
| `select_related()` | Consulta de recursos junto con sus categorías |

Todas las operaciones ejecutadas finalizaron correctamente. Los registros temporales utilizados para comprobar el ORM fueron eliminados al concluir las pruebas.

### 18.2. Integridad referencial

Se verificó el funcionamiento de `on_delete=models.PROTECT` intentando eliminar una categoría que tenía un recurso relacionado.

Django generó la excepción `ProtectedError`, impidiendo la eliminación.

Posteriormente se comprobó que ambos registros seguían existiendo. Después de eliminar primero el recurso, fue posible eliminar la categoría.

Esto demuestra el funcionamiento de la restricción de integridad entre `Category` y `Resource`.

### 18.3. Persistencia de datos

Se comprobó que los datos permanecen almacenados después de detener y reiniciar el servidor de Django.

Como evidencia, se utilizó un recurso denominado `Quijote`, que continuó apareciendo en la página `/resources/` después de reiniciar la aplicación.

Esto confirma que los recursos no dependen exclusivamente de variables temporales en Python, sino que se recuperan desde MariaDB.

### 18.4. Resultado de las pruebas automatizadas

Se ejecutó el comando:

```bash
python manage.py test pages -v 2
```

Resultado obtenido:

```text
Found 10 test(s).
System check identified no issues (0 silenced).

Ran 10 tests in 0.118s

OK
```

Las diez pruebas finalizaron correctamente. Django creó la base temporal `test_classroom_hub`, aplicó las migraciones necesarias y la eliminó al finalizar.

### 18.5. Estado de las migraciones

El proyecto dispone de las siguientes migraciones:

- `0001_initial.py`: creación de los modelos `Category` y `Resource`.
- `0002_alter_category_id_alter_resource_id.py`: actualización de los campos identificadores.

Se comprobó la sincronización de los modelos mediante:

```bash
python manage.py makemigrations --check --dry-run
```

Resultado:

```text
No changes detected
```

El campo `resource_type` está implementado en el modelo `Resource` y fue incluido originalmente en `0001_initial.py`. Su incorporación mediante una migración independiente permanece como un punto de ajuste respecto a la secuencia solicitada en el laboratorio.

## 19. Estrategia de control de versiones

ClassroomHub se desarrolla en un único repositorio de GitHub, conservando los avances de los laboratorios anteriores y ampliando las funcionalidades progresivamente.

La estrategia de trabajo consiste en:

1. Conservar en `main` las versiones estables.
2. Crear una rama para cada nueva etapa del proyecto.
3. Registrar commits que identifiquen los cambios técnicos realizados.
4. Verificar las funcionalidades y pruebas antes de integrar los cambios.
5. Utilizar Pull Requests para fusionar cada etapa con `main`.
6. Crear etiquetas para identificar las versiones finales de los laboratorios.

Las ramas previstas son `lab-07`, `lab-08` y `lab-09`, partiendo del trabajo desarrollado en el Laboratorio 6.

Esta estrategia permite mantener un historial del desarrollo y construir progresivamente una versión definitiva de ClassroomHub.

## 20. Estado final del Laboratorio 7

Se verificó el funcionamiento de la aplicación web, la conexión con MariaDB, las operaciones CRUD, las consultas con relaciones, la protección de integridad referencial y la persistencia después de reiniciar el servidor.

También se confirmó la aplicación de las migraciones existentes y la ejecución satisfactoria de diez pruebas automatizadas.

Queda documentada como particularidad del historial de migraciones la inclusión inicial del campo `resource_type`, en lugar de su incorporación mediante una migración posterior.