# protobuf-definitions

Este repositorio contiene definiciones de mensajes protobuf utilizados en nuestros servicios.

## Archivos

- `messages.proto`: Definiciones de mensajes para la comunicación entre servicios.
- `services.proto`: Definiciones de mensajes relacionados con los servicios.

## Script de Automatización

Hemos creado un script de Python (`update_identifiers.py`) para automatizar la numeración de identificadores en los archivos `.proto`.

### Uso del Script

1. Clona el repositorio.
2. Navega al directorio del repositorio.
3. Ejecuta el script:

```bash
python3 update_identifiers.py
