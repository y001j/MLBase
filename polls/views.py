import base64
from io import BytesIO

from django.http import HttpResponse
import matplotlib.pyplot as plt
from django.shortcuts import render
from numpy.random import randn


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_picture(request):
    plt.plot(randn(50).cumsum(), 'k--')
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    imb = base64.b64encode(plot_data)  # 对plot_data进行编码
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    context = {
        'img': imd,
    }
    return render(request, 'test.html', context)

