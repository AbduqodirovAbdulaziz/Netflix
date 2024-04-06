from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class HelloApi(APIView):
    def get(self, request):
        data = {
            "message": "Hello world! Biz bugun rest_fremworkni boshladik"
        }
        return Response(data)


class AktyorlarApi(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializers(aktyorlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        aktyor = request.data
        serializers = AktyorSerializers(data=aktyor)
        if serializers.is_valid():
            data = serializers.validated_data
            Aktyor.objects.create(
                ism=data.get('ism'),
                t_sana=data.get('t_sana'),
                davlat=data.get('davlat'),
                jins=data.get('jins'),
            )
            return Response({'success': True, 'create_data': serializers.data})
        return Response({'success': False, 'errors': serializers.errors})


class AktyorApi(APIView):
    def get(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializers(aktyor)
        return Response(serializer.data)

    def put(self, request, pk):
        aktyor = Aktyor.objects.filter(id=pk)
        serializer = AktyorSerializers(aktyor.first(), data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            aktyor.update(
                ism=data.get('ism'),
                t_sana=data.get('t_sana'),
                davlat=data.get('davlat'),
                jins=data.get('jins'),
            )
            serializer = AktyorSerializers(aktyor.first())
            return Response({'sucsess': True, 'update_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})


class TarifApi(APIView):
    def get(self, request):
        tariflar = Tarif.objects.all()
        serializer = TarifSerializers(tariflar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TarifSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            Tarif.objects.create(
                nom=data.get('nom'),
                davomiyligi=data.get('davomiyligi'),
                narx=data.get('narx')
            )
            return Response({'success': True, 'created_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})


class TarifDeleteApi(APIView):
    def delete(self, request, pk):
        tarif = Tarif.objects.get(id=pk)
        tarif.delete()
        return Response({'success': True})


class TarifEditApi(APIView):
    def get(self, request, pk):
        tariflar = Tarif.objects.get(id=pk)
        serializer = TarifSerializers(tariflar)
        return Response(serializer.data)

    def put(self, request, pk):
        tarif = Tarif.objects.filter(id=pk)
        serializer = TarifSerializers(tarif.first(), data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            tarif.update(
                nom=data.get('nom'),
                davomiyligi=data.get('davomiyligi'),
                narx=data.get('narx')
            )
            return Response({'success': True, 'update_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})
