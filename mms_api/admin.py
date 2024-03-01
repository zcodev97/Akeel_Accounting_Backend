from django.contrib import admin
from .models import (Deposit, Withdraw, WithdrawType,
                     Company, Container, Personal, CompanyType,
                     Invoice,BuildingCalc, WithdrawType1,WorkerCalc
                    ,WithdrawType2,CompanyType1,CompanyType2
                     )
from django.utils.html import format_html


@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]

    def get_actions(self, request):
        actions = super(CompanyTypeAdmin, self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


# @admin.register(Personal)
# class PersonalAdmin(admin.ModelAdmin):
#     def formatted_total_price_dinar(self, obj):
#         return format_html(f"IQD {obj.total_dinar:,.0f}")

#     def formatted_total_price_dollar(self, obj):
#         return format_html(f"$ {obj.total_dollar:,.0f}")

#     formatted_total_price_dinar.short_description = 'Total Dinar'  # Sets the column header
#     formatted_total_price_dollar.short_description = 'Total Dollar'  # Sets the column header
#     list_display = ['title', 'container', 'formatted_total_price_dinar',
#                     'formatted_total_price_dollar', 'created_at', 'created_by']

#     def get_actions(self, request):
#         actions = super(PersonalAdmin, self).get_actions(request)
#         print(actions)
#         if 'delete_selected' in actions:
#             del actions['delete_selected']
#         return actions


@admin.register(CompanyType1)
class CompanyType1Admin(admin.ModelAdmin):
    
    list_per_page = 5  # Items per page
    ordering = ('-created_at','title')  # Default ordering
    search_fields = ['title']  # Fields to search by
    def formatted_total_price_dinar(self, obj):
        return format_html(f"IQD {obj.total_dinar:,.0f}")

    def formatted_total_price_dollar(self, obj):
        return format_html(f"$ {obj.total_dollar:,.0f}")

    formatted_total_price_dinar.short_description = 'Total Dinar'  # Sets the column header
    formatted_total_price_dollar.short_description = 'Total Dollar'  # Sets the column header
    list_display = ['title', 'container',
                    #  'company_type',
                     'total_dinar', 'formatted_total_price_dinar',
                    'formatted_total_price_dollar', 'supervisor', 'created_at', 'created_by']

    def get_actions(self, request):
        actions = super(CompanyType1Admin, self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(company_type='c674ded8-5eff-4287-be01-539c7280f70a')

@admin.register(CompanyType2)
class CompanyType2Admin(admin.ModelAdmin):
        
    list_per_page = 5  # Items per page
    ordering = ('-created_at','title')  # Default ordering
    search_fields = ['title']  # Fields to search by
    def formatted_total_price_dinar(self, obj):
        return format_html(f"IQD {obj.total_dinar:,.0f}")

    def formatted_total_price_dollar(self, obj):
        return format_html(f"$ {obj.total_dollar:,.0f}")

    formatted_total_price_dinar.short_description = 'Total Dinar'  # Sets the column header
    formatted_total_price_dollar.short_description = 'Total Dollar'  # Sets the column header
    list_display = ['title',
                    #  'company_type',
                       'container', 'formatted_total_price_dinar',
                    'formatted_total_price_dollar', 'supervisor', 'created_at', 'created_by']

    def get_actions(self, request):
        actions = super(CompanyType2Admin, self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(company_type='4e77e7e6-7a0c-478a-a672-319cb1635383')



@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    def formatted_total_price_dinar(self, obj):
        return format_html(f"IQD {obj.total_dinar:,.0f}")

    def formatted_total_price_dollar(self, obj):
        return format_html(f"$ {obj.total_dollar:,.0f}")

    formatted_total_price_dinar.short_description = 'Total Dinar'  # Sets the column header
    formatted_total_price_dollar.short_description = 'Total Dollar'  # Sets the column header

    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ['name']  # Fields to search by
    list_display = ['name', 'formatted_total_price_dinar', 'formatted_total_price_dollar',
                    'created_at', 'created_by']

    def get_actions(self, request):
        actions = super(ContainerAdmin, self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    # list_filter = ('container', 'company_name','description','received_from')  # Fields to filter by in the sidebar
    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ('container__name', 'company_name__title', 'description', 'received_from')  # Fields to search by

    def formatted_price_dinar(self, obj):
        return format_html(f"IQD {obj.price_in_dinar:,.0f}")

    def formatted_price_dollar(self, obj):
        return format_html(f"$ {obj.price_in_dollar:,.0f}")

    formatted_price_dinar.short_description = 'Total Dinar'  # Sets the column header

    formatted_price_dollar.short_description = 'Total Dollar'  # Sets the column header

    list_display = [
        # 'id',
        'invoice_id',
        'document',
        'deposit_number',
        'container', 'company_name',
        'formatted_price_dinar', 'formatted_price_dollar',
        'description', 'received_from', 'record_created_at',
        'created_at', 'created_by']

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs  # Superuser can see all companies
    #     else:
    #         # Filter companies based on the logged-in supervisor
    #         return qs.filter(company=request.user)

    def get_actions(self, request):
        actions = super(DepositAdmin, self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    



@admin.register(WithdrawType1)
class WithdrawType1Admin(admin.ModelAdmin):

    def formatted_price_dinar(self, obj):
        return format_html(f"IQD {obj.price_in_dinar:,.0f}")

    def formatted_price_dollar(self, obj):
        return format_html(f"$ {obj.price_in_dollar:,.0f}")

    formatted_price_dinar.short_description = 'Total Dinar'  # Sets the column header

    formatted_price_dollar.short_description = 'Total Dollar'  # Sets the column header

    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ('withdraw_type__title',
                     'container__name', 'company_name__title', 'description', 'out_to')  # Fields to search by
    list_display = [
        'invoice_id',
        'document',
        'withdraw_number',
        'withdraw_type',
        'container', 'company_name',
        'formatted_price_dinar', 'formatted_price_dollar',
        'description', 'out_to', 'record_created_at',
        'created_at', 'created_by']

    def get_actions(self, request):
        actions = super(WithdrawType1Admin, self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(company_name__company_type='c674ded8-5eff-4287-be01-539c7280f70a')

@admin.register(WithdrawType2)
class WithdrawType2Admin(admin.ModelAdmin):

    def formatted_price_dinar(self, obj):
        return format_html(f"IQD {obj.price_in_dinar:,.0f}")

    def formatted_price_dollar(self, obj):
        return format_html(f"$ {obj.price_in_dollar:,.0f}")

    formatted_price_dinar.short_description = 'Total Dinar'  # Sets the column header

    formatted_price_dollar.short_description = 'Total Dollar'  # Sets the column header

    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ('withdraw_type__title',
                     'container__name', 'company_name__title', 'description', 'out_to')  # Fields to search by
    list_display = [
        'invoice_id',
        'document',
        'withdraw_number',
        'withdraw_type',
        'container', 'company_name',
        'formatted_price_dinar', 'formatted_price_dollar',
        'description', 'out_to', 'record_created_at',
        'created_at', 'created_by']

    def get_actions(self, request):
        actions = super(WithdrawType2Admin, self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(company_name__company_type='4e77e7e6-7a0c-478a-a672-319cb1635383')


@admin.register(WithdrawType)
class WithdrawTypeAdmin(admin.ModelAdmin):
    list_per_page = 5  # Items per page
    search_fields = ['title']  # Fields to search by
    list_display = ['title']

    def get_actions(self, request):
        actions = super(WithdrawTypeAdmin, self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):

    def formatted_price_dinar(self, obj):
        return format_html(f"IQD {obj.price_in_dinar:,.0f}")

    def formatted_price_dollar(self, obj):
        return format_html(f"$ {obj.price_in_dollar:,.0f}")

    formatted_price_dinar.short_description = 'Total Dinar'  # Sets the column header

    formatted_price_dollar.short_description = 'Total Dollar'  # Sets the column header

    list_display = ['id', 'invoice_id','title', 'description', 'created_at']


@admin.register(BuildingCalc)
class BuildingCalcAdmin(admin.ModelAdmin):

    def formatted_price_dinar(self, obj):
        return format_html(f"IQD {obj.price_in_dinar:,.0f}")

    def formatted_price_dollar(self, obj):
        return format_html(f"$ {obj.price_in_dollar:,.0f}")

    formatted_price_dinar.short_description = 'Total Dinar'  # Sets the column header

    formatted_price_dollar.short_description = 'Total Dollar'  # Sets the column header

    list_display = ['id', 'invoice_id','title', 'description', 'created_at']
@admin.register(WorkerCalc)
class WorkerCalcAdmin(admin.ModelAdmin):

    def formatted_price_dinar(self, obj):
        return format_html(f"IQD {obj.price_in_dinar:,.0f}")

    def formatted_price_dollar(self, obj):
        return format_html(f"$ {obj.price_in_dollar:,.0f}")

    formatted_price_dinar.short_description = 'Total Dinar'  # Sets the column header

    formatted_price_dollar.short_description = 'Total Dollar'  # Sets the column header

    list_display = ['id', 'invoice_id','title', 'description', 'created_at']
