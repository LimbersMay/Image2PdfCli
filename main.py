from conversion import PngToJpg, ImgToPdf


def main():
    # Determinamos las rutas tan origen como destino
    ruta_origen = "numeracion/"
    ruta_destino = "convertido/"

    # Creamos los respectivos objetos
    convertir_png = PngToJpg(ruta_origen, ruta_destino)
    convertir_png.realizar_conversion()

    convertir_pdf = ImgToPdf(ruta_origen, ruta_destino)
    convertir_pdf.convertir_unido()


if __name__ == "__main__":
    main()
