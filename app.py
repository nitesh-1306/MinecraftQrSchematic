from flask import Flask, Response, render_template, request
from link_shortner import LinkShortner
from qr_schematic import QrSchematic

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download_schematic():
    url = request.args.get('url')

    shortner = LinkShortner()
    short_link = shortner.short_url(url)

    qrschem = QrSchematic()
    schematic_data = qrschem.generate_qr_structure(short_link)

    return Response(
        schematic_data,
        mimetype="application/octet-stream",
        headers={
            "Content-Disposition": "attachment;filename=qr_schematic.schem"
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
