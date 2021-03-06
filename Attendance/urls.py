from django.conf.urls import patterns, include, url
from django.contrib import admin
from model_report import report

report.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Attendance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^marca/', 'asistencia.views.marcar', name='marcar'),
                       url(r'^mensaje/', 'asistencia.views.mensaje', name='mensaje'),
                       url(r'', include('model_report.urls'), name='reportes'),
)
