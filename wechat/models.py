#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

"""
AcademyInfo		# ѧԺ��
ClassInfo		# �༶��
SyllabusInfo	# �γ̱�
TestInfo		# ������Ŀ��
TestAnsInfo		# ������Ŀѡ�����ȷ�𰸱�
StudentInfo		# �û���Ϣ��
GradeInfo		# ���Խ����
CREATE DATABASE itcast_wechat DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
"""

class AcademyInfo(models.Model):
	"AcademyInfo	ѧԺ��Ϣ"
	academyName = models.CharField(max_length = 100,unique = True)	# ����
	slug = models.SlugField(unique = True)							# �޿ո��ѧԺ����
	academyPre = models.CharField(max_length = 30)					# Ժ��
	academyIntro = models.TextField()								# ���
	academyImage = models.ImageField(upload_to = 'upload')			# ѧԺͼƬ

	def save(self, *args, **kwargs):
		self.slug = slugify(self.academyName)
		super(AcademyInfo, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.academyName

class ClassInfo(models.Model):
	"ClassInfo	�༶��Ϣ��"
	academyID = models.ForeignKey(AcademyInfo)			# ����ѧԺID
	className = models.CharField(max_length = 100)		# �༶����
	slug = models.SlugField(unique = True)				# ������ҳ����ת
	classBegDate = models.DateField()					# ��������
	classCharge = models.CharField(max_length = 30)		# ������
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.className)
		super(ClassInfo, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.className

class SyllabusInfo(models.Model):
	"SyllabusInfo	�γ�����"
	academyID = models.ForeignKey(AcademyInfo)			# ����ѧԺID �� C/C++
	lessonName = models.CharField(max_length = 300)		# �γ����� �� MFC�׶Ρ�Qt�׶�
	lessonContent = models.TextField()					# �γ����� �� 1��MFC�ؼ�ʹ��	2��MFC Socket
	timeOut = models.IntegerField()						# ʱ�����������Ի�����ѧʱ��Ϊ׼

	def __unicode__(self):
		return self.lessonName

class TestInfo(models.Model):
	"TestInfo	�����Ϣ��"
	syllaID= models.ForeignKey(SyllabusInfo)			# �����γ�����
	topic = models.TextField()							# ��Ŀ

	def __unicode__(self):
		return self.topic

class TestAnsInfo(models.Model):
	"TestAnsInfo	��Ŀѡ���ű�"
	testInfoId = models.ForeignKey(TestInfo)				# ��Ӧ��Ŀ
	option = models.CharField(max_length = 300)				# ��Ŀ����ѡ������
	rightOption = models.BooleanField(default = False)		# �Ƿ�����ȷ��
	
	def __unicode__(self):
		return self.option

class UserProfile(models.Model):
	"�����û������֤�����ṹ"
	fromUser = models.OneToOneField(User)
	nickName = models.CharField(max_length = 30)		# ΢���ǳ�
	stuSex = models.IntegerField(default=True)			# ΢�ű�ʶ���Ա�
	stuName = models.CharField(max_length = 30)			# ѧԱ��ʵ���ƣ�ע��ʱ�����
	country = models.CharField(max_length = 30)			# ����
	province = models.CharField(max_length = 30)		# ʡ��
	city = models.CharField(max_length = 30)			# ����
	inClass = models.ForeignKey(ClassInfo)				# �����༶�����Լ��ClassInfo��
	tel = models.CharField(max_length = 20)				# �绰
	photoAddr = models.URLField()						# ͷ��
	createTime = models.DateField()						# ע��ʱ��
	lastTime = models.DateField()						# ������ʱ��
	
	# ���������������ֶΣ������΢�Ż�ȡ�����û��������Ϣ
	
	def __unicode__(self):
		return self.fromUser.username
		
class StudentInfo(models.Model):
	"StudentInfo	ѧԱ��Ϣ��"
	openid = models.CharField(max_length = 100, unique = True)			# ��ʶ�û�Ψһ��ݵ�openid
	isRegister = models.BooleanField(default=False)		# �Ƿ�����֤ѧԱ��Ĭ�ϲ���
	nickName = models.CharField(max_length = 30)		# ΢���ǳ�
	stuSex = models.IntegerField(default=True)			# ΢�ű�ʶ���Ա�
	stuName = models.CharField(max_length = 30)			# ѧԱ��ʵ���ƣ�ע��ʱ�����
	inClass = models.ForeignKey(ClassInfo)				# �����༶�����Լ��ClassInfo��
	tel = models.CharField(max_length = 20)				# �绰
	photoAddr = models.URLField()						# ͷ��
	createTime = models.DateField()						# ע��ʱ��
	lastTime = models.DateField()						# ������ʱ��
	
	# ���������Ҫ����ϸ���û������Ϣ�����������������ֶ�

	def __unicode__(self):
		return self.stuName

class GradeInfo(models.Model):	
	"GradeInfo	���Խ����"
	stuID = models.ForeignKey(StudentInfo)			# ����ѧԱID
	syllaID = models.ForeignKey(SyllabusInfo)		# �����γ�ID
	grade = models.CharField(max_length = 10)		# ���Խ��

	def __unicode__(self):
		return self.grade