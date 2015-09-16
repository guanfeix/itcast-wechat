#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.core.exceptions import *


from wechat.config import *
from wechat.functions import *
from wechat.models import *

import datetime
import time
import hashlib

# Create your views here.
def index(request):
	# 微信接入参考 http://mp.weixin.qq.com/wiki/17/2d4265491f12608cd170a95559800f2d.html
	if request.method == "GET":
		signature	= request.GET.get("signature")
		timestamp	= request.GET.get("timestamp")
		nonce		= request.GET.get("nonce")
		echostr		= request.GET.get("echostr")
		# 放到数组中按字典序排序
		token		= WEIXIN_TOKEN
		tmp_list 	= [token, timestamp, nonce]
		tmp_list.sort()
		# 把三个字符串拼接在一起进行sha1加密
		tmp_str 	= "%s%s%s" % tuple(tmp_list)
		tmp_str		= hashlib.sha1(tmp_str).hexdigest()
		# 判断与传递进来的 signature 是否一致
		if tmp_str == signature:
			return HttpResponse(echostr)
		else:
			return render(request,'index.html')
	else:
		pass
		
def create_menu(request):
	# 在微信公共号中创建菜单，这个请求是要我们主动发起的
	menu_data = {}
	button1 = {}
	button1['name'] = '我的传智历程'
	button1['type'] = 'view'
	button1['url'] = HOME_URL

	menu_data['button'] = [button1]
	
	post_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + get_access_token()	
	post_data = parse_Dict2Json(menu_data)
	resp, content = my_post(post_url, post_data)
	response = parse_Json2Dict(content)
	
	if response['errcode'] == 0:
		return HttpResponse('create menu OK.')
	else:
		return HttpResponse(WEIXIN_ACCESS_TOKEN + ' create menu err:' + response['errmsg'])


def user_info(request):
	# 获取用户 openid 判定 ID 是否是认证用户来跳转不同的页面
	# http://www.cnblogs.com/txw1958/p/weixin71-oauth20.html
	code	= request.GET.get("code", "")
	state	= request.GET.get("state", "")
	
	if code == '':
		return HttpResponse('非法访问...')
	
	# 构造请求 openid 的 url，使用 get 方式请求该 url，将得到的数据转为字典
	url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=' + WEIXIN_APPID + '&secret=' + WEIXIN_APPSECRET + '&code=' + code + '&grant_type=authorization_code'
	resp, content = my_get(url)
	user_dict = parse_Json2Dict(content)
	
	# 临时变量，用来显示用户是否已经申请成为认证用户
	showUrl = ""
	showText = ""
	
	# 判断用户的 openid 是否在 StudentInfo 表中存在
	try:
		isExist = StudentInfo.objects.get(openid = user_dict['openid'])
	except StudentInfo.DoesNotExist:
		# 构造申请成为认证用户的地址
		callback = 'http://www.itcastcpp.cn/register/'
		showUrl = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=' + WEIXIN_APPID + '&redirect_uri=' + callback + '&response_type=code&scope=snsapi_userinfo&state=snsapi_userinfo#wechat_redirect'
		showText = "申请成为认证学员"
	else:
		# 修改前台用来显示的文字
		showUrl = HOME_URL
		showText = "审核中，请等待..."
		# 判断是否是已经审核为认证用户
		if isExist.isRegister:
			# 获取用户的个人信息
			userInfo = {}
			userInfo["userId"]	 = isExist.id
			userInfo["imageUrl"] = isExist.photoAddr
			userInfo["userName"] = isExist.nickName
			userInfo["inClass"]	 = isExist.inClass
			return render(request, 'authorized.html', userInfo)
	
	# 检索学院列表信息
	registerDict = {}
	academyInfoList = AcademyInfo.objects.all()
	registerDict['AcademyInfoList'] = academyInfoList
	registerDict['showUrl'] = showUrl
	registerDict['showText'] = showText

	# 返回
	return render(request, 'index.html', registerDict)
	
def register(request):
	code	= request.GET.get("code", "")
	state	= request.GET.get("state", "")
	
	if code == '':
		return HttpResponse('非法访问...')
	
	# 构造请求 openid 的 url，使用 get 方式请求该 url，将得到的数据转为字典
	url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=' + WEIXIN_APPID + '&secret=' + WEIXIN_APPSECRET + '&code=' + code + '&grant_type=authorization_code'
	resp, content = my_get(url)
	user_dict = parse_Json2Dict(content)
	
	# 获取用户详细信息，储存到 user_info 字典中
	info = 'https://api.weixin.qq.com/sns/userinfo?access_token=' + user_dict['access_token'] + '&openid=' + user_dict['openid'] + '&lang=zh_CN'
	resp, content = my_get(info)
	user_info = parse_Json2Dict(content)
	
	# 返回的 json 数据格式 http://mp.weixin.qq.com/wiki/17/c0f37d5704f0b64713d5d2c37b468d75.html
	# 修改字典的 headimgurl 属性，把头像修改成 96*96 的
	user_info['headimgurl'] = user_info['headimgurl'][:-1]
	user_info['headimgurl'] += '96'
	
	# 取学院的列表
	academyInfoList = AcademyInfo.objects.all()
	user_info['academyInfoList'] = academyInfoList
	
	# 时间过滤 http://www.cnblogs.com/linjiqin/p/3821914.html
	# https://docs.djangoproject.com/en/1.8/ref/models/querysets/#exclude
	# 只取近 60 天内开的班
	begDate = datetime.datetime.now() + datetime.timedelta(days = -60)
	user_info['classInfo'] = ClassInfo.objects.filter(academyID = academyInfoList[0], classBegDate__gt = begDate)
	
	return render(request, 'register.html', user_info)
	
def academyInfo(request, academyinfo_name_slug):
	# 点学院分类跳转到的函数，category_name_slug 是跳转的参数	
	context_dict = {}
	try:
		academyInfo = AcademyInfo.objects.get(slug = academyinfo_name_slug)
		context_dict['academyInfo'] = academyInfo
	except AcademyInfo.DoesNotExist:
		pass
	
	return render(request, 'academyInfo.html', context_dict)
	
def userPost(request):
	# 接收用户申请成为认证学员的数据
	if request.method == "POST":
		stuInfo = StudentInfo(
			openid = request.POST.get("openid"),						# openid
			isRegister = False,											# 由老师管理设置，True为认证成功，False为等待认证
			nickName = request.POST.get("nickname"),					# 用户昵称，由微信接口获取
			stuSex = request.POST.get("sex"),							# 用户性别，由微信接口获取
			stuName = request.POST.get("username"),						# 用户名称，由用户自己输入
			inClass = ClassInfo(id = request.POST.get("classInfo")),	# 所属班级，由用户自己选择
			tel = request.POST.get("usertel"),							# 用户电话，由用户自己输入
			photoAddr = request.POST.get("headimgurl"),					# 用户头像，由微信接口获取
			createTime = datetime.datetime.now(),						# 创建时间
			lastTime = datetime.datetime.now()							# 修改时间，以后修改资料可能会用到
		)
		stuInfo.save()
		return HttpResponse(HOME_URL)
	else:
		return HttpResponse('亲，别乱点...')

def student(request, student_name_slug):
	# 根据班级信息获取班级里面所有学生
	context_dict = {}
	
	try:
		classInfo = ClassInfo.objects.get(slug = student_name_slug)
	except classInfo.DoesNotExist:
		pass
	else:
		try:
			sutList = StudentInfo.objects.filter(inClass = classInfo.id, isRegister = True)
		except StudentInfo.DoesNotExist:
			pass
		else:
			context_dict["stuList"] = sutList

	return render(request, "student.html", context_dict)

def courseList(request, course_name_slug):
	# 构造用户每个阶段的课程和测试信息
	stuId = request.GET.get("userId")
	context_dict = {}
	
	# 获取用户所在班级的开班时间
	begTime = StudentInfo.objects.get(id = stuId).inClass.classBegDate
	dateRet = datetime.date.today() - begTime
	classTime = dateRet.days
	
	# 写个自定义sql，django实在实现不了
	cursor = connection.cursor()
	cursor.execute("select g.stuID_id, s.lessonName, s.timeOut, g.grade "
				"from wechat_syllabusinfo s left outer join "
				"(select * from wechat_gradeinfo where stuID_id = " + stuId + ") g "
				"on s.id = g.syllaID_id")
	context_dict["courseList"] = dictfetchall(cursor)
	context_dict["classTime"] = classTime

	return render(request, "courseList.html", context_dict)

def topic(request):
	context_dict = {}
	return render(request, "courseList.html", context_dict)
	
def help(request):
	context_dict = {}
	return render(request, "courseList.html", context_dict)
	
def about(request):
	context_dict = {}
	return render(request, "courseList.html", context_dict)
	
def ajaxTest(request):
	appid	= request.GET.get("appid")
	return HttpResponse('ajax ok...')
	