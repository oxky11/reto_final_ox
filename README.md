# Reto Final Oscar Llopis Herrero

# Gestor de ramas.
Para realizar modificaciones en la rama, lo primero que haremos será en JIRA (<Dirección del JIRA>) tomar un ticket del sprint que esté en To-Do. Nos quedaremos con el código o nombre del ticket. 

Tendremos dos formas de crear la rama. Siempre la realizaremos desde main.
En la consola realizaremos el siguiente comando:

```
git branch [nombre-rama]
```

Se escribirá de la siguiente manera:

```
 [tipo-ticket]/[nombre-ticket]
```
 
La ramas o tipo-ticket pueden ser clasificadas por

- FEATURE : Nuevos evolutivos
- BUG : Corrección de errores

El nombre-ticket corresponderá al código del ticket del JIRA.

```
git checkout [nombre-rama]
```

# Arranque del proyecto

En nuestro IDE podemos arrancar el proyecto , o podemos hacerlo mediante Docker.

Siendo Docker realizamos los siguientes pasos:

```
docker-compose build
docker-compose up -d 
```

## Hacer peticiones en CMD

```
$ curl -GET 127.0.0.1:5000/data
```

## Ejecución de tests

En la carpeta raiz podemos ejecutar un shell ejecutando este comando

```
python -m unittest ./app/tests/tests.py
```

2025-04-19