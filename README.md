GENERADOR DE CONTRASEÑAS SEGURAS MEJORADO
=====================================

Materia: Lógica de Programación
Proyecto Integrador: El impacto de las nuevas tecnologías en la sociedad: visualización del futuro
Fecha: 01/03/2025

-------------------------------------
DESCRIPCIÓN
-------------------------------------
Este programa permite generar contraseñas seguras de forma personalizada desde la consola.
El usuario puede elegir la longitud, si incluir mayúsculas, números y símbolos, y el programa
evalúa qué tan segura es la contraseña generada. También guarda un historial de todas las
contraseñas creadas durante la sesión.

El proyecto fue desarrollado como parte del curso de Lógica de Programación, integrando
los conocimientos de las 4 unidades de la materia.

-------------------------------------
OBJETIVO DEL PROGRAMA
-------------------------------------
Demostrar que la programación puede resolver problemas reales de seguridad digital.
Las contraseñas débiles son una de las principales vulnerabilidades en internet; este programa
ayuda a los usuarios a generar contraseñas fuertes de manera sencilla, aplicando conceptos
fundamentales de programación en Python

-------------------------------------
FUNCIONALIDADES PRINCIPALES
-------------------------------------
- Generar contraseña: crea una contraseña aleatoria con los parámetros elegidos por el usuario
- Elegir longitud: el usuario decide cuántos caracteres tendrá la contraseña (mínimo 8, máximo 30)
- Personalizar caracteres: opción de incluir mayúsculas, números y/o símbolos
- Evaluar seguridad: el programa califica la contraseña como DÉBIL, MEDIA o FUERTE
- Historial: guarda todas las contraseñas generadas en la sesión con su número y nivel de seguridad
- Menú interactivo: interfaz de consola con opciones numeradas, fácil de usar

-------------------------------------
CONTENIDOS DE LA MATERIA APLICADOS
-------------------------------------

UNIDAD 1 — Introducción a la Resolución de Problemas
  - Problema identificado: las contraseñas débiles exponen cuentas a ataques
  - Pasos para resolver el problema: definir requisitos, diseñar algoritmo, implementar en Python
  - Entorno de desarrollo: Python 3 + VS Code

UNIDAD 2 — Manejo de Datos, Algoritmos y Diagramas de Flujo
  - Variables de distintos tipos: str, int, bool, dict
  - Algoritmo documentado paso a paso antes de codificar
  - Diagrama de flujo del programa completo

UNIDAD 3 — Lógica de Programación
  - Condicionales if, elif, else para validaciones y menú
  - Operadores relacionales (>=, <=, ==) y lógicos (or)
  - Ciclo while para el menú principal y validación de entrada
  - Ciclo for para construir la contraseña carácter por carácter
  - Alterador de ciclo: seguir = False para salir del while

UNIDAD 4 — Estructuras de Datos y Funciones
  - Tuplas: LETRAS_MINUSCULAS, LETRAS_MAYUSCULAS, NUMEROS, SIMBOLOS (datos inmutables)
  - Listas: caracteres_disponibles, contrasena_lista (construcción dinámica)
  - Diccionarios: historial{} para el registro, opciones{} para la configuración
  - Funciones con parámetros y retorno:
      mostrar_menu()
      pedir_longitud()                         retorna: int
      pedir_opciones()                         retorna: dict
      generar_contrasena(longitud, opciones)   retorna: str
      evaluar_seguridad(contrasena, opciones)  retorna: str
      guardar_en_historial(contrasena, longitud, nivel)
      mostrar_historial()

-------------------------------------
CÓMO EJECUTAR EL PROGRAMA
-------------------------------------
Requisitos: Python 3 instalado
-------------------------------------
EJEMPLO DE USO
-------------------------------------
Bienvenido al Generador de Contraseñas Seguras

========================================
   GENERADOR DE CONTRASENAS SEGURAS
========================================
1. Generar una nueva contrasena
2. Ver historial de contrasenas
3. Salir
========================================

Elige una opcion (1, 2 o 3): 1
Que longitud quieres para tu contrasena? (minimo 8, maximo 30): 16
Incluir MAYUSCULAS? (s/n): s
Incluir NUMEROS? (s/n): s
Incluir SIMBOLOS (!@#...)? (s/n): s

========================================
  Tu contrasena generada es:
  gT3!mK#9pLw@Xn2&
  Nivel de seguridad: FUERTE
========================================

-------------------------------------
DATOS DEL GRUPO
-------------------------------------
Nombres:      Daniel Villanueva
Materia:      Lógica de Programación
Universidad:  UIDE
Semestre:     Primero
Año:          2025

Proyecto desarrollado como parte del curso de Lógica de Programación — UIDE 2026
