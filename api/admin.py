import csv

from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html

from .models import Lead, Product


admin.site.site_header = "Dachfenster-24 Admin"
admin.site.site_title = "Dachfenster-24"
admin.site.index_title = "Dashboard"


def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{meta.model_name}.csv"'

    writer = csv.writer(response)
    writer.writerow(field_names)

    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return response


export_as_csv.short_description = "Export selected rows as CSV"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "image_preview",
        "title",
        "short_description",
        "created_at",
    )
    search_fields = ("title", "description")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "image_preview_large")
    actions = (export_as_csv,)
    fieldsets = (
        ("Product content", {
            "fields": ("title", "description", "image", "image_preview_large"),
        }),
        ("System", {
            "fields": ("created_at",),
            "classes": ("collapse",),
        }),
    )

    @admin.display(description="Image")
    def image_preview(self, obj):
        if not obj.image:
            return "-"
        return format_html(
            '<img src="{}" style="height: 54px; width: 82px; object-fit: cover; border-radius: 8px;" />',
            obj.image.url,
        )

    @admin.display(description="Preview")
    def image_preview_large(self, obj):
        if not obj.image:
            return "No image uploaded."
        return format_html(
            '<img src="{}" style="max-height: 260px; max-width: 100%; object-fit: contain; border-radius: 12px;" />',
            obj.image.url,
        )

    @admin.display(description="Description")
    def short_description(self, obj):
        if not obj.description:
            return "-"
        return obj.description[:90] + ("..." if len(obj.description) > 90 else "")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_link",
        "email_link",
        "postcode",
        "product",
        "status",
        "created_at",
    )
    list_filter = ("status", "created_at", "postcode", "product")
    search_fields = ("name", "phone", "email", "postcode", "message", "product", "admin_notes")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)
    list_editable = ("status",)
    actions = (
        "mark_as_new",
        "mark_as_contacted",
        "mark_as_offer_sent",
        "mark_as_won",
        "mark_as_lost",
        export_as_csv,
    )
    fieldsets = (
        ("Customer", {
            "fields": ("name", "phone", "email", "postcode"),
        }),
        ("Request", {
            "fields": ("product", "message", "status"),
        }),
        ("Internal admin notes", {
            "fields": ("admin_notes",),
        }),
        ("System", {
            "fields": ("created_at",),
            "classes": ("collapse",),
        }),
    )

    @admin.display(description="Phone", ordering="phone")
    def phone_link(self, obj):
        if not obj.phone:
            return "-"
        return format_html('<a href="tel:{}">{}</a>', obj.phone, obj.phone)

    @admin.display(description="Email", ordering="email")
    def email_link(self, obj):
        if not obj.email:
            return "-"
        return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)

    @admin.action(description="Mark selected leads as new")
    def mark_as_new(self, request, queryset):
        queryset.update(status=Lead.Status.NEW)

    @admin.action(description="Mark selected leads as contacted")
    def mark_as_contacted(self, request, queryset):
        queryset.update(status=Lead.Status.CONTACTED)

    @admin.action(description="Mark selected leads as offer sent")
    def mark_as_offer_sent(self, request, queryset):
        queryset.update(status=Lead.Status.OFFER_SENT)

    @admin.action(description="Mark selected leads as won")
    def mark_as_won(self, request, queryset):
        queryset.update(status=Lead.Status.WON)

    @admin.action(description="Mark selected leads as lost")
    def mark_as_lost(self, request, queryset):
        queryset.update(status=Lead.Status.LOST)
