Proyecto realizado para la asignatura Ingeniería Web, Grado en Ingeniería Informática, Universidad de Córdoba.

Se trata de una Red Social que incluye aspectos de geoposicionamiento, varios perfiles por un usuario
(con funcionalidades adaptadas según el perfil), interacción con usuarios cercanos y resposive. 
Acciones a destacar entre usuarios: Chat, Envío de archivos, envío de mensajes y sistema de votaciones.

Se adjunta la documentación realizada también para la asignatura.

﻿=========================================================
=========================================================
==							==
=	SOCIAL NETWORK: HÁBLAME				=
==							==
=========================================================
=========================================================
===========	   REALIZADO POR        ================
=========================================================
==   - Rafael Carlos Soriano Mármol.                   ==
==   - Carlos Sevilla Gómez.                           ==
==   - Luis Ojeda Duque. 			       ==
==   - Francisco Javier Clavero Álvarez.               ==
=========================================================
=========================================================


FrameWork Django usado:
=======================

  [·] Version: 1.5.5
  [·] enlace de descarga: https://www.djangoproject.com/download/1.5.5/tarball
  [·] Version de Python: 2.7


Fichero del proyecto:
=====================

  [·] redSocial
  
  [·] Estructura del proyecto:

	  ...  			
		└── redSocial
		    ├── djangoChat
		    ├── django_messages
		    ├── filetransfers
		    ├── manage.py
		    ├── password_reset
		    ├── principal
		    ├── RedSocial
		    ├── redSocial.sqlite
		    └── users

  [·] Arrancar el servidor de desarrollo para probarlo:

  	1.- Desde la terminal o consola situarse en: 

  				>.../redSocial$

  	2.- Ejecutar:

                >.../redSocial$ python manage.py runserver

    3.- Ir al navegador en la url que se indica:

    			http://localhost:8000

    4.- Para parar el servidor pulsar la combinación de teclas:
				
				 control + C
				 
	5.- [OPCIONAL] Hay una base de datos creada para interactuar pero si se quiere crear de 0
	    borrar la actual llamada "redSocial.sqlite" y volver a sincronizar.
		* Tener en cuenta que los usarios y admin creados para probar la aplicación se borrarán.

		                >.../redSocial$ python manage.py syncdb

Notas Importantes:
	- Usuario Administrador para la aplicación: admin2 ; pass: admin
	
	- Usuario Registrado para la aplicación: usuario ; pass: usuario
	
    - Es importante utilizar el usuario "admin2" como administrador para trabajar con la aplicación con permisos de administrador. 
	  NO se debe usar el usuario "Admin" como usuario de la aplicación, este es únicamente para la inicialización de la base de datos 
	  y carece de muchos campos que son requeridos para el funcionamiento de la aplicación.
	  
	- Existe algún problema con el firefox de la UCO, posiblemente relacionado con la versión o alguna restricción de seguridad. 
	  Usar otro navegador para poder ver a los usuarios en el geolocalizador.
	  
    - La aplicación se basa en los usuarios cercanos, hacen falta mínimo dos usuarios para gran parte de las funcionalidades, 
	  como por ejemplo, ver usuarios cercanos, ver su perfil, iniciar chat, enviar archivo, enviar comentario privado o votar al usuario.
	  
	- Se recomienda usar Google Chrome debido a las funcionalidades implementadas de Google maps. *(Recomendación de Google).
