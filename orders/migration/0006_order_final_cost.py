
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190729_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
     
