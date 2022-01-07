from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import User, Guild, Rank, GuildRank, Genre

# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if ('login' in request.POST):
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Invalid Credentials!')
                return redirect('/')
        elif ('register' in request.POST):
            if username == '' or password == '':
                messages.error(
                    request, 'Please provide both username and password')
                return redirect('/')
            else:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Already Taken!')
                    return redirect('/')
                else:
                    user = User.objects.create_user(
                        username=username, password=password)
                    user.save()
                    messages.info(
                        request, 'Account Registered! Please Login Now')
                    return redirect('/')
    else:
        return render(request, 'baseapp/index.html')


def dashboard(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(pk=request.user.pk)
        if current_user.user_is_profile_completed == False:
            return redirect('profile-creation')
        else:
            return redirect('my-profile-tab')
    else:
        return redirect('/')


def profileCreation(request):
    if request.user.is_authenticated:
        genres = Genre.objects.all()
        guilds = Guild.objects.all()
        if request.method == 'POST':
            current_user = User.objects.get(pk=request.user.pk)
            current_user.username = request.POST['username']
            current_user.user_image = request.FILES['user_image']
            for genre in genres:
                if str(genre.genre_name) == request.POST['user_genre']:
                    current_user.user_genre = genre
            for guild in guilds:
                if str(guild.guild_name) == request.POST['user_guild']:
                    current_user.user_guild = guild
            current_user.user_is_profile_completed = True
            current_user.save()
            return redirect('dashboard')
        else:
            return render(request, 'baseapp/profile-creation-components/new-user-welcome.html', {'genres': genres, 'guilds': guilds})
    else:
        return redirect('/')


def myProfileTab(request):
    if request.user.is_authenticated:
        current_user = request.user
        updateRank(request)
        return render(request, 'baseapp/my-profile-tab.html', {
            'user': current_user
        })
    else:
        return redirect('/')


def guildsTab(request):
    current_user = request.user
    if request.user.is_authenticated:
        return render(request, 'baseapp/guilds-tab.html', {
            'user': current_user
        })
    else:
        return redirect('/')


def userGuildOverview(request):
    guild = Guild.objects.all()
    if request.user.is_authenticated:
        return render(request, 'baseapp/guilds-components/user-guild-overview.html', {
            'guild': guild
        })
    else:
        return redirect('/')


def selectedGuild(request, guild_slug):
    selected_guild = Guild.objects.get(slug=guild_slug)
    guild_rank = GuildRank.objects.all()
    if request.user.is_authenticated:
        return render(request, 'baseapp/guilds-components/selected-guild.html', {
            'guild_rank': guild_rank,
            'selected_guild': selected_guild
        })
    else:
        return redirect('/')


def guildRankPlayers(request, guild_slug, guild_rank_slug):
    selected_guild = Guild.objects.get(slug=guild_slug)
    selected_guild_rank = GuildRank.objects.get(slug=guild_rank_slug)
    if request.user.is_authenticated:
        return render(request, 'baseapp/guilds-components/guild-rank-players.html', {
            'selected_guild_rank': selected_guild_rank,
            'selected_guild': selected_guild
        })
    else:
        return redirect('/')


def challengesTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/challenges-tab.html')
    else:
        return redirect('/')


def buyInTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/buy-in-tab.html')
    else:
        return redirect('/')


def myTicketsTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/my-tickets-tab.html')
    else:
        return redirect('/')


def battlesTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/battles-tab.html')
    else:
        return redirect('/')


def adminPanel(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/admin-panel.html')
    else:
        return redirect('/')


def updateRank(request):
    ranks = Rank.objects.all()
    current_user = User.objects.get(pk=request.user.pk)
    for rank in ranks:
        if current_user.user_xp >= rank.rank_min_point:
            current_user.user_rank = rank
            current_user.save()
        else:
            break


def logout_request(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('index')
