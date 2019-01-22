# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-22 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    replaces = [('home', '0138_auto_20190119_1920'), ('home', '0139_midpointinternfeedback_midpointmentorfeedback'), ('home', '0140_auto_20190121_1904'), ('home', '0141_auto_20190121_1921'), ('home', '0142_auto_20190121_2141')]

    dependencies = [
        ('home', '0137_auto_20190119_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internselection',
            name='midpoint_feedback_due',
            field=models.DateField(blank=True, verbose_name='Date mid-point feedback form due'),
        ),
        migrations.AlterField(
            model_name='internselection',
            name='midpoint_feedback_opens',
            field=models.DateField(blank=True, verbose_name='Date mid-point feedback form opens (typically 7 days before the mid-point feedback deadline)'),
        ),
        migrations.CreateModel(
            name='MidpointInternFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_edits', models.BooleanField()),
                ('ip_address', models.GenericIPAddressField()),
                ('last_contact', models.DateField(verbose_name='What was the last date you were in contact with your mentor?')),
                ('hours_worked', models.CharField(choices=[('10H', '10 hours'), ('20H', '20 hours'), ('30H', '30 hours'), ('40H', '40 hours'), ('50H', '50 hours'), ('60H', '60 hours')], help_text='Include time you spend researching questions, communicating with your mentor and the community, reading about the project and the community, working on skills you need in order to complete your tasks, and working on the tasks themselves. Please be honest about the number of hours you are putting in.', max_length=3, verbose_name='What is the average number of hours per week you spend on your Outreachy internship?')),
                ('mentor_support', models.TextField(verbose_name='Please provide a paragraph describing how your mentor has (or has not) been helping you. This information will only be seen by Outreachy mentors. We want you to be honest with us if you are having trouble with your mentor, so we can help you get a better internship experience.')),
                ('intern_help_requests_frequency', models.CharField(choices=[('0', 'I have not asked for help'), ('U', 'Multiple times per day'), ('D', 'Once per day'), ('M', 'Multiple times per week'), ('W', 'Once per week'), ('B', 'Every other week')], default='0', max_length=1, verbose_name="How often do <b>you</b> ask for your mentor's help?")),
                ('intern_contribution_frequency', models.CharField(choices=[('0', 'I have not submitted a contribution'), ('D', 'Once per day'), ('M', 'Multiple times per week'), ('W', 'Once per week'), ('B', 'Every other week')], default='0', max_length=1, verbose_name='How often do <b>you</b> submit a project contribution?')),
                ('intern_contribution_revision_time', models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=3, verbose_name="How long does it take for <b>you</b> to incorporate your mentor's feedback and resubmit a contribution?")),
                ('progress_report', models.TextField(verbose_name='Please provide a paragraph describing your progress on your project. This will only be shown to Outreachy organizers and Software Freedom Conservancy accounting staff.')),
                ('intern_selection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.InternSelection')),
                ('mentor_help_response_time', models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=3, verbose_name='How long does it take for <b>your mentor</b> to respond to your requests for help?')),
                ('mentor_review_response_time', models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=3, verbose_name='How long does it take for <b>your mentor</b> to give feedback on your contributions?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MidpointMentorFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_edits', models.BooleanField()),
                ('ip_address', models.GenericIPAddressField()),
                ('last_contact', models.DateField(verbose_name='What was the last date you were in contact with your intern?')),
                ('full_time_effort', models.BooleanField(verbose_name='Do you believe your Outreachy intern is putting in a full-time, 40 hours a week effort into the internship?')),
                ('organizer_payment_approved', models.NullBooleanField(default=None, help_text='Outreachy organizers approve or do not approve to pay this intern.')),
                ('request_extension', models.BooleanField(help_text='Sometimes interns do not put in a full-time effort. In this case, one of the options is to delay payment of their stipend and extend their internship a specific number of weeks. You will be asked to re-evaluate your intern after the extension is done.', verbose_name='Does your intern need an extension?')),
                ('request_termination', models.BooleanField(help_text='Sometimes after several extensions, interns still do not put in a full-time effort. If you believe that your intern would not put in a full-time effort with a further extension, you may request to terminate the internship. The Outreachy organizers will be in touch to discuss the request.', verbose_name='Do you believe the internship should be terminated?')),
                ('termination_reason', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text="Please elaborate on the efforts you have put in to get your intern back on track, and the results of those efforts. Tell us about your intern's work efforts, communication frequency, and meeting attendance since their last extension. Provide links to any work that is still in progress or has been completed since their last extension. Please let us know any additional information about why the internship should be terminated.", null=True, verbose_name='Why you feel the internship should be terminated?')),
                ('intern_help_requests_frequency', models.CharField(choices=[('0', 'Intern has not asked for help'), ('U', 'Multiple times per day'), ('D', 'Once per day'), ('M', 'Multiple times per week'), ('W', 'Once per week'), ('B', 'Every other week')], default='0', max_length=1, verbose_name='How often does <b>your intern</b> ask for your help?')),
                ('intern_contribution_frequency', models.CharField(choices=[('0', 'Intern has not submitted a contribution'), ('D', 'Once per day'), ('M', 'Multiple times per week'), ('W', 'Once per week'), ('B', 'Every other week')], default='0', max_length=1, verbose_name='How often does <b>your intern</b> submit a project contribution?')),
                ('intern_contribution_revision_time', models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=3, verbose_name='How long does it take for <b>your intern</b> to incorporate feedback and resubmit a contribution?')),
                ('progress_report', models.TextField(verbose_name="Please provide a paragraph describing your intern's progress on their project. This will only be shown to Outreachy organizers and Software Freedom Conservancy accounting staff.")),
                ('payment_approved', models.BooleanField(help_text='Please base your answer on whether your intern has put in a full-time, 40 hours a week effort. They should have made project contributions, promptly responded to feedback on those contributions, and resubmitted their revised contributions. If they were stuck, they should have reached out to you or the community for help. If you are going to ask for an internship extension, please say no to this question.', verbose_name='Should your Outreachy intern be paid the mid-point $2,000 payment?')),
                ('extension_date', models.DateField(blank=True, help_text="If you want to extend the internship, please pick a date when you will be asked to update your intern's mid-point feedback and authorize payment. Internships can be extended for up to five weeks. We don't recommend extending an internship for more than 3 weeks at mid-point feedback. Please leave this field blank if you are not asking for an extension.", null=True)),
                ('intern_selection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.InternSelection')),
                ('mentor_help_response_time', models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=3, verbose_name="How long does it take for <b>you</b> to respond to your intern's request for help?")),
                ('mentor_review_response_time', models.CharField(choices=[('1H', '1 hour'), ('3H', '3 hours'), ('6H', '6 hours'), ('12H', '12 hours'), ('1D', '1 day'), ('2D', '2-3 days'), ('4D', '4-5 days'), ('6D', '6-7 days'), ('>7D', '> 7 days')], default='>7D', max_length=3, verbose_name="How long does it take for <b>you</b> to give feedback on your intern's contributions?")),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
