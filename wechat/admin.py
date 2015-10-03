from django.contrib import admin
from wechat.models import UserProfile, AcademyInfo, ClassInfo, SyllabusInfo, TestInfo, StudentInfo, GradeInfo, TestAnsInfo

# Register your models here.

class AcademyInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'academyName', 'academyPre', 'academyIntro', 'slug', 'academyImage')
	prepopulated_fields = {'slug':('academyName',)}
	
class ClassInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'academyID', 'className', 'classBegDate', 'classCharge')
	prepopulated_fields = {'slug':('className',)}
	
class SyllabusInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'academyID', 'lessonName', 'lessonContent', 'timeOut')
	
class TestInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'syllaID', 'topic')
	
class TestAnsInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'testInfoId', 'option', 'rightOption')

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'fromUser', 'nickName', 'stuSex', 'stuName', 'inClass', 'tel', 'createTime', 'lastTime')
	
class StudentInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'isRegister', 'nickName', 'stuSex', 'stuName', 'inClass', 'tel', 'createTime', 'lastTime')
	
class GradeInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'stuID', 'syllaID', 'grade')

admin.site.register(AcademyInfo, AcademyInfoAdmin)
admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(SyllabusInfo, SyllabusInfoAdmin)
admin.site.register(TestInfo, TestInfoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(GradeInfo, GradeInfoAdmin)
admin.site.register(TestAnsInfo, TestAnsInfoAdmin)