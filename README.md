Buenas! espero se encuentren bien, mi nombre es Gaston Espinosa
Para esta entrega decidí usar el emprendimiento de mi hermano como el caso sobre el que voy a trabajar lo visto en el curso.
Se trata de un local que funciona como sala de ensayos para los diferentes artistas o grupos musicales en la cual se dan turnos y se da la venta de bebidas en lata. Los problemas que logré identificar son:
    - Organizacion de turnos
    - Foro para contacto de Bandas
    - Organizacion del stock de bebidas
Ya con esta idea empecé a trabajar el proyecto (bastante básico para lo que quiero lograr) buscando la forma de que se creen los turnos y se listen, al igual que las bebidas se puedan cargar y enlistar.
Apps: Bandas, Users y Bebidas
Clases: dentro de Bandas (turnos)

Las 3 clases tienen su funcion crear y listar, con la particularidad de la lista de turnos que es en la que sume la funcion de busqueda.

Algunos de los errores que no pude resolver son:

Errores sin solucionar
	- Borrar un turno me borra la banda en lista (raro, porque el delete se hace en la clase hija)
	- Al actualizar el campo own_instruments (instrumentos propios) al parecer por ser booleano algo me hace en la clase que borra la imagen
	- El campo name_band es un atributo unico que no se puede repetir, esto para no generar muchas copias de la misma banda, sin embargo al estar anotada como banda 'amiga' y luego registrarme para sacar turno no me deja porque 'ya existe uno con el mismo nombre (name_band)' (misma confusión me genera que lo anterior por tratarse de clases hija y padre
	- Al estar logueado y clickear en la opcion mis turnos pasa una cosa rarisimas: si la banda esta registrada me crea un turno vacío
Error más grande
Generar un usuario y que se genere una banda pero que los campos del usuario (name_band , ig) se generen también en esta banda.

Link del video (muestra en funcionamiento): https://youtu.be/sLI5DoBt3o0

Perdón por excederme de tiempo.

