from django.contrib import admin
from wechat.models import AcademyInfo, ClassInfo, SyllabusInfo, TestInfo, StudentInfo, GradeInfo

# Register your models here.

class AcademyInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'academyName', 'academyPre', 'academyIntro', 'slug', 'academyImage')
	prepopulated_fields = {'slug':('academyName',)}
	
class ClassInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'academyID', 'className', 'classBegDate', 'classCharge')
	
class SyllabusInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'academyID', 'lessonName', 'lessonContent', 'timeOut')
	
class TestInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'syllaID', 'topic', 'result')
	
class StudentInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'isRegister', 'nickName', 'stuSex', 'stuName', 'inClass', 'tel', 'qq', 'email', 'Idcard', 'createTime', 'lastTime')
	
class GradeInfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'stuName', 'syllaID', 'grade')

admin.site.register(AcademyInfo, AcademyInfoAdmin)
admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(SyllabusInfo, SyllabusInfoAdmin)
admin.site.register(TestInfo, TestInfoAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(GradeInfo, GradeInfoAdmin)