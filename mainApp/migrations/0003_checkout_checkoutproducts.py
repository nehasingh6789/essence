# Generated by Django 4.1.5 on 2023-02-16 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_product_pic1_alter_product_pic2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orderStatus', models.IntegerField(choices=[(0, 'Order Placed'), (1, 'Not Packed'), (2, 'Packed'), (3, 'Ready to Dispatch'), (4, 'Dispatched'), (5, 'Out For Delivery'), (6, 'Delivered'), (7, 'Cancelled')], default=0)),
                ('paymentMode', models.IntegerField(choices=[(0, 'COD'), (1, 'Net Banking')], default=0)),
                ('paymentStatus', models.IntegerField(choices=[(0, 'Pending'), (1, 'Done')], default=0)),
                ('rppid', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('totalAmount', models.IntegerField()),
                ('shippingAmount', models.IntegerField()),
                ('finalAmount', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='CheckoutProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pid', models.IntegerField(default=None)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total', models.IntegerField()),
                ('pic', models.CharField(max_length=50)),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.checkout')),
            ],
        ),
    ]
