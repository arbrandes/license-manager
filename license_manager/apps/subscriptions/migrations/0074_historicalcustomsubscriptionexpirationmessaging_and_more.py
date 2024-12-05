# Generated by Django 4.2.16 on 2024-10-31 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0073_remove_customeragreement_hyper_link_text_for_expired_modal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCustomSubscriptionExpirationMessaging',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('has_custom_license_expiration_messaging', models.BooleanField(default=False, help_text='Indicates if the customer has a unique license expiration experience, instead of the standard one.')),
                ('modal_header_text', models.CharField(blank=True, help_text='The bold text that will appear as the header in the expiration modal.', max_length=512, null=True)),
                ('expired_subscription_modal_messaging', models.TextField(blank=True, help_text='The content of a modal that will appear to learners upon subscription expiration. This text can be used for custom guidance per customer.', null=True)),
                ('button_label_in_modal', models.CharField(blank=True, help_text='The text that will appear as on the button in the expiration modal', max_length=255, null=True)),
                ('url_for_button_in_modal', models.CharField(blank=True, help_text='The URL that should underly the sole button in the expiration modal', max_length=512, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('customer_agreement', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='subscriptions.customeragreement')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical custom subscription expiration messaging',
                'verbose_name_plural': 'historical custom subscription expiration messagings',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='CustomSubscriptionExpirationMessaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_custom_license_expiration_messaging', models.BooleanField(default=False, help_text='Indicates if the customer has a unique license expiration experience, instead of the standard one.')),
                ('modal_header_text', models.CharField(blank=True, help_text='The bold text that will appear as the header in the expiration modal.', max_length=512, null=True)),
                ('expired_subscription_modal_messaging', models.TextField(blank=True, help_text='The content of a modal that will appear to learners upon subscription expiration. This text can be used for custom guidance per customer.', null=True)),
                ('button_label_in_modal', models.CharField(blank=True, help_text='The text that will appear as on the button in the expiration modal', max_length=255, null=True)),
                ('url_for_button_in_modal', models.CharField(blank=True, help_text='The URL that should underly the sole button in the expiration modal', max_length=512, null=True)),
                ('customer_agreement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='_custom_subscription_expiration_messaging', to='subscriptions.customeragreement')),
            ],
        ),
    ]