from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
app = Flask(__name__)
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.form.get('Body', '').lower()
    resp = MessagingResponse()
    
    if "hola" in msg or "menu" in msg:
        resp.message("""Hola! 👋 Bienvenido a Las recetas de la nona

Escribí el número:
1. Ver menú completo
2. Ñoquis - receta completa
3. Pastas caseras - receta completa  
4. Empanadas - receta completa
5. Historia de la nona
6. Precios
7. Comprar ahora
8. Dejar mi número para novedades""")
    
    elif "1" in msg or "menu" in msg:
        resp.message("""Menú de Las recetas de la nona 🍽️

Ñoquis
Pastas caseras
Empanadas
Guisos
Tarta
Puré
Papas
Pizza
Ensaladas
Y muchas más...

Solo Ñoquis, Pastas y Empanadas tienen receta completa acá.""")
    
    elif "2" in msg or "ñoquis" in msg:
        resp.message("""Ñoquis de la nona 🥟

Ingredientes:
- 1 kg papas
- 300g harina 0000
- 1 huevo
- Sal y nuez moscada

Paso a paso:
1. Hervir papas con cáscara hasta que estén tiernas
2. Pelar y hacer puré bien seco
3. Agregar harina, huevo, sal y nuez moscada
4. Formar masa sin amasar mucho
5. Hacer rollitos y cortar los ñoquis
6. Hervir en agua con sal hasta que floten
7. Servir con salsa a gusto

¿Querés la historia? Escribí 'historia ñoquis'""")
    
    elif "historia ñoquis" in msg:
        resp.message("""Historia de los ñoquis 💛

Los domingos en casa de la nona se comían los ñoquis. 
'Dijo el más chiquito' y desde ahí se volvió tradición.

Ese olor a salsa y familia es lo que queremos que pruebes.""")
    
    elif "3" in msg or "pastas" in msg or "fideos" in msg:
        resp.message("""Pastas caseras de la nona 🍝

Ingredientes:
- 400g harina 0000
- 4 huevos
- Pizca de sal
- 1 cda aceite

Paso a paso:
1. Hacer corona con harina, poner huevos, sal y aceite en el centro
2. Mezclar de adentro hacia afuera hasta formar masa
3. Amasar 10 min hasta que quede lisa y elástica
4. Dejar reposar tapada 30 min
5. Estirar bien finita
6. Cortar en tiras y hervir 4-5 min
7. Escurrir y servir con salsa""")
    
    elif "4" in msg or "empanadas" in msg:
        resp.message("""Empanadas de la nona 🥟

Ingredientes masa:
- 500g harina 0000
- 100g grasa o manteca
- 250ml agua tibia
- 1 cdita sal

Ingredientes relleno:
- 500g carne picada
- 2 cebollas
- 1 morrón
- Condimentos: sal, pimienta, comino, pimentón

Paso a paso:
1. Hacer masa y dejar reposar 30 min
2. Sofreír cebolla, morrón y carne con condimentos
3. Dejar enfriar el relleno
4. Armar las empanadas y repulgar
5. Hornear 20 min a 200°C hasta dorar""")
    
    elif "5" in msg or "historia" in msg:
        resp.message("""La historia de la nona 💛

Todo empezó en la cocina de la nona, donde cada domingo 
era una excusa para juntarse en familia alrededor de la mesa.

Sus recetas pasaron de generación en generación. 
Ahora queremos compartir ese sabor de casa con vos.""")
    
    elif "6" in msg or "precio" in msg or "cuanto" in msg:
        resp.message("""Precios Las recetas de la nona

Mensual: $8.000
Anual: $72.000

Escribí 'comprar' para suscribirte ahora.""")
    
    elif "7" in msg or "comprar" in msg:
        resp.message("""Comprar Las recetas de la nona 🛒

Mensual: $8.000
Anual: $72.000

Para finalizar tu compra escribí tu nombre completo y mail. 
Te enviamos el link de pago al toque.

Ejemplo: Juan Pérez, juan@mail.com""")
    
    elif "8" in msg or "numero" in msg or "novedades" in msg or "telefono" in msg:
        resp.message("""Perfecto! 📱 

Dejame tu número con código de área y te mandamos recetas nuevas y promociones por WhatsApp.

Escribí solo el número. Ejemplo: 1123456789""")
    
    else:
        # Guardar número si el mensaje parece ser un teléfono
        if msg.isdigit() and len(msg) >= 8:
            resp.message("Gracias! 🙌 Guardamos tu número. Pronto te mandamos recetas y novedades de la nona.")
        # Guardar datos de compra si tiene @
        elif "@" in msg and "," in msg:
            resp.message("Genial! Recibimos tus datos. En las próximas horas te mandamos el link de pago para activar tu suscripción.")
        else:
            resp.message("No entendí 🤔 Escribí 'menu' para ver las opciones.")
    
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.envieron,get("PORT",5000)), debug=True)
