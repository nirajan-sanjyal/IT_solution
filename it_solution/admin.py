from django.contrib import admin

from it_solution.models import BusinessGrowth, Comment, CostumerFeedbacks, LatestNews, MeetExports, Project, Services, Technology

# Register your models here.

admin.site.register(Project)
admin.site.register(LatestNews)
admin.site.register(MeetExports)
admin.site.register(Technology)
admin.site.register(BusinessGrowth)
admin.site.register(Comment)
admin.site.register(Services)
admin.site.register(CostumerFeedbacks)

