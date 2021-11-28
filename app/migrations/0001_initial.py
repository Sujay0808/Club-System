# Generated by Django 3.2.3 on 2021-11-28 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carnival',
            fields=[
                ('game_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('venue', models.CharField(max_length=20)),
                ('participation_fee', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_id', models.IntegerField(primary_key=True, serialize=False)),
                ('club_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Guest_Lecture',
            fields=[
                ('lecture_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('resource_person', models.CharField(max_length=20)),
                ('topic_name', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('venue', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('candidate_PRN', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('candidate_name', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('department_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('workshop_id', models.IntegerField(primary_key=True, serialize=False)),
                ('workshop_name', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('venue', models.CharField(max_length=20)),
                ('resource_person', models.CharField(max_length=20)),
                ('total_seat', models.IntegerField()),
                ('registration_fee', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Participation3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_PRN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.participant')),
                ('lecture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.guest_lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Participation2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_winner', models.BooleanField(default=False)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('candidate_PRN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.participant')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carnival')),
            ],
        ),
        migrations.CreateModel(
            name='Participation1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_PRN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.participant')),
                ('workshop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.workshop')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.club')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carnival')),
            ],
        ),
        migrations.CreateModel(
            name='Conduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.club')),
                ('workshop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.workshop')),
            ],
        ),
        migrations.CreateModel(
            name='Club_Member',
            fields=[
                ('member_PRN', models.IntegerField(primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.club')),
            ],
        ),
        migrations.CreateModel(
            name='Arrange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.club')),
                ('lecture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.guest_lecture')),
            ],
        ),
    ]
