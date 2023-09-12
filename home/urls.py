from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',Home,name='home'),
  path('ajax/',FilterPost, name='ajax_view'),
  path('productfilter/',ProductFilter,name='productfilter'),
  path('product/<int:id>/',ProductDeatail,name='productDeatil'),
  path('searchproduct/',SearchProduct,name='searchproduct'),
  path('addtocart/',Add_To_cart,name='addtocart'),
  path('cart',Cart,name='cart'),
  path('application',UserBookings,name='application'),
  path('delete-cart/',Delete_cart,name='delete-cart'),
  path('user',user,name='user'),
  path('signup',Signup,name='signup'),
  path('update/',user_update,name='update'),
  path('login',Login,name='login'),
  path('logout',Logout,name='logout'),
  path('book/',Bookings,name='book'),
  

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
