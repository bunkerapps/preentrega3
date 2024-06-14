# Instrucciones para iniciar el proyecto preentrega3

Este documento proporciona una guía paso a paso para poner en marcha el proyecto `preentrega3`.

## Requisitos previos

Asegúrate de tener instalado Python y Django en tu sistema. Este proyecto ha sido desarrollado con Django 5.0.6.

## Configuración del entorno

1. Clona el repositorio a tu máquina local (ajusta la URL según sea necesario):

```sh
git clone <URL-del-repositorio>
```

2. Clona el repositorio a tu máquina local (ajusta la URL según sea necesario):
```sh
cd preentrega3
```

3. Instala las dependencias del proyecto:
```sh
pip install -r requirements.txt
```

4. Realiza las migraciones necesarias para configurar la base de datos:
```sh
python manage.py migrate
```

5. Inicia el servidor de desarrollo:
```sh
python manage.py runserver
```

Ahora deberías poder acceder al proyecto en http://127.0.0.1:8000/.
