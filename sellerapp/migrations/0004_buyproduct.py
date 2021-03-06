# Generated by Django 4.0.5 on 2022-07-04 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0003_alter_product_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_price', models.IntegerField(null=True)),
                ('buyer_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyername', to=settings.AUTH_USER_MODEL)),
                ('product_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sellerapp.product')),
                ('seller_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sellername', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
