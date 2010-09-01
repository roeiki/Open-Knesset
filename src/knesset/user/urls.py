from django.conf.urls.defaults import *
from views import PublicUserProfile, ProfileListView

user_public_profile = PublicUserProfile(slug_field='username')
profile_list = ProfileListView()

# views coded in this app
urlpatterns = patterns('knesset.user.views',
    url(r'^create/$', 'create_user', name ='register'),
    url(r'^members/$', 'follow_members', name ='follow-members'),
    url(r'^edit-profile/$', 'edit_profile', name='edit-profile'),
    )


urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'user/login.html'}, name='login'),
    url(r'^logout/$', 'logout_then_login', name='logout'),
    url(r'^password_reset/$', 'password_reset', {'template_name': 'user/password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset/done/$', 'password_reset_done', {'template_name': 'user/password_reset_done.html'}),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', {'template_name': 'user/password_reset_confirm.html'}),
    url(r'^reset/done/$', 'password_reset_complete', {'template_name': 'user/password_reset_complete.html'}),
    )

# views coded elsewhere
urlpatterns += patterns('',
    (r'^registration/', include('knesset.accounts.urls')),
    url(r'^(?P<object_id>\d+)/$', user_public_profile, name='public-profile'),
    url(r'^(?P<slug>.+)/$', user_public_profile, name='public-profile'),
    url(r'^$', profile_list, name='profile-list'),
    )
