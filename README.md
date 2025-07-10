# Mi Aplicación Kivy

Una aplicación simple creada con Kivy que se compila automáticamente para Android usando GitHub Actions.

## Características

- Interfaz simple con botones
- Funcionalidad de saludo personalizado
- Compilación automática para Android

## Archivos

- `main.py` - Código principal de la aplicación
- `buildozer.spec` - Configuración para compilar el APK
- `.github/workflows/build-apk.yml` - Workflow de GitHub Actions

## Cómo funciona

1. Cada vez que haces un push al repositorio
2. GitHub Actions compila automáticamente el APK
3. El APK se puede descargar desde la pestaña "Actions"

## Instalación

1. Clona este repositorio
2. El APK se compilará automáticamente
3. Descarga el APK desde GitHub Actions

## Desarrollo

Para probar la aplicación localmente:

```bash
python main.py
```
