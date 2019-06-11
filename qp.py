import pyqrcode
import png

def toQRcode(data, format='png', scale=4):
    qr = pyqrcode.create(data)
    if format == 'png':
        qr.png('{}.png'.format(data), scale=scale)
    elif format == 'svg':
        qr.svg('{}.svg'.format(data), scale=scale)


def tocoloredQRcode(data, background, format='png', scale=4):
    qr = pyqrcode.create(data)
    if format == 'png':
        qr.png('{}-colored.png'.format(data), scale=scale, background=background)
    elif format == 'svg':
        qr.svg('{}-colored.svg'.format(data), scale=scale, background=background)


if __name__ == '__main__':
	
	text = 'wie ein Diamant'
	toQRcode(text)
	tocoloredQRcode(text, (24,25,26), (111,181,113))