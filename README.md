## Instrucciones 
1. Instalar los paquetes necesarios con `pip install -r requirements.txt` 
2. Correr la aplicación con `flask --app main run`
3. Hacer una petición de POST a la ruta <http://127.0.0.1:5000/screenshot> con el siguiente cuerpo (ejemplo):
```json
{
    "screenshot_name": "screenshot"
}
```   

Esta app fue creada haciendo uso de [Flask](https://flask.palletsprojects.com/en/3.0.x/) <img alt="flask logo" height="15" src="https://static-00.iconduck.com/assets.00/flask-icon-2048x1826-nxzeqh6a.png"> y [Pillow](https://pypi.org/project/pillow/) <img alt="pillow logo" height="15" src="https://python-pillow.org/assets/images/pillow-logo-248x250.png">