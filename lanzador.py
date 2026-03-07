import os
import sys
import streamlit.web.cli as stcli

def resolver_ruta(ruta):
    if getattr(sys, 'frozen', False):
        ruta_resuelta = os.path.abspath(os.path.join(sys._MEIPASS, ruta))
    else:
        ruta_resuelta = os.path.abspath(os.path.join(os.getcwd(), ruta))
    return ruta_resuelta

if __name__ == "__main__":
    # Simulamos que el usuario escribió "streamlit run app.py" en la terminal
    sys.argv = ["streamlit", "run", resolver_ruta("app.py"), "--global.developmentMode=false"]
    
    # Ejecutamos Streamlit
    sys.exit(stcli.main())ß