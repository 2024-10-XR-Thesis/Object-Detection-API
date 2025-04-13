# Object Detection API
Esta API está dedicada a reconocer objetos dentro de una captura de pantalla tomada automáticamente al momento de hacer la petición.

## Instrucciones 
0. Configurar credenciales de Eden AI: [instrucciones](https://github.com/2024-10-XR-Thesis/.github/wiki/Instrucciones-Eden-AI).
1. Instalar los paquetes necesarios con `pip install -r requirements.txt` 
2. Correr la aplicación con `flask --app main run`
3. Hacer una petición de POST a la ruta <http://127.0.0.1:5000/detect> con un cuerpo vacío

Por si acaso, en la carpeta [/collections](https://github.com/2024-10-VR-Thesis/Object-Detection-API/tree/main/collections) se encuentra una colección de Postman que puede ser usada como guía.

## Información adicional
Esta app fue creada haciendo uso, principalmente, de las siguientes herramientas:

<img alt="flask logo" height="15" src="https://static-00.iconduck.com/assets.00/flask-icon-2048x1826-nxzeqh6a.png">  [Flask](https://flask.palletsprojects.com/en/3.0.x/) <br>
<img alt="pillow logo" height="15" src="https://raw.githubusercontent.com/2024-10-XR-Thesis/.github/refs/heads/main/assets/pillow_logo.png"> [Pillow](https://pypi.org/project/pillow/) <br>
<img alt="eden ai logo" height="15" src="https://raw.githubusercontent.com/2024-10-XR-Thesis/.github/refs/heads/main/assets/eden_AI_logo.png"> [Eden AI](https://www.edenai.co/) <br>
