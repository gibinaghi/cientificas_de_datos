# Científicas_de_datos
- Repositorio para módulo Científicas de datos 
- TSCD - ISPC
- Cohorte 2021

## Integrantes
- Karina Alem
- Florencia Bravo Corvalán
- Laura Martinez Quijano
- María Gimena Binaghi

### Objetivo del proyecto: 
poner en producción un proyecto de detección de spam. 

### Breve descripción: 
Se toma un dataset que posee informacion sobre mensajes que fueron fraude o no. La base se usó para crear un modelo de clasificacion con  una precisión de 0.91 y recall de 0.93 para la clase de interés(SPAM) y precisión de 0.99 y recall de 0.99 para la clase HAM.
En posterior se realizó la construcción de un frontend con HTML y CSS. Luego se desarrollo del lado del backend la estructura para llamar al modelo, realizar la predicción y mostrarlo en el front. Por último se realizaron distintos test para asegurar el correcto funcionamiento.

### Instrucciones para poner en marcha (deploy) el modelo
Se encuentran en un documento con imágenes ilustrativas en la carpeta "documentation".

### Problemas y dificultades encontradas:
Los primeros issues que definimos fueron tentativos, antes de definir sobre qué modelo trabajaríamos. Cuando identificamos al modelo de detección de spam, surgieron más espontáneamente las tareas y su asignación en el grupo.
Los primeros sprints que definimos (uno por semana) nos quedaron cortos porque hubo varias redefiniciones a medida que avanzábamos con el trabajo, por lo que los desplazamos en el tiempo y reordenamos las issues.
Al verificar la funcionalidad del back end encontramos conflictos con la versión de Python y de las librerías que resolvimos creando un entorno virtual.
Al desarrollar el front end nos encontramos con el desafío de investigar como conectar back con front. Decidimos hacerlo con Flask y desarrollamos el front con HTML dandole estilos con CSS.
Después nos encontramos con el desafío de dónde subir la aplicación Flask creada, y encontramos pythonanywhere.com.
Luego de entender cómo se estructura un repo, re-estructuramos lo que habíamos hecho originalmente en las carpetas sugeridas , y creamos branches para subir el trabajo de cada una de nosotras.
En la etapa de testing nos encontramos con el problema de que corre con paths locales o rutas estaticas pero no relativas. Corroborando que corre de manera local pero no al cambiar de pc.

### Link servidor: 
http://florcorvalan26.pythonanywhere.com/

# Para levantar la aplicación:

En Linux:

sudo apt install python3-venv

Crear un entorno virtual nuevo:  python3 -m venv my-project-env

Activar un entorno virtual: source my-project-env/bin/activate

En Windows:

Crear un entorno virtual nuevo: python -m venv c:\ruta\al\entorno\virtual

Activar un entorno virtual: c:\ruta\al\entorno\virtual\scripts\activate.bat

---------------------------------------------------------------------------------------
Instalar librerias correpondientes:

pip install flask

Despues de instalar CTRL+SHIFT+P y buscar Python Interpreter 
![imagen](https://github.com/gibinaghi/cientificas_de_datos/assets/67662395/7d8aceb8-f074-436f-b3ef-501a23448e8f)

Seleccionar el entorno virtual my-project-env que se creo en el paso anterior
![imagen](https://github.com/gibinaghi/cientificas_de_datos/assets/67662395/57334731-f9e7-4253-bc6c-80ffe7569c2c)

Luego pararse en la carpeta donde esta el archivo requirements.txt y para instalar las librerias ejecutar lo siguiente:
pip install -r requirements.txt

Por ultimo configurar los siguientes paths:
![imagen](https://github.com/gibinaghi/cientificas_de_datos/assets/67662395/5b875ade-ffbf-43bf-b111-c594a674581d)
![imagen](https://github.com/gibinaghi/cientificas_de_datos/assets/67662395/61c648e3-8e99-444e-ac7a-a3a63e782d67)
