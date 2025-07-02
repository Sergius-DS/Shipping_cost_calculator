# Shipping_cost_calculator

Este script es una aplicación gráfica en Python que calcula el costo de envío basado en diferentes planes de envío y el peso del paquete ingresado por el usuario. Utiliza la biblioteca tkinter para crear la interfaz gráfica y ttkbootstrap para mejorar el aspecto visual con temas modernos.

# GitHub Actions:

Este flujo de trabajo de GitHub Actions, llamado **"Lint and Format"**, revisa automáticamente el estilo y los errores del código Python al enviar y extraer solicitudes a la rama principal. Verifica el formato del código con Black y realiza comprobaciones de calidad con Flake8, incluyendo errores de sintaxis, sangría, importaciones no utilizadas, nombres indefinidos y complejidad del código (máximo 10). También establece una longitud máxima de línea de 79 caracteres para mantener la coherencia de los estándares de codificación.

## Clases para modelar planes y tarifas de envío:

WeightTier: Representa un rango de peso y su precio por libra.

ShippingPlan: Representa un plan de envío, incluyendo el nombre de la compañía y servicio, las tarifas por peso, y posibles cargos fijos o planos. Tiene un método calc_cost() que calcula el costo total basado en el peso proporcionado.

## Planes de envío definidos:

ground: Envío terrestre con diferentes tarifas según el peso y un cargo fijo de $20.

premium: Envío terrestre premium sin tarifas por peso, solo un cargo fijo de $125.

avion_basic: Envío por avión con tarifas diferenciadas, sin cargo fijo.

## Interfaz gráfica (ShippingApp):

Tiene una ventana principal con un tema oscuro (darkly).
Entrada para que el usuario ingrese el peso del paquete.

Dos botones:

"Calculate Cheapest": calcula y muestra la opción de envío más económica.

"Clear": limpia los campos y resultados.

Área de texto (no ttkbootstrap) para mostrar los resultados, incluyendo:
La opción de envío más barata.

Todos los planes de envío y sus costos correspondientes.

## Funcionalidad principal:

Cuando el usuario hace clic en "Calculate Cheapest", la aplicación:

Toma el peso ingresado y valida que sea un número positivo.

Calcula el costo de envío para cada plan.

Ordena los planes por costo y muestra el más barato.

También muestra los costos de todos los planes para comparación.

La opción "Clear" reinicia los campos y limpia los resultados.

---

## 🔬 Tecnologías Clave

*   **Python**
*   **Tkinter**
