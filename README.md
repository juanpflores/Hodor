# Culture.ly
Culturely es una plataforma educativa e interactiva orientada a los niños para aprender y conocer acerca
de distintos hámbitos, entre ellos ciencia y cultura.

## Instalación
Necesitas [`Python3`](https://www.python.org/downloads/) y [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/).

Crea un entorno virtual:
```shell
$ mkvirtualenv -p python3 adventures
```

Instala dependencias de desarrollo:
```shell
$ pip install -r requirements/dev.txt
```

Edita el archivo postactivate: 
```shell
$ vim $VIRTUAL_ENV/bin/postactivate
```

y declara las siguientes variables de entorno con su valor correspondiente:
```shell
export DJANGO_SECRET_KEY=''

export DATABASE_NAME=''
export DATABASE_USER=''
export DATABASE_PASSWORD=''
export DATABASE_HOST='localhost'
export DATABASE_PORT=5432

export DJANGO_SETTINGS_MODULE='adventures.settings.dev'  # ¡Importante!
```

En la raiz del proyecto, haz las migraciones:
```shell
$ ./manage.py migrate
```

Carga los datos de la base:
```shell
$ ./manage.py loaddata mayas questions
```

Corre el servidor
```shell
$ ./manage.py runserver
```

Finalmente ve a [`localhost:8000`](http://localhost:8000) 🚀

¡Y listo! 👌
