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