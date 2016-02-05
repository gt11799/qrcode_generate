#! coding=utf-8
import qrcode
import cStringIO
from flask import Flask, request, Response
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route("/")
def qr_code():
    data = request.args.get('data')
    if not data:
        return "<p>not found</p>"
    qr = qrcode.QRCode(
        version=3,
        box_size=20,
        border=3,
    )
    qr.add_data(data)
    img = qr.make_image()
    temp = cStringIO.StringIO()
    img.save(temp, 'png')

    return Response(temp.getvalue(), mimetype="image/png")


if __name__ == '__main__':
    app.run("0.0.0.0", port=9000)
