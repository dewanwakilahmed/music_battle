from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import User, Guild, Rank, GuildRank, Genre, Ticket, UserTicket, BuyIn

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

def userBuyInOverview(request):
    if request.user.is_authenticated:
        buy_ins = BuyIn.objects.all()
        if request.method == 'POST':
            for buy_in in buy_ins:
                if str(buy_in) in request.POST:
                    user_buy_in = buy_in
                    return redirect('buy-in-actions', user_buy_in)
        return render(request, 'baseapp/buy-in-components/user-buy-in-overview.html', { "buy_ins": buy_ins })
    else:
        return redirect('/')

def buyInActions(request, user_buy_in):
    if request.user.is_authenticated:
        user_tickets = UserTicket.objects.all()
        current_user_tickets = user_tickets.filter(user=request.user)
        buy_ins = BuyIn.objects.all()
        buy_in_item = None
        available_ticket = None
        for buy_in in buy_ins:
                if str(buy_in) == user_buy_in:
                    buy_in_item = buy_in
        for current_user_ticket in current_user_tickets:
            if str(current_user_ticket.type) in user_buy_in:
                available_ticket = current_user_ticket
        return render(request, 'baseapp/buy-in-components/buy-in-actions.html', { "available_ticket": available_ticket, "buy_in_item": buy_in_item })
    else:
        return redirect('/')

def myTicketsTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/my-tickets-tab.html')
    else:
        return redirect('/')

def userTicketsOverview(request):
    if request.user.is_authenticated:
        user_tickets = UserTicket.objects.all()
        current_user_tickets = user_tickets.filter(user=request.user)
        return render(request, 'baseapp/my-tickets-components/user-tickets-overview.html', { "user_tickets": current_user_tickets })
    else:
        return redirect('/')

def buyTickets(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.all()
        current_user = User.objects.get(pk=request.user.pk)
        if request.method == 'POST':
            for ticket in tickets:
                if (str(ticket.type) in request.POST):
                    if current_user.user_gold > ticket.price:
                        current_user.user_gold -= ticket.price
                        if UserTicket.objects.filter(user=current_user, type=ticket).exists():
                            user_ticket = UserTicket.objects.get(user=current_user, type=ticket)                            
                        else:
                            user_ticket = UserTicket.objects.create(
                            user=current_user, type=ticket)
                        user_ticket.num_of_tickets += 1
                        user_ticket.save()
                        current_user.save()
                        messages.info(
                        request, 'Ticket Purchased!')
                    return redirect('buy-tickets')
            current_user.save()
                
        return render(request, 'baseapp/my-tickets-components/buy-tickets.html', {"tickets": tickets})
    else:
        return redirect('/')

def ticketActions(request, selected_ticket):
    if request.user.is_authenticated:
        user_tickets = UserTicket.objects.all()
        selected_user_ticket = None
        for user_ticket in user_tickets:
            if str(user_ticket) == selected_ticket:
                selected_user_ticket = user_ticket
                print(selected_user_ticket)
        if request.method == 'POST':
            if ('drop_item' in request.POST):
                if (selected_user_ticket.num_of_tickets > 0):
                    selected_user_ticket.num_of_tickets -= 1
                    selected_user_ticket.save()
                    messages.info(request, 'Ticket Item Dropped!')
                else:
                    messages.info(request, 'No Such Ticket Item Found!')
            if ('use_item' in request.POST):
                pass
            if ('sell_item' in request.POST):
                if (selected_user_ticket.num_of_tickets > 0):
                    selected_user_ticket.num_of_tickets -= 1
                    user = request.user
                    user.user_gold += selected_user_ticket.type.sell_back_price
                    user.save()
                    selected_user_ticket.save()
                    messages.info(request, 'Ticket Item Dropped!')
                else:
                    messages.info(request, 'No Such Ticket Item Found!')
            return redirect('ticket-actions', selected_user_ticket)
        return render(request, 'baseapp/my-tickets-components/ticket-actions.html', { "selected_user_ticket": selected_user_ticket })
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
