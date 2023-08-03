"""
URL configuration for WebsiteCoreLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

from django.contrib import admin
from django.urls import path
import sys

from IndexProcesser import views_main
from NovartisProcesser import views_text
from PaddleProcesser import views_figure
from CSVProcesser import views_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_main.index),
    path('text/', views_text.PatientSelection.text),
    path('text/extraction/', views_text.PatientSelection.extraction),
    path('text/normalization/', views_text.PatientSelection.normalization),
    path('text/generation/', views_text.PatientSelection.generation),
    path('figure/', views_figure.FigureClassification.figure),
    path('figure/read/', views_figure.FigureClassification.read),
    path('csv/', views_csv.CSVHandler.csv),
    path('csv/read/', views_csv.CSVHandler.read),
    path('csv/desensitization/', views_csv.CSVHandler.desensitization),
]
