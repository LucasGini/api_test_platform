from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

PRODUCT_LINE = (
    (0, 'FMS系统'),
    (1, 'CRM系统'),
    (2, 'TMS系统'),
    (3, 'COO系统'),

)
PRIORITY = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)
ENABLED_FLAG = (
    (0, '禁用'),
    (1, '启用')
)


class ProjectList(models.Model):
    """
    项目列表
    """
    project_name = models.CharField(max_length=128, verbose_name='项目名称')
    product_line = models.CharField(choices=PRODUCT_LINE, max_length=32, verbose_name='产品线')
    pro_principal = models.ForeignKey(User, verbose_name='负责人', on_delete=models.SET_NULL, null=True,
                                      related_name='pro_principal')
    pro_developer = models.ForeignKey(User, verbose_name='开发人员', on_delete=models.SET_NULL, null=True,
                                      related_name='pro_developer')
    pro_tester = models.ForeignKey(User, verbose_name='测试人员', on_delete=models.SET_NULL, null=True,
                                   related_name='pro_tester')
    pro_creator = models.ForeignKey(User, verbose_name='创建人', on_delete=models.SET_NULL, null=True,
                                    related_name='pro_creator')
    enabled_flag = models.CharField(choices=ENABLED_FLAG, max_length=31, verbose_name='启用标记')
    created_date = models.DateTimeField(verbose_name='创建日期', default=datetime.now())
    modified_date = models.DateTimeField(verbose_name='修改时间', default=datetime.now())

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目列表'


class ModuleList(models.Model):
    """
    模块列表
    """
    module_name = models.CharField(max_length=128, verbose_name='模块名称')
    mod_project = models.ForeignKey(ProjectList, verbose_name='归属项目', on_delete=models.SET_NULL, null=True,
                                    related_name='mod_project')
    mod_principal = models.ForeignKey(User, verbose_name='负责人', on_delete=models.SET_NULL, null=True,
                                      related_name='mod_principal')
    mod_developer = models.ForeignKey(User, verbose_name='开发人员', on_delete=models.SET_NULL, null=True,
                                      related_name='mod_developer')
    package_name = models.CharField(max_length=128, verbose_name='包名')
    mod_creator = models.ForeignKey(User, verbose_name='创建人', on_delete=models.SET_NULL, null=True,
                                    related_name='mod_creator')
    enabled_flag = models.CharField(choices=ENABLED_FLAG, max_length=31, verbose_name='启用标记')
    created_date = models.DateTimeField(verbose_name='创建日期', default=datetime.now())
    modified_date = models.DateTimeField(verbose_name='修改时间', default=datetime.now())

    class Meta:
        verbose_name = '模块'
        verbose_name_plural = '模块列表'


class TestCase(models.Model):
    """
    用例列表
    """
    case_name = models.CharField(max_length=128, verbose_name='用例名称')
    case_project = models.ForeignKey(ProjectList, verbose_name='归属项目', on_delete=models.SET_NULL, null=True,
                                     related_name='case_project')
    case_module = models.ForeignKey(ModuleList, verbose_name='模块', on_delete=models.SET_NULL, null=True)
    priority = models.IntegerField(choices=PRIORITY, verbose_name='优先级')
    api_code = models.CharField(max_length=256, verbose_name='接口code')
    parameter = models.TextField(max_length=1024, verbose_name='参数')
    headers = models.TextField(max_length=1024, verbose_name='请求头')
    status = models.CharField(max_length=32, verbose_name='用例状态', )
    enabled_flag = models.CharField(choices=ENABLED_FLAG, max_length=31, verbose_name='启用标记')
    case_creator = models.ForeignKey(User, verbose_name='创建人', on_delete=models.SET_NULL, null=True,
                                     related_name='case_creator')
    created_date = models.DateTimeField(verbose_name='创建日期', default=datetime.now())
    case_modifier = models.ForeignKey(User, verbose_name='修改人', on_delete=models.SET_NULL, null=True,
                                      related_name='case_modifier')
    modified_date = models.DateTimeField(verbose_name='修改时间', default=datetime.now())

    class Meta:
        verbose_name = '用例'
        verbose_name_plural = '用例列表'


class TestSuite(models.Model):
    """
    测试套件
    """
    suite_name = models.CharField(max_length=128, verbose_name='套件名称')
    case_set = models.TextField(max_length=2048, verbose_name='用例集')
    suite_project = models.ForeignKey(ProjectList, verbose_name='归属项目', on_delete=models.SET_NULL, null=True,
                                      related_name='suite_project')
    enabled_flag = models.CharField(choices=ENABLED_FLAG, max_length=31, verbose_name='启用标记')
    suite_creator = models.ForeignKey(User, verbose_name='创建人', on_delete=models.SET_NULL, null=True,
                                      related_name='suite_creator')
    created_date = models.DateTimeField(verbose_name='创建日期', default=datetime.now())
    suite_modifier = models.ForeignKey(User, verbose_name='修改人', on_delete=models.SET_NULL, null=True,
                                       related_name='suite_modifier')
    modified_date = models.DateTimeField(verbose_name='修改时间', default=datetime.now())
    describe = models.TextField(max_length=1024, verbose_name='描述')

    class Meta:
        verbose_name = '测试套件'
        verbose_name_plural = '套件列表'










