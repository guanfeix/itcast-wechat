#encoding:utf-8
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

"""
AcademyInfo		# 学院表
ClassInfo		# 班级表
SyllabusInfo	# 课程表
TestInfo		# 测试题目表
StudentInfo		# 用户信息表
GradeInfo		# 测试结果表
"""

class AcademyInfo(models.Model):
	#AcademyInfo	学院信息
	academyName = models.CharField(max_length = 100,unique = True)	# 名称
	slug = models.SlugField(unique=True)							# 无空格的学院名称
	academyPre = models.CharField(max_length = 30)					# 院长
	academyIntro = models.TextField()								# 简介
	academyImage = models.ImageField(upload_to = 'upload')			# 学院图片

	def save(self, *args, **kwargs):
		self.slug = slugify(self.academyName)
		super(AcademyInfo, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.academyName

class ClassInfo(models.Model):
	#ClassInfo	班级信息表
	academyID = models.ForeignKey(AcademyInfo)			# 所在学院ID
	className = models.CharField(max_length = 100)		# 班级名称
	classBegDate = models.DateField()					# 开班日期
	classCharge = models.CharField(max_length = 30)		# 班主任
	
	def __unicode__(self):
		return self.className

class SyllabusInfo(models.Model):
	#SyllabusInfo	课程名称
	academyID = models.ForeignKey(AcademyInfo)			# 所属学院ID 如 C/C++
	lessonName = models.CharField(max_length = 300)		# 课程名称 如 MFC阶段、Qt阶段
	lessonContent = models.TextField()					# 课程内容 如 1、MFC控件使用	2、MFC Socket
	timeOut = models.IntegerField()						# 时长，天数，以基础入学时间为准

	def __unicode__(self):
		return self.lessonName

class TestInfo(models.Model):
	#TestInfo	题库信息表
	syllaID= models.ForeignKey(SyllabusInfo)			# 所属课程名称
	topic = models.TextField()							# 题目
	result = models.TextField()							# 答案

	def __unicode__(self):
		return self.topic

class StudentInfo(models.Model):
	#StudentInfo	学员信息表
	openid = models.CharField(max_length = 100, unique = True)			# 标识用户唯一身份的openid
	isRegister = models.BooleanField(default=False)		# 是否是认证学员，默认不是
	nickName = models.CharField(max_length = 30)		# 微信昵称
	stuSex = models.BooleanField(default=True)			# 微信标识的性别
	stuName = models.CharField(max_length = 30)			# 学员真实名称，注册时输入的
	inClass = models.ForeignKey(ClassInfo)				# 所属班级，外键约束ClassInfo表
	tel = models.CharField(max_length = 20)				# 电话
	qq = models.CharField(max_length = 20)				# QQ
	email = models.EmailField(max_length = 75)			# email
	Idcard = models.CharField(max_length = 30)			# 身份证号
	photoAddr = models.URLField()						# 头像
	createTime = models.DateField()						# 注册时间
	lastTime = models.DateField()						# 最后访问时间
	
	# 记录学员的出生日期
	# stuAge = models.IntegerField()
	# 记录学院籍贯，省、市、详细
	# IdcardAddr = models.CharField(max_length = 200)
	# nowAddress = models.CharField(max_length = 200)
	# 学员上学的信息
	# isGradute = models.BooleanField(default=True)
	# graduteDate = models.DateField()
	# college = models.CharField(max_length = 100)
	# eduBack = models.CharField(max_length = 30)
	# photo = models.ImageField(upload_to='photos',blank = True)

	def __unicode__(self):
		return self.stuName

class GradeInfo(models.Model):	
	# GradeInfo	测试结果表
	stuName = models.ForeignKey(StudentInfo)		# 所属学员ID
	syllaID  = models.ForeignKey(SyllabusInfo)		# 所属课程ID
	grade = models.IntegerField()					# 测试结果

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
