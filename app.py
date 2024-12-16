from flask import Flask, Response
from qr_schematic import QrSchematic

app = Flask(__name__)

@app.route('/download')
def download_schematic():
    url = ''
    qrschem = QrSchematic()
    schematic_data = qrschem.generate_qr_structure(url)

    return Response(
        schematic_data,
        mimetype="application/octet-stream",
        headers={
            "Content-Disposition": "attachment;filename=rickroll.schem"
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
