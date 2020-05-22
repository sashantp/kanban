from django.db import models

# Create your models here.

COMPANY_TYPES = [
    ('Active', 'active'),
    ('Inactive', 'inactive'),
]


class User(models.Model):

    
    is_default = models.BooleanField(default=True)
    slack_uid = models.CharField(max_length=10, blank=True, null=True)

    username = models.CharField(max_length=40, blank=True, null=True)
    encrypted_password = models.CharField(max_length=20)

    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    designation = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    user_function = models.CharField(max_length=20, blank=True, null=True)

    is_super_admin = models.BooleanField(blank=True)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    created_by = models.ForeignKey('self', models.DO_NOTHING, related_name='User_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('self', models.DO_NOTHING, related_name='User_updated_by', blank=True, null=True)

    permissions = JSONField(default=dict, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'


class Project(models.Model):

    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    status = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    created_by = models.ForeignKey('self', models.DO_NOTHING, related_name='User_created_by', blank=True, null=True)
    updated_by = models.ForeignKey('self', models.DO_NOTHING, related_name='User_updated_by', blank=True, null=True)


class Task(models.Model):

    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    estimated_time = models.IntegerField(null=True,blank=True)
    logged_time = models.IntegerField(null=True, blank=True)

    reporter = models.OneToOneField(User,related_name='Task_reporter', null=False)
    assignee = models.OneToOneField(User, related_name='Task_assignee', null=False)

    watch_list = models.ForeignKey(User, related_name='Task_watch_list', null=True)

    status = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)


class Comments(models.Model):

    text = models.TextField(null=True,blank=True)
    
    task = models.ForeignKey(Task, related_name='Comment_task', null=True, blank=True)
    project = models.ForeignKey(Project, related_name='Comment_project', null=True, blank=True)

    status = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)


class Status(models.Model):

    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    status = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)


class Configuration(models.Model):

    sprint_duration = models.IntegerField(max_length=32, null=True, blank=True)
    