from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='home'),
    path('category', views.category, name='category'),
    path('blog', views.blog, name='blog'),
    path('artist/<int:id>', views.artist, name='artist'),
    path('music/<int:id>', views.music, name='music'),
    path('artists', views.artists, name='artists'),
    path('artist', views.artist, name='artist'),
    path('playlists', views.playlists, name='playlists'),
    path('playlist', views.playlist, name='playlist'),
    path('contact', views.contact, name='contact'),
    path('About', views.About, name='About'),
    path('LoginT', views.Login, name='index'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('register', views.register, name='register'),
    path('create_event', views.create_Event,name='create_event'),
    path('Show_events', views.Show_events,name='Show_events'),
    path('player', views.player,name='player'),
    path('admin/', views.admin_login),
    # path('adminProfile', views.adminprofile),
    # path('adminhandle', views.adminhandle),
    # path('artistrequest', views.artistrequest),
    # path('acceptartist/<int:id>', views.acceptartist),
    # path('declineartist/<int:id>', views.declineartist),
    # path('adminallusers', views.allusers),
    # path('allmusic', views.allmusic),
    # path('deleteuser/<int:id>', views.deleteuser),
    # path('deletemusic/<int:id>', views.deletemusic),
    # path('update/<int:id>', views.update),
    # path('logout', views.logout, name='logout'),
    # path('profile/<int:id>', views.profile, name='profile'),
    # path('profile/<int:id>/edit', views.edit, name='edit'),
    # path('song/<int:id>', views.song, name='song'),
    # path('addsong', views.addsong, name='addsong'),
    # path('requestToBeArtist', views.requestToBeArtist, name='requestToBeArtist'),
    # path('admin', views.admin, name='admin'),
    # path('admin/acceptArtist/<int:id>', views.acceptArtist, name='acceptArtist'),
    # path('admin/declineArtist/<int:id>', views.declineArtist, name='declineArtist'),
    # path('admin/allArtists', views.allArtists, name='allArtists'),
    # path('admin/allUsers', views.allUsers, name='allUsers'),
    # path('admin/allSongs', views.allSongs, name='allSongs'),
    # path('admin/allAlbums', views.allAlbums, name='allAlbums'),
    # path('admin/allPlaylists', views.allPlaylists, name='allPlaylists'),

]
