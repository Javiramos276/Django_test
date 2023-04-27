# Django_test

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django?logo=Python&style=plastic)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=plastic&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css3-%231572B6.svg?style=plastic&logo=css3&logoColor=white)

Este proyecto tiene como fin crear una pagina web como una plantilla para un curriculum vitae.

## Parte 0. Puesta en marcha.
Una vez clonado el repositorio ejecutar en consola
- Ejecutar en consola `pip install -r requeriments.txt` en el directorio donde se quiera ejecutar el proyecto.
- `python3 manage.py makemigrations`. Este comando sirve para hacerle entender a Django que se hicieron cambios en los modelos
- `python3 manage.py migrate` esto es para aplicar las migraciones a la base de datos
- `python3 manage.py createsuperuser` esto es para crear un usuario con acceso al admin http://127.0.0.1:8000/admin/.
- `python3 manage.py runserver` para ejecutar el servidor

## Parte 1. Implementaciones del usuario

- El usuario podrá acceder a la pagina de administración y subir a la base de datos cualquier tipo de imagen
accediendo al siguiente link http://127.0.0.1:8000/admin/.
- El usuario podrá ver sus fotos subidas únicamente si se encuentra con la sesión iniciada.
- El usuario podrá subir/modificar/eliminar el contenido subido a la base de datos
- Un mismo usuario podrá tener mas de una cuenta y en la página principal tener contenido diferente (por ejemplo para crearse mas de un curriculum) 

## Parte 2. Tecnologías utilizadas

* Django
* Python

## Requisitos.

- Python >= 3.7
- Django 4.1.7

# Mejoras

Posibles mejoras para implementar en un futuro.

- En caso de haber mas de una imagen en la base de datos que quiera ser llamada en las plantillas, habrá que recorrer los objetos de la base 
de datos, o bien aplicar un filtro para poder acceder a los mismos y luego se mostrado en la plantilla necesaria.
- Importar de manera correcta los estilos de css. En el proyecto, de momento los estilos que hay son los que se encuentran en la libreria bootstrap.
- Modificar los nombres de las funciones y plantillas si resultan confusos.

