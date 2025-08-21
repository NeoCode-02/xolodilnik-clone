from rest_framework import generics

from .models import (
    Discount,
    Order,
    OrderItem,
    ProductDiscount,
    Promocode,
    PromocodeUsage,
    Provider,
    Transaction,
)
from .permissions import IsAdminForWrite
from .serializers import (
    DiscountSerializer,
    OrderItemSerializer,
    OrderSerializer,
    ProductDiscountSerializer,
    PromocodeSerializer,
    PromocodeUsageSerializer,
    ProviderSerializer,
    TransactionSerializer,
)


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminForWrite,)


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminForWrite,)


class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAdminForWrite,)


class OrderItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAdminForWrite,)


class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAdminForWrite,)


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAdminForWrite,)


class ProviderListCreateView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = (IsAdminForWrite,)


class ProviderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = (IsAdminForWrite,)


class DiscountListCreateView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = (IsAdminForWrite,)


class DiscountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = (IsAdminForWrite,)


class ProductDiscountListCreateView(generics.ListCreateAPIView):
    queryset = ProductDiscount.objects.all()
    serializer_class = ProductDiscountSerializer
    permission_classes = (IsAdminForWrite,)


class ProductDiscountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductDiscount.objects.all()
    serializer_class = ProductDiscountSerializer
    permission_classes = (IsAdminForWrite,)


class PromocodeListCreateView(generics.ListCreateAPIView):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer
    permission_classes = (IsAdminForWrite,)


class PromocodeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer
    permission_classes = (IsAdminForWrite,)


class PromocodeUsageListCreateView(generics.ListCreateAPIView):
    queryset = PromocodeUsage.objects.all()
    serializer_class = PromocodeUsageSerializer
    permission_classes = (IsAdminForWrite,)


class PromocodeUsageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PromocodeUsage.objects.all()
    serializer_class = PromocodeUsageSerializer
    permission_classes = (IsAdminForWrite,)
