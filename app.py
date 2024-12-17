from flask import Flask, Response, render_template, request
from qr_schematic import QrSchematic

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download_schematic():
    url = request.args.get('url')
    qrschem = QrSchematic()
    schematic_data = qrschem.generate_qr_structure(url)

    return Response(
        schematic_data,
        mimetype="application/octet-stream",
        headers={
            "Content-Disposition": "attachment;filename=qr_schematic.schem"
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
