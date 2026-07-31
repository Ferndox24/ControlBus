from urllib.parse import urlparse, parse_qs



def extraer_rut(texto):

    try:

        url = urlparse(texto)


        parametros = parse_qs(
            url.query
        )


        if "RUN" in parametros:

            return parametros["RUN"][0]


    except Exception as error:

        print(
            "Error leyendo QR:",
            error
        )


    return None