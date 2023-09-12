from django.contrib import admin
from .models import *
from .form import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','image', 'age', 'phone_number', 'area', 'district', 'state', 'nation','rating','time','currency')
    
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Banner)
admin.site.register(Nation)
admin.site.register(District)
admin.site.register(State)
admin.site.register(Post)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('get_user_username','get_post_titles','created_at' )
    
    def get_post_titles(self, obj):
        return ", ".join([post.name for post in obj.post.all()])
    get_post_titles.short_description = 'Post Titles'
    
    def get_user_username(self, obj):
        return obj.user.username
    get_user_username.short_description = 'User Username'

admin.site.register(Booking, BookingAdmin)
admin.site.register(UserRating)