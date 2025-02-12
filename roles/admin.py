from django.contrib import admin
from .models import Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'description', 'status', 'created_at', 'updated_at')  
    list_filter = ('status',) 
    search_fields = ('role_name', 'description')  

    def delete_model(self, request, obj):
        obj.status = False
        obj.save()

    actions = ['soft_delete_selected']

    def soft_delete_selected(self, request, queryset):
        queryset.update(status=False)
    soft_delete_selected.short_description = "Soft delete selected roles"


