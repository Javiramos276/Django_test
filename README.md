# Django_test

Este proyecto tiene como fin crear una pagina web como una plantilla para un curriculum vitae.

## Parte 0. Puesta en marcha.
Una vez clonado el repositorio ejecutar en consola
- `python3 manage.py migrate` esto es para aplicar las migraciones a la base de datos
- `python3 manage.py createsuperuser` esto es para crear un usuario con acceso al admin http://127.0.0.1:8000/admin/.
- `python3 manage.py runserver` para ejecutar el servidor

## Parte 1. Implementaciones del usuario

- El usuario podrá acceder a la pagina de administración y subir a la base de datos cualquier tipo de imagen
accediendo al siguiente link http://127.0.0.1:8000/admin/.
- El usuario podrá ver sus fotos subidas únicamente si se encuentra con la sesión iniciada.
- El usuario podrá subir/modificar/eliminar el contenido subido a la base de datos

## Parte 2. Tecnologías utilizadas

- Django
- Python
- Bootstrap
