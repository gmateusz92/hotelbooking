# Generated by Django 4.1.2 on 2022-10-13 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receptionist',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='room_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='room',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='room',
            name='price',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_no',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_status_id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type_id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='check_out',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='beds',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('YAC', 'AC'), ('NAC', 'NON-AC'), ('DEL', 'DELUXE'), ('KIN', 'KING'), ('QUE', 'QUEEN')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='PaymentType',
        ),
        migrations.DeleteModel(
            name='Receptionist',
        ),
        migrations.DeleteModel(
            name='RoomStatus',
        ),
        migrations.DeleteModel(
            name='RoomType',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
