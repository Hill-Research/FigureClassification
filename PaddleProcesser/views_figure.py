#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA  02110-1301, USA.

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from WebsiteCoreLibrary.settings import MEDIA_URL
import uuid
from paddleocr import PaddleOCR, draw_ocr
import os

# Create your views here.

class FigureClassification:
    @classmethod
    def figure(cls, request):
        if request.method == "GET":
            cls.ocr_english = PaddleOCR(use_angle_cls=True, lang="en")
            cls.ocr_chinese = PaddleOCR(use_angle_cls=True, lang="ch")
            return render(request, 'figure.html')

    @classmethod
    @csrf_exempt
    def read(cls, request):
        if request.method == 'POST':
            lang = request.POST.get('lang')
            print(lang)
            image = request.FILES.get('figure')
            file = FileSystemStorage(location = MEDIA_URL)
            upload_file_name = '{}.jpg'.format(str(uuid.uuid4()))
            file_path = file.save(upload_file_name,image)
            if(lang == 'Chinese'):
                result = cls.ocr_chinese.ocr(os.path.join(MEDIA_URL, file_path), cls=True)
            if(lang == 'English'):
                result = cls.ocr_english.ocr(os.path.join(MEDIA_URL, file_path), cls=True)
            names = ['Location', 'Name', 'Probability']
            body_items = list()
            for idx in range(len(result)):
                res = result[idx]
                for line in res:
                    body_items.append({'Location' : str(line[0]), 'Name' : str(line[1][0]), 'Probability' : str(line[1][1])})
            return JsonResponse({'head' : names, 'body' : body_items})
