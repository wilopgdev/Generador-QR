"""
    Generador de códigos QR
    Version: 1.0
    Programa en mejora para generar un QR a partir de información suministrada
    Autor: wilopgdev
"""
# Imports
import qrcode
import os

# Colors
c_black = (0, 0, 0)
c_white = (255, 255, 255)


def main_menu():
    """
    Función que muestra el menú principal y deriva a las subfunciones
    """
    while True:
        os.system("cls")
        print("__________________________________________")
        print("Welcome to program \"QR generator\"")
        print("Created by wilopgdev")
        print("__________________________________________")
        print("[1] Create QR web address")
        print("[2] Create QR vCard")
        print("[0] Exit")
        try:
            option = int(input(" > "))
        except ValueError:
            print("\n\n\nError: unrecognized value\n\n\n")
            continue

        if option == 1:
            menu_qr_web()
        if option == 2:
            menu_qr_vcard()
        if option == 0:
            print("Come back soon!")
            break


def menu_qr_web():
    """
    Función que muestra el submenú de generar un QR de una web, recopila la información y la envía a la función generadora,
    si todo ha salido bien indica que se guardó el QR si no, informa de un error (pero no lo muestra)
    """
    os.system("cls")
    print("__________________________________________")
    print("Generador QR de dirección web")
    print("__________________________________________")
    url = input(
        "Por favor, introduce URL completa (ej: https://www.miweb.com/):\n(Dejar en blanco para volver atrás)\n > ")
    if url:
        if qr_web(url):
            input(
                "QR generado correctamente\nSe ha guardado en la ruta del script\n(Intro para continuar)")
        else:
            input("Error desconocido (Intro para continuar)")


def menu_qr_vcard():
    """
    Función que muestra el submenú de generar un QR de una vCard, recopila la información y la manda a la función generadora,
    si todo ha salido bien indica que se guardó el QR si no, informa de un error (pero no lo muestra)
    """
    data = ["", "", "", "", ""]
    items = ['"Nombre"', '"Apellidos"', '"Teléfono"', '"Email"',
             '"Url de web personal (ej: https://www.miweb.com/)"']
    os.system("cls")
    print("__________________________________________")
    print("Generador QR de vCard")
    print("__________________________________________")
    for i in range(len(items)):
        print("Por favor, introduce " + items[i] + ":")
        if i > 1:
            print("(Intro para dejar en blanco)")
            data[i] = input(" > ")
        else:
            print("(Deja en blanco para volver atrás)")
            data[i] = input(" > ")
            if not data[i]:
                return
    if qr_vcard(data):
        input("QR generado correctamente\nSe ha guardado en la ruta del script\n(Intro para continuar)")
    else:
        input("Error desconocido (Intro para continuar)")


def qr_web(url):
    """
    Fución encargada de generar y guardar el QR de la web generado a partir de la información recibida de la función
    \"menu_qr_web\", devuelve True si no ha habido errores, False en caso contrario.
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=8,
        )
        qr.add_data(url)
        img = qr.make_image(fill_color=c_black, back_color=c_white)
        img.save("QR_Web.png")
        return True
    except:
        return False


def qr_vcard(data):
    """
    Fución encargada de generar y guardar el QR de la vCard generado a partir de la información recibida de la función
    \"menu_qr_vcard\", devuelve True si no ha habido errores, False en caso contrario.
    """
    data_card = ["BEGIN:VCARD", "VERSION:3.0", "END:VCARD"]
    try:
        value = "N:" + data[1] + ";" + data[0] + ";;;"
        data_card.insert(2, value)
        value = "FN:" + data[0] + " " + data[1]
        data_card.insert(3, value)
        if data[2]:
            value = "TEL;TYPE=CELL,VOICE:" + data[2]
            data_card.insert(-1, value)
        if data[3]:
            value = "EMAIL;TYPE=HOME,PREF,INTERNET:" + data[3]
            data_card.insert(-1, value)
        if data[4]:
            value = "URL:" + data[4]
            data_card.insert(-1, value)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=5,
            border=14,
        )
        qr.add_data("\n".join(data_card))
        img = qr.make_image(fill_color=c_black,
                            back_color=c_white)
        img.save("QR_vCard.png")
        return True
    except:
        return False


# Lanzamos la aplicación
if __name__ == "__main__":
    main_menu()
