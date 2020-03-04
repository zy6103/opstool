from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """登陆账号"""
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        ('staff_status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    project_tab = models.ManyToManyField('ProjectTab')
    objects= UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

class IDCTab(models.Model):
    name = models.CharField(max_length=64, unique=True)
    notes = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name


class ProjectTab(models.Model):
    """项目表"""
    name = models.CharField(max_length=64, verbose_name='项目名')
    pro_type_choices = (
        ('---','---'),
        ('app','app'),
        ('db2','db2'),
        ('oracle','oracle'),
        ('mysql','mysql')
    )
    pro_type = models.CharField(choices=pro_type_choices,max_length=8,default='---', verbose_name='项目主机类型')
    notes = models.TextField(blank=True,null=True)

    def __str__(self):
        return '%s-%s' % (self.name,self.pro_type)

    class Meta:
        unique_together = ('name','pro_type')


class SysTypeTab(models.Model):
    '''主机系统类型'''
    name = models.CharField(max_length=16,unique=True,verbose_name='主机系统类型',help_text='AIX/redhat6/redhat7/...')
    notes = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name


class HostTab(models.Model):
    """主机系统"""
    ip_addr = models.GenericIPAddressField(verbose_name='系统IP')
    port = models.PositiveSmallIntegerField(default=22)
    login_user = models.CharField(max_length=16,verbose_name='用户名')
    login_pwd = models.CharField(max_length=32,verbose_name='密码')
    sys_type_tab = models.ForeignKey('SysTypeTab')
    project_tab = models.ForeignKey('ProjectTab')
    idc_tab = models.ForeignKey('IDCTab')

    def __str__(self):
        return '%s(%s))' % (self.ip_addr,self.sys_type_tab)


class TaskTab(models.Model):
    """批量任务记录表"""
    user = models.ForeignKey('UserProfile',verbose_name='关联账号')
    pid = models.PositiveIntegerField(verbose_name='任务ID')
    host_tab = models.ForeignKey('HostTab',verbose_name='关联主机')
    task_read_choices = (
        (0,'未读'),
        (1,'已读')
    )
    task_read = models.SmallIntegerField(choices=task_read_choices,verbose_name='任务查看状态')
    task_status_choices = ((0, 'success'), (1, 'failed'), (2, 'init'))
    status = models.SmallIntegerField(choices=task_status_choices,verbose_name='任务执行结果状态')
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return '%s' % self.pid

class TaskLogDetailTab(models.Model):
    '''任务结果记录'''
    task = models.ForeignKey('TaskTab')
    result = models.TextField(blank=True,null=True)
    start_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    end_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return '%s' % (self.task)
