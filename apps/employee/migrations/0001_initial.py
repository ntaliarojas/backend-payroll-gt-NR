# Generated by Django 3.2.4 on 2024-03-28 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=200)),
                ('dpi', models.CharField(max_length=13, unique=True)),
                ('date_hiring', models.DateField()),
                ('date_completion', models.DateField(blank=True, null=True)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=10)),
                ('base_salary', models.IntegerField()),
                ('base_salary_initial', models.IntegerField()),
                ('head_department', models.BooleanField(default=False)),
                ('method_payment', models.CharField(choices=[('BANCO', 'Banco'), ('CHEQUE', 'Cheque'), ('EFECTIVO', 'Efectivo')], max_length=100)),
                ('bank', models.CharField(choices=[('BANRURAL', 'Banrural'), ('BANCO INDUSTRIAL', 'Banco Industrial'), ('G&T CONTINENTAL', 'G&T Continental'), ('BAM', 'Banco Agromercantil'), ('BAC', 'Banco de América Central')], max_length=100)),
                ('account_number', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.department')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryIncrease',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('reason', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='RequestAbsenceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='JobPositionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on  was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on  was last modified', verbose_name='modified at')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeDocument',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on  was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on  was last modified', verbose_name='modified at')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('file', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='job_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.jobpositionmodel'),
        ),
    ]
