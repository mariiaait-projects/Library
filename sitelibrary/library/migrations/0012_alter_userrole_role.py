from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_userrole_alter_cartheader_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=10),
        ),
    ]
