# T1_AYD1_202307354

## Requisitos previos

- Python 3.10 o superior

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone <url-del-repositorio>
   cd T1_AYD1_202307354
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Iniciar el servidor con:

```bash
python main.py
```

El servidor quedará disponible en `http://localhost:8080`.

## Endpoints

| Método | Ruta               | Descripción                                          |
|--------|--------------------|------------------------------------------------------|
| GET    | `/`                | Mensaje de confirmación de que la API está activa.  |
| GET    | `/cancionFavorita` | Retorna el nombre, carnet y canción favorita.        |

## Ejemplos de uso

### Verificar el funcionamiento

```bash
http://localhost:8080/
```

Respuesta:

```json
{"mensaje": "API funcionando correctamente"}
```

### Obtener la canción favorita

```bash
http://localhost:8080/cancionFavorita
```

Respuesta:

```json
{
  "Nombre": "Hector Antonio Cardona Cos",
  "Carnet": "202307354",
  "Cancion_Favorita": "Sweet nothing"
}
```

## Documentación interactiva

FastAPI genera automáticamente documentación interactiva disponible mientras el servidor está en ejecución:

- Swagger UI: `http://localhost:8080/docs`
- ReDoc: `http://localhost:8080/redoc`
