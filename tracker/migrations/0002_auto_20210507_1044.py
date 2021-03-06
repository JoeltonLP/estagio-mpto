# Generated by Django 3.2 on 2021-05-07 10:44

from django.db import migrations, models
import django.db.models.deletion
import tracker.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalperson',
            name='fantasy_name',
            field=models.CharField(max_length=200, verbose_name='fantasy_name'),
        ),
        migrations.CreateModel(
            name='PackageContainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=5)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('unique_identify', models.CharField(db_index=True, max_length=5, unique=True)),
                ('delivery_state', models.SmallIntegerField(choices=[(1, 'Na origem'), (2, 'Em trânsito'), (3, 'No destino'), (4, 'Entregue'), (5, 'Extraviado')], default=1)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='as_destination_of', to='tracker.person')),
                ('destination_city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='as_destination_of', to='tracker.city')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='as_sender_of', to='tracker.person')),
                ('sender_city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='as_origin_of', to='tracker.city')),
            ],
        ),
        migrations.CreateModel(
            name='LogTrace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=tracker.models.City, related_name='+', to='tracker.city')),
                ('package_container', models.ForeignKey(on_delete=tracker.models.PackageContainer, related_name='logs', to='tracker.packagecontainer')),
            ],
        ),
    ]
