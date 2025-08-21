from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sponsor
from .serializers import SponsorSerializer


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def blog_single(request):
    return render(request, "blog-single.html")


def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")


def shop(request):
    return render(request, "shop.html")


def single_product(request):
    return render(request, "single_product.html")


def wishlist(request):
    return render(request, "wishlist.html")


class SponsorListAPIView(APIView):
    def get(self, request):
        sponsors = Sponsor.objects.all()
        return Response(SponsorSerializer(sponsors, many=True).data)


class SponsorDetailAPIView(APIView):
    def get(self, request, pk):
        sponsor = Sponsor.objects.get(pk=pk)
        return Response(SponsorSerializer(sponsor).data)


class SponsorCreateAPIView(APIView):
    def post(self, request):
        sponsor = Sponsor.objects.create(**request.data)
        return Response(SponsorSerializer(sponsor).data)


class SponsorUpdateAPIView(APIView):
    def put(self, request, pk):
        sponsor = Sponsor.objects.get(pk=pk)
        sponsor.name = request.data.get("name")
        sponsor.logo = request.data.get("logo")
        sponsor.save()
        return Response(SponsorSerializer(sponsor).data)


class SponsorDeleteAPIView(APIView):
    def delete(self, request, pk):
        sponsor = Sponsor.objects.get(pk=pk)
        sponsor.delete()
        return Response({"message": "Sponsor deleted"})
