# Generated by Django 4.2.8 on 2024-06-14 09:58

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerAndTabletsBaseClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('processor', models.TextField(max_length=255)),
                ('memory', models.TextField(max_length=255)),
                ('storage', models.TextField(max_length=255)),
                ('graphics_card', models.TextField(max_length=255)),
                ('screen_size', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Price must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(limit_value=999999.99, message='Price cannot exceed 999999.99.')])),
            ],
        ),
        migrations.CreateModel(
            name='ComputerSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('LAPTOP_ACCESSORIES', 'laptop accessories'), ('COMPUTERS_AND_TABLETS', 'computer and tablets'), ('TABLETS_REPLACEMENT_PARTS', 'tablets replacement parts'), ('SERVERS', 'servers'), ('MONITORS', 'monitors')], max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Electronics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('POWER_ACCESSORIES', 'power accessories')], max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LaptopAccessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('SCREEN_FILTERS', 'screen filters'), ('SCREEN_PROTECTORS', 'screen protectors'), ('BATTRIES', 'battries'), ('BAGS', 'bags'), ('CHARGERS_AND_ADAPTORS', 'chargers and adpators')], max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LaptopBagsTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Color', models.CharField(blank=True, max_length=50)),
                ('item_dimensions', models.CharField(blank=True, max_length=50)),
                ('item_weight', models.CharField(blank=True, max_length=25)),
                ('size', models.CharField(blank=True, max_length=50)),
                ('material', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Monitors',
            fields=[
                ('image_1', models.ImageField(null=True, upload_to='images/')),
                ('image_2', models.ImageField(null=True, upload_to='images/')),
                ('image_3', models.ImageField(null=True, upload_to='images/')),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(blank=True, max_length=255)),
                ('aspect_ratio', models.CharField(max_length=255)),
                ('max_display_resolution', models.CharField(max_length=255)),
                ('screen_size', models.CharField(max_length=255)),
                ('monitor_type', models.CharField(default='HOME_OFFICE', max_length=255)),
                ('refresh_rate', models.CharField(max_length=255)),
                ('mounting_type', models.CharField(max_length=255)),
                ('item_dimensions', models.CharField(blank=True, max_length=255)),
                ('item_weight', models.PositiveIntegerField()),
                ('voltage', models.IntegerField(default=220)),
                ('color', models.CharField(blank=True, max_length=50)),
                ('hdmi_port', models.FloatField(default=2.0, max_length=255)),
                ('built_speakers', models.CharField(blank=True, default='yes', max_length=255)),
                ('monitor_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Price must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(limit_value=999999.99, message='Price cannot exceed 999999.99.')])),
                ('quantity_available', models.PositiveIntegerField(default=15)),
                ('restock_threshold', models.PositiveIntegerField(default=9)),
                ('Computer_SubCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Monitors_Computer_Subcategory', to='i.computersubcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('COMPUTER', 'computer'), ('ELECTRONICS', 'electronics'), ('BOOKS', 'Books')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Special_Features',
            fields=[
                ('name', models.CharField(choices=[('adaptive_sync', 'Adaptive Sync'), ('anti_glare_screen', 'Anti Glare Screen'), ('blue_light_filter', 'Blue Light Filter'), ('built_in_speakers', 'Built-In Speakers'), ('built_in_webcam', 'Built-In Webcam'), ('curved', 'Curved'), ('eye_care', 'Eye Care'), ('flicker_free', 'Flicker-Free'), ('frameless', 'Frameless'), ('height_adjustment', 'Height Adjustment'), ('high_dynamic_range', 'High Dynamic Range'), ('lightweight', 'Lightweight'), ('pivot_adjustment', 'Pivot Adjustment'), ('portable', 'Portable'), ('swivel_adjustment', 'Swivel Adjustment'), ('tilt_adjustment', 'Tilt Adjustment'), ('touchscreen', 'Touchscreen'), ('usb_hub', 'USB Hub')], default='Frameless', max_length=255, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TabletsReplacementParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('FLEX_CABLES', 'flex cables'), ('LCD_DISPLAYS', 'Lcd displays')], max_length=255, unique=True)),
                ('ComputerSubCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tab_replace_computersubcategory', to='i.computersubcategory')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tab_replace_product_category', to='i.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(blank=True, max_length=255)),
                ('cpu', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('os', models.CharField(max_length=255)),
                ('cpu_cout', models.PositiveIntegerField(blank=True)),
                ('graphics_card', models.CharField(max_length=255)),
                ('hard_disk', models.CharField(max_length=255)),
                ('flah_memory_size', models.CharField(blank=True, max_length=255)),
                ('item_dimensions', models.CharField(blank=True, max_length=255)),
                ('item_weight', models.PositiveIntegerField(blank=True)),
                ('no_usb_port_two_zero', models.IntegerField()),
                ('no_usb_port_three_zero', models.IntegerField()),
                ('storage_controller', models.CharField(blank=True, max_length=255)),
                ('network_controller', models.IntegerField()),
                ('power_supply_type', models.CharField(blank=True, max_length=255)),
                ('server_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Price must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(limit_value=999999.99, message='Price cannot exceed 999999.99.')])),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='server_product_category', to='i.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ScreenProtector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('screen_surface_description', models.CharField(max_length=255, null=True)),
                ('screen_size', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=255)),
                ('compatible_devices', models.TextField(max_length=255)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screen_protector_laptop_accessories', to='i.laptopaccessories')),
            ],
        ),
        migrations.CreateModel(
            name='ScreenFilters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Color', models.CharField(max_length=50)),
                ('item_dimensions', models.CharField(max_length=50)),
                ('item_weight', models.CharField(max_length=25)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screen_filters_laptop_accessories', to='i.laptopaccessories')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('status', models.BooleanField(default='1', null=True)),
                ('text', ckeditor.fields.RichTextField()),
                ('image_1', models.ImageField(default='https://res.cloudinary.com/dh8vfw5u0/image/upload/v1702231959/rmpi4l8wsz4pdc6azeyr.ico', null=True, upload_to='images/')),
                ('image_2', models.ImageField(default='https://res.cloudinary.com/dh8vfw5u0/image/upload/v1702231959/rmpi4l8wsz4pdc6azeyr.ico', null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='i.monitors')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PowerAccessories',
            fields=[
                ('name', models.CharField(choices=[('ADAPTORS', 'Adaptors'), ('ISOLATED TRANSFORMERS', 'Isolated transformers'), ('PDUS', 'PDUs'), ('LINE CONDITIONERS', 'line conditoners')], max_length=255, unique=True)),
                ('PowerAccessories_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='power_accessories_electronics', to='i.electronics')),
            ],
        ),
        migrations.CreateModel(
            name='PDUS',
            fields=[
                ('style', models.CharField(choices=[('6', '6'), ('8', '8'), ('14', '14'), ('16', '16'), ('20', '20'), ('24', '24'), ('28', '28'), ('30', '30'), ('32', '32'), ('36', '36'), ('38', '38'), ('48', '48')], max_length=50)),
                ('size', models.CharField(choices=[('15', '15'), ('20', '20'), ('30', '30'), ('20A/240V', '20A/240V'), ('30A/240V', '30A/240V'), ('32A/240V', '32A/240V'), ('16A/240V', '16A/240V')], max_length=15)),
                ('configuration', models.CharField(choices=[('STANDARD', 'standard'), ('SURGE_PROTECTION', 'surge_protection'), ('CONTROLLABLE_OUTLETS/NETWORKING_CARD', 'Controllable_Outlets/Networking_Card'), ('CONTROLLABLE_OUTLETS/DUAL_LOAD_BOOK', 'Controllable_Outlets/Dual Load Banks')], max_length=50)),
                ('product_description', models.TextField(blank=True, max_length=1000)),
                ('name', models.CharField(max_length=255)),
                ('pdu_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Price must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(limit_value=999999.99, message='Price cannot exceed 999999.99.')])),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdu_power_accessories', to='i.poweraccessories')),
            ],
        ),
        migrations.AddField(
            model_name='monitors',
            name='Product_Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Monitors_Product_Category', to='i.productcategory'),
        ),
        migrations.AddField(
            model_name='monitors',
            name='special_features',
            field=models.ManyToManyField(to='i.special_features'),
        ),
        migrations.AddField(
            model_name='monitors',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monitor_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='MessengerAndShoulderBag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_feature', models.CharField(max_length=255)),
                ('laptop_accessories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messenger_and_shoulder_bag_laptop_accessories', to='i.laptopaccessories')),
                ('laptop_bag_types', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='messenger_and_shoulder_bag_laptop_bag_type', to='i.laptopbagstypes')),
            ],
        ),
        migrations.CreateModel(
            name='LineConditioners',
            fields=[
                ('voltage_ratings', models.CharField(blank=True, max_length=50)),
                ('current_ratings', models.CharField(blank=True, max_length=15)),
                ('battery_cell_composition', models.CharField(blank=True, max_length=25)),
                ('product_description', models.TextField(blank=True, max_length=1000)),
                ('name', models.CharField(max_length=255)),
                ('line_conditioners_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Price must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(limit_value=999999.99, message='Price cannot exceed 999999.99.')])),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_conditioners_power_accessories', to='i.poweraccessories')),
            ],
        ),
        migrations.CreateModel(
            name='LcdDisplayReplacementParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('compatibility', models.TextField(blank=True, max_length=255)),
                ('product_model_name', models.TextField(blank=True, max_length=255)),
                ('item_weight', models.PositiveIntegerField()),
                ('item_dimensions', models.CharField(blank=True, max_length=255)),
                ('screen_size', models.FloatField(blank=True)),
                ('color', models.CharField(blank=True, max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Price must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(limit_value=999999.99, message='Price cannot exceed 999999.99.')])),
                ('product_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='full_lcd_display_table_replacement_parts', to='i.tabletsreplacementparts')),
            ],
        ),
        migrations.CreateModel(
            name='LaptopBattry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compatible_for_laptop_model', models.TextField(max_length=255)),
                ('battery_cell_composition', models.CharField(max_length=255)),
                ('voltage', models.CharField(max_length=255)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_battry_laptop_accessories', to='i.laptopaccessories')),
            ],
        ),
        migrations.CreateModel(
            name='LaptopBagSleeves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_factor', models.CharField(blank=True, max_length=50)),
                ('shell_type', models.CharField(blank=True, max_length=25)),
                ('compatible_devices', models.TextField(max_length=255)),
                ('laptop_accessories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_bag_sleeves_laptop_accessories', to='i.laptopaccessories')),
                ('laptop_bag_types', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_bag_sleeves_laptop_bag_type', to='i.laptopbagstypes')),
            ],
        ),
        migrations.CreateModel(
            name='LaptopBags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('SLEEVES_BAGS', 'Sleeves Bags'), ('BRIEFCASE', 'Briefcase'), ('MESSENGER_AND_SHOULDER_BAGS', 'Messenger and shoulder Bags'), ('BAGPACKS', 'Bagpacks'), ('HARDSHELL', 'Hardshell')], max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_bags_laptop_accessories', to='i.laptopaccessories')),
            ],
        ),
        migrations.AddField(
            model_name='laptopaccessories',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_accessories_product_category', to='i.productcategory'),
        ),
        migrations.CreateModel(
            name='IsolatedTransformers',
            fields=[
                ('power_source', models.CharField(blank=True, max_length=50)),
                ('current_ratings', models.CharField(blank=True, max_length=15)),
                ('frequency', models.CharField(blank=True, max_length=15)),
                ('product_description', models.TextField(blank=True, max_length=1000)),
                ('name', models.CharField(max_length=255)),
                ('isolated_transformers_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Price must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(limit_value=999999.99, message='Price cannot exceed 999999.99.')])),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isolated_transformers_power_accessories', to='i.poweraccessories')),
            ],
        ),
        migrations.CreateModel(
            name='HardShellCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capatible_devices', models.TextField(max_length=255)),
                ('form_factor', models.CharField(max_length=50)),
                ('shell_type', models.CharField(max_length=50)),
                ('laptop_accessories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hard_shell_cases_laptop_accessories', to='i.laptopaccessories')),
                ('laptop_bag_types', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hard_shell_cases_laptop_bag_type', to='i.laptopbagstypes')),
            ],
        ),
        migrations.CreateModel(
            name='FlexCables',
            fields=[
                ('cable_type', models.CharField(choices=[('MOBILES', 'flex cables'), ('CAMERA', 'Lcd displays'), ('DRONE', 'drone'), ('TABLETS', 'tablets')], max_length=255, unique=True)),
                ('device_name', models.CharField(max_length=255)),
                ('brand_name', models.CharField(max_length=150)),
                ('flex_cable_for_replacement_part', models.CharField(max_length=255)),
                ('flex_cables_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Price must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(limit_value=999999.99, message='Price cannot exceed 999999.99.')])),
                ('product_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cable_type_table_replacement_parts', to='i.tabletsreplacementparts')),
            ],
        ),
        migrations.AddField(
            model_name='electronics',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electronics_product_category', to='i.productcategory'),
        ),
        migrations.AddField(
            model_name='computersubcategory',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comp_product_category', to='i.productcategory'),
        ),
        migrations.CreateModel(
            name='ComputerAndTablets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('LAPTOPS', 'laptop'), ('TABLETS', 'tablets'), ('DESKTOP', 'desktop')], max_length=255, unique=True)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comp_tab_comp_sub_category', to='i.computersubcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ChargersAndadaptors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compatible_devices', models.TextField(max_length=255)),
                ('compatible_phone_models', models.TextField(max_length=255)),
                ('color', models.CharField(blank=True, max_length=25)),
                ('voltage', models.CharField(max_length=255)),
                ('watts', models.CharField(max_length=255)),
                ('connectivity_technology', models.CharField(max_length=255)),
                ('connector_type', models.CharField(max_length=255)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charger_laptop_accessories', to='i.laptopaccessories')),
            ],
        ),
        migrations.CreateModel(
            name='BriefCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_capacity', models.CharField(max_length=25)),
                ('no_of_compartments', models.PositiveIntegerField()),
                ('laptop_accessories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brief_cases_laptop_accessories', to='i.laptopaccessories')),
                ('laptop_bag_types', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_cases_laptop_bag_type', to='i.laptopbagstypes')),
            ],
        ),
        migrations.CreateModel(
            name='BagPacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_capacity', models.CharField(max_length=25)),
                ('laptop_accessories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_bag_paks_laptop_accessories', to='i.laptopaccessories')),
                ('laptop_bag_types', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_bag_packs_laptop_bag_type', to='i.laptopbagstypes')),
            ],
        ),
        migrations.CreateModel(
            name='Adaptors',
            fields=[
                ('connectivity_technology', models.CharField(blank=True, max_length=50)),
                ('connector_type', models.CharField(blank=True, max_length=255)),
                ('compatible_devices', models.TextField(blank=True, max_length=255)),
                ('product_description', models.TextField(blank=True, max_length=1000)),
                ('name', models.CharField(max_length=255)),
                ('adaptors_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Price must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(limit_value=999999.99, message='Price cannot exceed 999999.99.')])),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adaptors_power_accessories', to='i.poweraccessories')),
            ],
        ),
        migrations.CreateModel(
            name='Tablets',
            fields=[
                ('computerandtabletsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='i.computerandtabletsbaseclass')),
                ('computer_and_tablets_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tablets_comp_tab', to='i.computerandtablets')),
            ],
            bases=('i.computerandtabletsbaseclass',),
        ),
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('computerandtabletsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='i.computerandtabletsbaseclass')),
                ('computer_and_tablets_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptops_comp_tab', to='i.computerandtablets')),
            ],
            bases=('i.computerandtabletsbaseclass',),
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('computerandtabletsbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='i.computerandtabletsbaseclass')),
                ('desktop_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('computer_and_tablets_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desktop_comp_tab', to='i.computerandtablets')),
            ],
            bases=('i.computerandtabletsbaseclass',),
        ),
    ]
