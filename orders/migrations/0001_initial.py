# Generated by Django 4.1.2 on 2023-05-03 10:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_alter_vendor_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.vendor')),
                ('comission_rate', models.IntegerField()),
                ('total', models.FloatField()),
                ('transaction_id', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=100)),
                ('estate', models.CharField(max_length=100)),
                ('shipping_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('delivered_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('contact_no', models.CharField(max_length=25)),
                ('shipped', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField()),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order')),
            ],
        ),
    ]
