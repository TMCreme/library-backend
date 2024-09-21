"""
Admin for the core app
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering: list[str] = ["id"]
    search_fields: list[str] = ["first_name", "last_name", "email", "country"]
    list_display: list[str] = ["email", "first_name", "last_name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal Info"),
            {"fields": ("first_name", "last_name", "country")},
        ),
        (
            _("Others"),
            {
                "fields": (
                    "account_type",
                    "user_type",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "email_confirmed",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "country",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "account_type",
                    "groups",
                ),
            },
        ),
    )

    # def account_actions(self, obj):
    #     return format_html(
    #         '<a class="button" href="{}">Send Activation</a>&nbsp;',
    #         reverse("user:resend-activation-email", args=[obj.pk]),
    #     )

    # account_actions.short_description = "Account Actions"
    # account_actions.allow_tags = True


admin.site.register(models.User, UserAdmin)
