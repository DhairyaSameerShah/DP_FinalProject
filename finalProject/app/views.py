from django.shortcuts import render
from .models import Data
import requests
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialization import SerializationClass
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


# Create your views here.

# getting data from url
# response = requests.get("https://drive.google.com/file/d/1nZQOU8MMgL2mP-TClB1Tleii71z1CF6S/view?usp=sharing")


def index(request):
    # deleting all file from the directory.
    # if os.path.exists("../finalProject/app/dataset/data.zip"):
    #     os.remove("../finalProject/app/dataset/data.zip")
    #     os.remove("../finalProject/app/dataset/Auto_data.csv")
    # else:
    #     print("The file does not exist")

    Data.objects.all().delete()

    # downloading file
    # with open('../finalProject/app/dataset/data.zip', 'wb') as f:
    #     f.write(response.content)

    # extracting file
    # with zipfile.ZipFile('../finalProject/app/dataset/data.zip', 'r') as data_zip:
    #     data_zip.extractall('../finalProject/app/dataset')

    # reading and importing csv file in database.
    df = pd.read_csv('../finalProject/app/dataset/Auto_data.csv')
    number_of_rows = df.shape
    for i in range(number_of_rows[0]):
        Data.objects.create(Row_ID=df.row_id[i], Symboling=df.symboling[i], Normalized_Losses=df.normalized_losses[i],
                            Make=df.make[i], Num_of_Doors=df.num_of_doors[i], Body_Style=df.body_style[i],
                            Drive_Wheels=df.drive_wheels[i],
                            Engine_Location=df.engine_location[i], Wheel_Base=df.wheel_base[i], Length=df.length[i],
                            Width=df.width[i], Height=df.height[i], Curb_Weight=df.curb_weight[i],
                            Engine_Type=df.engine_type[i], Num_of_Cylinders=df.num_of_cylinders[i],
                            Engine_Size=df.engine_size[i], Fuel_System=df.fuel_system[i], Bore=df.bore[i],
                            Stroke=df.stroke[i], Compression_Ratio=df.compression_ratio[i],
                            Horsepower=df.horsepower[i],
                            Peak_rpm=df.peak_rpm[i], City_mpg=df.city_mpg[i], Highway_mpg=df.highway_mpg[i],
                            Price=df.price[i], Horsepower_Binned=df.horsepower_binned[i], Diesel=df.diesel[i],
                            Gas=df.gas[i], Normal=df.normal[i], Turbo=df.turbo[i])
    get_table = requests.get('http://127.0.0.1:8000/get_api')
    return render(request, 'index.html', {'index_data': get_table})


def spreadsheet(request):
    show_all = requests.get('http://127.0.0.1:8000/get_api')
    spreadsheet_results = show_all.json()
    return render(request, 'spreadsheet.html', {'spreadsheet_data': spreadsheet_results})


def bonus(request):
    show_all = requests.get('http://127.0.0.1:8000/get_api')
    bonus_results = show_all.json()
    return render(request, 'bonus.html', {'spreadsheet_data': bonus_results})


@api_view(['GET'])
def get_api(request):
    if request.method == 'GET':
        show_all = Data.objects.all()
        serialize = SerializationClass(show_all, many=True)
        json = JSONRenderer().render(serialize.data)
        stream = io.BytesIO(json)
        data = JSONParser().parse(stream)
        return Response(data)
    # return render(request, 'bonus.html', {'data': show_all})


@api_view(['GET'])
def get_id(request, item_id=1):
    final_data = {}
    if request.method == 'GET':
        show_all = Data.objects.all()
        serialize = SerializationClass(show_all, many=True)
        json = JSONRenderer().render(serialize.data)
        stream = io.BytesIO(json)
        data = JSONParser().parse(stream)
        for i in data:
            if i['Row_ID'] == item_id:
                print(i)
                final_data = i
        return Response(final_data)
