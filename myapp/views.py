from django.http import HttpResponse, JsonResponse
import sqlite3
import requests


def index(request):
    f = open("index.html", "r", encoding="utf8")
    texto = f.read()
    f.close()
    return HttpResponse(texto)


def acerca_de(request):
    return HttpResponse("¡Curso de Python y Django!")


def cursos(request):
    conn = sqlite3.connect("cursos.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM curso")
    html = """
    <html>
    <title>Lista de cursos</title>
    <table style="border: 1px solid">
    <thead>
    <tr>
    <th>Curso</th>
    <th>Inscriptos</th>
    </tr>
    </thead>
    """
    for (nombre, inscriptos) in cursor.fetchall():  # [("JAVA",8),("PYTHON",10),("PHP",12)]
        html += f"""
        <tr>
        <td> { nombre } </td>
        <td> { inscriptos } </td>
        </tr>
        """
    html += "</table></html>"
    conn.close()
    return HttpResponse(html)


def dolar_visto(request):
    try:
        r = requests.get(
            "https://www.dolarsi.com/api/api.php?type=valoresprincipales")
        d = r.json()
        compra = d[0]["casa"]["compra"]
        venta = d[0]["casa"]["venta"]
    except:
        r = requests.get("http://www.bna.com.ar/Cotizador/MonedasHistorico")
        texto = r.text
        compra = texto[491:499]
        venta = texto[539:547]
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Precio dolar</title>
    </head>
    <body>
    <H1>Valor principal Dolar</H1>
    <h2> <strong>Dolar compra:</strong>{compra}</h2>
    <h2> <strong>Dolar venta:</strong>{venta}</h2>
    </body>
    </html>
    """
    return HttpResponse(html)


def servicio_dolar(request):
    r = requests.get(
        "https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    d = r.json()
    compra = d[0]["casa"]["compra"]
    venta = d[0]["casa"]["venta"]
    return JsonResponse({"Compra": compra, "Venta": venta})


def aeropuertos(request):
    f = open("aeropuertos.csv", encoding="utf8")
    data = f.readlines()
    f.close()
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tp2</title>
    <body>
    <table>
    <tr>
    <td>Aeropuerto</td>
    <td>Ciudad</td>
    <td>Pais</td>
    </tr>
    """
    for renglon in data:
        # print(renglon)
        lista = renglon.split(",")
        # print(lista)
        a = lista[1].replace('"', '')
        c = lista[2].replace('"', '')
        p = lista[3].replace('"', '')
        html += f"""
        <tr>
        <td>{a}</td>
        <td>{c}</td>
        <td>{p}</td>
        </tr>
        """
    html += """
        </table>
        </body>
        </html>
    """
    return HttpResponse(html)


def servicio_aeropuertos(request):
    f = open("aeropuertos.csv", encoding="utf8")
    data = f.readlines()
    f.close()
    info = []
    for renglon in data:
        lista = renglon.split(",")
        a = lista[1].replace('"', '')
        c = lista[2].replace('"', '')
        p = lista[3].replace('"', '')
        d = {"nombre": a, "ciudad": c, "pais": p}
        info.append(d)
    return JsonResponse(info, safe=False)


