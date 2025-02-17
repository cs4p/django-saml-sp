# Generated by Django 4.0.8 on 2022-11-02 18:55

from django.db import migrations, models

import sp.models

PPT = "urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport"


class Migration(migrations.Migration):

    dependencies = [
        ("sp", "0011_idp_require_attributes"),
    ]

    operations = [
        migrations.AddField(
            model_name="idp",
            name="authn_comparison",
            field=models.CharField(
                default="exact",
                help_text="The Comparison attribute on RequestedAuthnContext.",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="idp",
            name="authn_context",
            field=models.JSONField(
                default=sp.models._default_authn_context,
                help_text=(
                    f"true ({PPT}), false, or a list of AuthnContextClassRef names."
                ),
            ),
        ),
    ]
