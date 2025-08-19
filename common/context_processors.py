# from django.db import models


# def common_context(request):
#     if request.user.is_authenticated:
#         cart_items = CartItem.objects.filter(cart=request.user.cart).annotate(
#             total_amount=models.F("quantity") * models.F("product__price")
#         )
#         total_amount = sum(item.total_amount for item in cart_items)

#         cart_items_count = request.user.cart.cart_items.count()

#         return {
#             "site_name": "VooCommerce",
#             "is_user_authenticated": request.user.is_authenticated,
#             "user_cart_items_count": cart_items_count,
#             "cart_total_amount": total_amount // 100,
#         }

#     return {
#         "site_name": "VooCommerce",
#         "is_user_authenticated": request.user.is_authenticated,
#     }
