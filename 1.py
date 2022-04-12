import qrcode

img = qrcode.make("https://www.youtube.com/channel/UCeO7v5cq_hoalGUjXTkN8RQ")
img.save("qrimage.jpg")




