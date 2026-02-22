🗺 MAP – Módulo 08: The Matrix
Entornos, Dependencias y Configuración en Python
🎯 Propósito del módulo

Este módulo no trata de algoritmia.

Trata de mentalidad profesional.

Introduce los pilares fundamentales para construir aplicaciones Python reales:

Aislamiento de entornos (venv)

Gestión reproducible de dependencias (pip / Poetry)

Separación entre código y configuración

Seguridad básica en proyectos

Disciplina estructural

Es el punto de transición entre:

“Escribir scripts” → “Diseñar aplicaciones mantenibles”

🧩 EX00 – Virtual Environment Detection
🧠 Qué hace realmente

Detecta si el intérprete actual está ejecutándose dentro de un entorno virtual aislado.

No solo imprime un mensaje:
Demuestra comprensión del funcionamiento interno de Python.

🔎 Conceptos clave

sys.prefix vs sys.base_prefix

Cómo Python determina el entorno activo

Diferencia entre entorno global y entorno virtual

Localización de site-packages

Qué significa realmente “aislar” dependencias

🎯 Por qué importa

Sin aislamiento:

Las dependencias se mezclan

Las versiones entran en conflicto

Se rompe la reproducibilidad

El entorno global se contamina

Un entorno virtual no es opcional en desarrollo profesional.

📦 EX01 – Dependency Management
🧠 Qué hace realmente

Valida que el entorno tenga instaladas las librerías necesarias antes de ejecutar lógica.

No asume.
Verifica.

Simula un pequeño procesamiento de datos para demostrar que:

Las dependencias funcionan

El entorno está correctamente configurado

🔎 Conceptos clave

requirements.txt vs pyproject.toml

Resolución de dependencias

Importación dinámica (importlib)

Manejo elegante de dependencias faltantes

No-crash behavior

Reproducibilidad

🎯 Por qué importa

Un proyecto profesional debe:

Poder instalarse en otra máquina

Tener dependencias controladas

Evitar errores en tiempo de ejecución

Ser predecible

La reproducibilidad no es comodidad.
Es ingeniería.

🔐 EX02 – Environment Configuration
🧠 Qué hace realmente

Carga configuración desde variables de entorno.

Demuestra separación entre:

Código

Configuración

Secretos

🔎 Conceptos clave

Uso de .env.example

python-dotenv

Variables obligatorias

Valores por defecto

Enmascarado de secretos

Validación segura

Salida controlada ante errores

🎯 Por qué importa

En desarrollo real:

Las credenciales no van en el código

La configuración cambia según entorno

La seguridad es responsabilidad del desarrollador

Los secretos no se suben a Git

Separar configuración de lógica es arquitectura básica.

🧠 Aprendizajes estructurales del módulo

Este módulo enseña:

Pensar en entornos antes que en código

Construir proyectos reproducibles

Diseñar con mentalidad backend

Validar antes de ejecutar

Prevenir antes que corregir

No trata de complejidad.
Trata de disciplina.

🧭 Conexión con el mundo real

Estos conceptos son la base de:

Django

Flask

Docker

Microservicios

CI/CD

Deploy en producción

Infraestructura cloud

Sin control del entorno, nada escala.

🏁 Conclusión conceptual

Este módulo marca un cambio mental:

De programadora que ejecuta código
a desarrolladora que diseña entornos.

La ingeniería empieza antes del main().
