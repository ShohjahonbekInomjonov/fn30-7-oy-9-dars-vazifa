from typing import Optional
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Car, Brand
from rest_framework import status
from .serializers import CarSerializer, BrandSerializer


class BrandAPIView(APIView):
    def get(self, request: Request, pk: Optional[int]=None):
        if not pk:
            brands = Brand.objects.all()
            serializer = BrandSerializer(brands, many=True)
            return Response(serializer.data)
        else:
            try:
                brand = Brand.objects.get(pk=pk)
                serializer = BrandSerializer(brand)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": "Brand Not Found !!!"}, status=status.HTTP_404_NOT_FOUND)

    
    def post(self, request: Request, pk: Optional[int]=None):
        if pk:
            return Response({"message": "Method POST Not Allowed!!!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer = BrandSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            brand = serializer.save()
            return Response(BrandSerializer(brand).data, status=status.HTTP_201_CREATED)
        
    
    def put(self, request: Request, pk: Optional[int]=None):
        if not pk:
            return Response({"message": f"Method {request.method} Not Allowed!!!"})
        else:
            try:
                brand = Brand.objects.get(pk=pk)
            except Exception as e:
                return Response({"message": "Brand Not Found!!!"}, status=status.HTTP_404_NOT_FOUND)
            serializer = BrandSerializer(instance=brand, data=request.data, partial=True if request.method == 'PATCH' else False)
            serializer.is_valid()
            brand = serializer.save()
            return Response(BrandSerializer(brand).data)
    
    def patch(self, request: Request, pk: Optional[int]=None):
        return self.put(request, pk)
    

    def delete(self, request: Request, pk: Optional[int]=None):
        if not pk:
            return Response({"message": "Brand Not Found!!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                brand = Brand.objects.get(pk=pk)
            except Exception as e:
                return Response({"message": "Brand Not Found!!!"}, status=status.HTTP_404_NOT_FOUND)
            brand.delete()
            return Response({"message": "Brand Successfully Deleted!!!"}, status=status.HTTP_204_NO_CONTENT)
            



class CarAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request: Request, pk: Optional[int]=None):
        if not pk:
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)
        else:
            try:
                car = Car.objects.get(pk=pk)
                serializer = CarSerializer(car)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": "Car Not Found !!!"}, status=status.HTTP_404_NOT_FOUND)
            

    def post(self, request: Request, pk: Optional[int]=None):
        if pk:
            return Response({"message": "Method POST Not Allowed!!!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer = CarSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            car = serializer.save()
            return Response(CarSerializer(car).data, status=status.HTTP_201_CREATED)
        
    
    def put(self, request: Request, pk: Optional[int]=None):
        if not pk:
            return Response({"message": f"Method {request.method} Not Allowed!!!"})
        else:
            try:
                car = Car.objects.get(pk=pk)
            except Exception as e:
                return Response({"message": "Car Not Found!!!"}, status=status.HTTP_404_NOT_FOUND)
            serializer = CarSerializer(instance=car, data=request.data, partial=True if request.method == 'PATCH' else False)
            serializer.is_valid()
            car = serializer.save()
            return Response(CarSerializer(car).data)
        
    
    def patch(self, request: Request, pk: Optional[int]=None):
        return self.put(request, pk)
    

    def delete(self, request: Request, pk: Optional[int]=None):
        if not pk:
            return Response({"message": "Car not Found !!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                car = Car.objects.get(pk=pk)
            except Exception as e:
                return Response({"message": "Car not Found !!!"}, status=status.HTTP_404_NOT_FOUND)
            car.delete()
            return Response({"message": "Car Successfully Deleted!!!"}, status=status.HTTP_204_NO_CONTENT)
