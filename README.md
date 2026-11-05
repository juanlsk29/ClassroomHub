# ClassroomHub

## 1. Descripción del proyecto

ClassroomHub es una aplicación web desarrollada con Django que funciona como un pequeño portal educativo. Su objetivo es permitir que los estudiantes consulten recursos relacionados con la programación y conozcan el propósito del proyecto.

El proyecto permite practicar los fundamentos de Django mediante la relación entre rutas, vistas y plantillas, utilizando una estructura organizada y reutilizando elementos comunes de la interfaz.

## 2. Tecnologías y versiones

- **Lenguaje:** Python 3.14.5
- **Framework:** Django 6.1.3
- **Frontend:** HTML y CSS
- **Entorno virtual:** venv
- **Pruebas:** SimpleTestCase de Django

## 3. Estructura del proyecto

```text
classroom-hub/
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
│   ├── templates/
│   │   └── pages/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── resources.html
│   │       ├── about.html
│   │       └── faq.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## 4. Instalación y configuración

### Requisitos previos

- Tener Python 3.14.5 instalado.
- Tener instalado Git.
- Contar con una terminal para ejecutar los comandos.

### Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd classroom-hub
```

Reemplazar `URL_DEL_REPOSITORIO` por la dirección real del repositorio.

### Crear el entorno virtual

```bash
python -m venv .venv
```

### Activar el entorno virtual

En Windows (CMD):

```bash
.venv\Scripts\activate
```

En Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar las dependencias

Con el entorno virtual activado, ejecutar:

```bash
python -m pip install -r requirements.txt
```

## 5. Ejecución del proyecto

Antes de iniciar el servidor, se recomienda comprobar la configuración:

```bash
python manage.py check
```

Para ejecutar las pruebas automatizadas:

```bash
python manage.py test pages
```

Para iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

Abrir el navegador en:

http://127.0.0.1:8000/

## 6. Rutas principales

| Ruta | Descripción |
|---|---|
| `/` | Página de inicio con un mensaje de bienvenida y el propósito de ClassroomHub. |
| `/resources/` | Presenta una lista de recursos educativos con sus categorías y disponibilidad. |
| `/about/` | Explica el propósito y objetivo del proyecto. |

### Página opcional

| Ruta | Descripción |
|---|---|
| `/faq/` | Presenta preguntas frecuentes y respuestas relacionadas con ClassroomHub. |

## 7. Funcionalidades implementadas

- Navegación entre las páginas mediante rutas de Django.
- Separación de responsabilidades entre URLs, vistas y plantillas.
- Uso de `render()` para mostrar contenido HTML.
- Envío de información desde las vistas hacia las plantillas mediante contextos.
- Uso de estructuras de control de Django Templates, como `if`, `for` y `empty`.
- Reutilización de una plantilla base mediante herencia con `base.html`.
- Navegación común compartida entre las páginas.
- Pruebas automatizadas para verificar las respuestas y plantillas utilizadas.

## 8. Funcionalidades que todavía no incluye

ClassroomHub es un proyecto de práctica enfocado en los fundamentos de Django. Por esta razón, todavía no incluye:

- Registro e inicio de sesión de usuarios.
- Formularios para agregar o modificar información.
- Modelos propios para administrar recursos.
- Base de datos para almacenar recursos de manera persistente.
- Operaciones CRUD (crear, consultar, actualizar y eliminar).
- Panel de administración personalizado.
- API para consultar información desde otras aplicaciones.

La información de los recursos está definida directamente en las vistas, por lo que los cambios realizados en el código determinan los datos que se muestran.

## 9. Pruebas automatizadas

El proyecto utiliza `SimpleTestCase` para comprobar el funcionamiento de sus páginas.

Las pruebas verifican:

1. Que la página de inicio responda correctamente.
2. Que la página de recursos muestre los datos de ejemplo.
3. Que la página About cargue su plantilla.
4. Que la navegación de inicio contenga el enlace a Resources.
5. Que una ruta inexistente devuelva el código HTTP 404.
6. Que la página FAQ responda correctamente y utilice su plantilla correspondiente.

Para ejecutar todas las pruebas:

```bash
python manage.py test pages
```

## 10. Preguntas para explicar la solución

### 1. ¿Qué diferencia existe entre el proyecto `config` y la aplicación `pages`?

El proyecto `config` contiene la configuración general de Django, como los ajustes, las rutas principales y la configuración del servidor.

La aplicación `pages` contiene la funcionalidad de ClassroomHub: sus vistas, rutas propias, plantillas y pruebas.

### 2. ¿Qué ocurre desde que escribes `/resources/` hasta que ves la lista en el navegador?

Primero, Django recibe la solicitud del navegador y consulta las rutas configuradas en `config/urls.py`. Allí encuentra que debe dirigir las solicitudes de la aplicación a `pages/urls.py`.

Después, identifica la ruta `resources/` y ejecuta la función `resources` de `pages/views.py`.

Esta función prepara una lista de recursos y la envía mediante un contexto a la plantilla `resources.html`. Finalmente, `render()` combina la información con el HTML y Django devuelve la respuesta al navegador.

### 3. ¿Qué ventaja aporta `include()` frente a colocar todas las rutas en un único archivo?

`include()` permite separar las rutas de cada aplicación en su propio archivo.

Esto facilita la organización del proyecto, evita concentrar todas las rutas en `config/urls.py` y permite mantener una estructura más fácil de modificar y ampliar.

### 4. ¿Por qué utilizamos `render()` en vez de crear todo el HTML con `HttpResponse`?

Utilizamos `render()` porque permite combinar una plantilla HTML con información enviada desde una vista.

Así podemos separar la lógica de Python de la presentación HTML, reutilizar plantillas y utilizar variables y estructuras de control de Django Templates.

### 5. ¿Qué problema resuelve `base.html` y qué ocurre si se modifica su navegación?

`base.html` evita repetir la estructura HTML, los estilos, la navegación y el footer en cada página.

Las demás plantillas heredan su contenido mediante `{% extends %}`. Si modificamos la navegación en `base.html`, el cambio se refleja automáticamente en todas las páginas que heredan esa plantilla.

### 6. ¿Qué diferencia hay entre una respuesta 404 y un error TemplateDoesNotExist?

Una respuesta 404 indica que Django no encontró una ruta o página correspondiente a la dirección solicitada.

`TemplateDoesNotExist` ocurre cuando una vista intenta cargar una plantilla HTML que Django no puede encontrar en las ubicaciones configuradas.

El primer caso está relacionado con la búsqueda de una ruta; el segundo, con la búsqueda de una plantilla.

### 7. ¿Por qué la lista de recursos siempre vuelve a los valores definidos en `views.py`? ¿Qué faltaría para guardar altas, ediciones o eliminaciones realizadas por usuarios?

Porque los recursos están definidos directamente en una lista dentro de `views.py`. Cada vez que se ejecuta la vista, se utiliza esa información escrita en el código.

Para guardar altas, ediciones o eliminaciones sería necesario implementar modelos de Django y conectarlos a una base de datos. También se necesitarían formularios o mecanismos para recibir y procesar los cambios de los usuarios.

### 8. ¿Qué demuestra `python manage.py check` y qué demuestran las pruebas automatizadas? ¿Por qué no son equivalentes?

`python manage.py check` revisa la configuración del proyecto y detecta posibles problemas en sus componentes y ajustes.

Las pruebas automatizadas comprueban comportamientos específicos, como que las páginas respondan con código 200, utilicen las plantillas correctas o devuelvan un código 404 cuando corresponde.

No son equivalentes porque `check` revisa aspectos generales de configuración, mientras que las pruebas verifican funcionalidades concretas del proyecto.

---

## 11. Autoría y propósito académico

ClassroomHub es un proyecto desarrollado como práctica de aprendizaje para el Laboratorio 6 de fundamentos de Django.

Su propósito es demostrar el manejo básico de proyectos y aplicaciones Django, configuración de rutas, creación de vistas, uso de plantillas, herencia de HTML y pruebas automatizadas.