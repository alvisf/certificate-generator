import pdfkit

import os
working_directory = os.path.abspath(os.getcwd())


def gen_pdf():

    body = """
    <html>
      <head>
        <meta name="pdfkit-page-size" content="Legal"/>
        <meta name="pdfkit-orientation" content="Landscape"/>
      </head>
      Hello World!
      </html>
    """
    pdfkit.from_string(body,
                       ''+working_directory+'/app/main/view/static/downloads/out.pdf')
