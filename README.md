# Object Detection API
Esta API está dedicada a reconocer objetos dentro de una captura de pantalla tomada automáticamente al momento de hacer la petición.

## Instrucciones 
0. Configurar credenciales de Eden AI: [instrucciones](https://github.com/2024-10-XR-Thesis/.github/wiki/Instrucciones-Eden-AI).
1. Instalar los paquetes necesarios con `pip install -r requirements.txt` 
2. Correr la aplicación con `flask --app main run`
3. Hacer una petición de POST a la ruta <http://127.0.0.1:5000/detect> con un cuerpo vacío

Por si acaso, en la carpeta [/collections](https://github.com/2024-10-VR-Thesis/Object-Detection-API/tree/main/collections) se encuentra una colección de Postman que puede ser usada para probar su uso.

## Información adicional
Esta app fue creada haciendo uso de las siguientes herramientas:

<img alt="flask logo" height="15" src="https://static-00.iconduck.com/assets.00/flask-icon-2048x1826-nxzeqh6a.png">  [Flask](https://flask.palletsprojects.com/en/3.0.x/) <br>
<img alt="pillow logo" height="15" src="https://python-pillow.org/assets/images/pillow-logo-248x250.png"> [Pillow](https://pypi.org/project/pillow/) <br>
<img alt="eden ai logo" height="15" src="https://media.dev.to/cdn-cgi/image/width=320,height=320,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F858514%2Fe693aabe-1ba7-4dcd-8391-16f4f1b27f1e.png"> [Eden AI](https://www.edenai.co/) <br>

Y demás librerías...
