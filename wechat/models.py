#encoding:utf-8
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

"""
AcademyInfo		# ѧԺ��
ClassInfo		# �༶��
SyllabusInfo	# �γ̱�
TestInfo		# ������Ŀ��
StudentInfo		# �û���Ϣ��
GradeInfo		# ���Խ����
"""

class AcademyInfo(models.Model):
	#AcademyInfo	ѧԺ��Ϣ
	academyName = models.CharField(max_length = 100,unique = True)	# ����
	slug = models.SlugField(unique=True)							# �޿ո��ѧԺ����
	academyPre = models.CharField(max_length = 30)					# Ժ��
	academyIntro = models.TextField()								# ���
	academyImage = models.ImageField(upload_to = 'upload')			# ѧԺͼƬ

	def save(self, *args, **kwargs):
		self.slug = slugify(self.academyName)
		super(AcademyInfo, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.academyName

class ClassInfo(models.Model):
	#ClassInfo	�༶��Ϣ��
	academyID = models.ForeignKey(AcademyInfo)			# ����ѧԺID
	className = models.CharField(max_length = 100)		# �༶����
	classBegDate = models.DateField()					# ��������
	classCharge = models.CharField(max_length = 30)		# ������
	
	def __unicode__(self):
		return self.className

class SyllabusInfo(models.Model):
	#SyllabusInfo	�γ�����
	academyID = models.ForeignKey(AcademyInfo)			# ����ѧԺID �� C/C++
	lessonName = models.CharField(max_length = 300)		# �γ����� �� MFC�׶Ρ�Qt�׶�
	lessonContent = models.TextField()					# �γ����� �� 1��MFC�ؼ�ʹ��	2��MFC Socket
	timeOut = models.IntegerField()						# ʱ�����������Ի�����ѧʱ��Ϊ׼

	def __unicode__(self):
		return self.lessonName

class TestInfo(models.Model):
	#TestInfo	�����Ϣ��
	syllaID= models.ForeignKey(SyllabusInfo)			# �����γ�����
	topic = models.TextField()							# ��Ŀ
	result = models.TextField()							# ��

	def __unicode__(self):
		return self.topic

class StudentInfo(models.Model):
	#StudentInfo	ѧԱ��Ϣ��
	openid = models.CharField(max_length = 100, unique = True)			# ��ʶ�û�Ψһ��ݵ�openid
	isRegister = models.BooleanField(default=False)		# �Ƿ�����֤ѧԱ��Ĭ�ϲ���
	nickName = models.CharField(max_length = 30)		# ΢���ǳ�
	stuSex = models.BooleanField(default=True)			# ΢�ű�ʶ���Ա�
	stuName = models.CharField(max_length = 30)			# ѧԱ��ʵ���ƣ�ע��ʱ�����
	inClass = models.ForeignKey(ClassInfo)				# �����༶�����Լ��ClassInfo��
	tel = models.CharField(max_length = 20)				# �绰
	qq = models.CharField(max_length = 20)				# QQ
	email = models.EmailField(max_length = 75)			# email
	Idcard = models.CharField(max_length = 30)			# ���֤��
	photoAddr = models.URLField()						# ͷ��
	createTime = models.DateField()						# ע��ʱ��
	lastTime = models.DateField()						# ������ʱ��
	
	# ��¼ѧԱ�ĳ�������
	# stuAge = models.IntegerField()
	# ��¼ѧԺ���ᣬʡ���С���ϸ
	# IdcardAddr = models.CharField(max_length = 200)
	# nowAddress = models.CharField(max_length = 200)
	# ѧԱ��ѧ����Ϣ
	# isGradute = models.BooleanField(default=True)
	# graduteDate = models.DateField()
	# college = models.CharField(max_length = 100)
	# eduBack = models.CharField(max_length = 30)
	# photo = models.ImageField(upload_to='photos',blank = True)

	def __unicode__(self):
		return self.stuName

class GradeInfo(models.Model):	
	# GradeInfo	���Խ����
	stuName = models.ForeignKey(StudentInfo)		# ����ѧԱID
	syllaID  = models.ForeignKey(SyllabusInfo)		# �����γ�ID
	grade = models.IntegerField()					# ���Խ��

	def __unicode__(self):
		return self.stuName

"""
#EmployInfo	NUM.8_jiuye
class EmployInfo(models.Model):
	#empNum 
	stuName = models.ForeignKey(StudentInfo)
	endDAata = models.DateField()
	isEmlpoy =models.BooleanField(default=True)
	company = models.CharField(max_length = 300)

	def __unicode__(self):
		return self.stuName
		
#UserInfo	NUM.5_yonghu
class UserInfo(models.Model):
	#userNum 
	account = models.CharField(max_length = 100)
	isLogin = models.BooleanField(default=True)
	logTime = models.DateField()

	def __unicode__(self):
		return self.account
"""
