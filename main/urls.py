from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home', views.index, name="home"),
    url(r'^login',views.loginPage, name="login"),
    url(r'^logout', views.logoutPage, name='logout'),
    url(r'^register',views.register, name="register"),
    url(r'^browse',views.browse, name="browse"),
    url(r'^plan',views.plan, name="plan"),
    url(r'^about',views.about, name="about"),
    # url(r'^settings',views.settings, name="settings"),
    url(r'^coursecatalog',views.coursecatalog, name="coursecatalog"),
    url(r'^account',views.account, name="account"),
    url(r'^addClass',views.addClass, name="addClass"),
    url(r'^removePlan',views.removePlan, name="removePlan"),
    url(r'^view_path/([0-9]+)',views.view_path ,name='path view'),
    url(r'^view_student/(?P<username>\w+)/$',views.view_student,name='student view'),
    url(r'^view_student/(\w+)/view_path/(?P<pth_id>\w+)',views.view_path,name='student plan view'),
    
    
]