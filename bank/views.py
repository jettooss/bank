
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.decorators import login_required
from .models import *

dd=[]


class BankInterest():
    def __init__(self, summ, perc, period):
        self.summ = summ
        self.period = period
        self.perc = perc

    def diff_int(self):
        arr = []
        mp_cnt = self.period * 12
        rest = self.summ
        mp_real = self.summ / (self.period * 12.0)
        while mp_cnt != 0:
            mp = mp_real + (rest * self.perc / 1200)
            arr.append(round(mp, 2))
            rest = rest - mp_real
            mp_cnt = mp_cnt - 1
        return arr, round(sum(arr), 2)
# Create your views here.
def index(request):
    p_form = cartForm2()
    context = {

        'p_form': p_form
    }
    return render(request, 'bank/bbb.html', {'title': 'гл стр'})


@login_required(login_url='login')
def credit(request):
    # if request.POST.get('get_active_true'):#ипотека
    posts = homes.objects.all()
    housing = housing_cost.objects.all()

    context = {
        'form': posts,
        'housing': housing,

    }

    return render(request, 'bank/credit.html', context)




@login_required(login_url='login')
def account(request):
    if request.method == 'POST':
        u_form = personalForm(request.POST)
        p_form = cartForm(request.POST)
        c_form = information_form(request.POST)
        if u_form.is_valid():
            u_form.save()

            messages.success(request, f'Your account has been updated!')
        elif p_form.is_valid():
            p_form.save()
        elif c_form.is_valid():
            c_form.save()


    else:
        u_form = personalForm(request.POST)
        p_form = cartForm(request.POST)
        c_form = information_form(request.POST)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'c_form': c_form
    }

    return render(request, 'bank/account.html', context)


def register(request):
    form = CreationForm()

    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'вы зарегистрированы{user}')
            return redirect('login')

    context = {'form': form}
    return render(request, 'bank/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('bank')
        else:
            messages.info(request, f'что не так,{user}')

    return render(request, 'bank/login.html')


def logoutUser(request):
    logout((request))
    return redirect('login')


def credit1(request):
    bid = 7
    info = 0
    if request.method == 'POST':
        form = login_form(request.POST)
        login = request.POST.get('login')
        money = request.POST.get('loan')
        time = request.POST.get('term')
        percent = request.POST.get('percent')
        x = information.objects.get(login=login).children
        b = information.objects.get(login=login).relationship
        v = information.objects.get(login=login).salary
        if b == "В":
            info += 2
        elif b == "П":
            info += 1
        elif b == "Х":
            info -= 1
        if x == "В":
            info += 2
        elif x == "П":
            info -= 1
        elif x == "Р":
            info -= 2
        elif x == "Р":
            info -= 2
        if info > 5:
            bid += 4



                           # Сумма,  процент, срок(год)
        diff = BankInterest(int(money), bid, int(time)).diff_int()
        payment = (diff)[0][0]

        balances = card.objects.get(name=login).balance
        if form.is_valid():

            if int(v) / 2 >= payment and int(percent) == int(bid):
                form.save()
                balances = card.objects.get(name=login).balance
                s = int(balances) + int(money)
                number = card.objects.filter(name=login).update(balance=s)


                for i, v in enumerate(diff):
                    if i == 0:
                        for j, p in enumerate(v):
                            messages.info(request, "Платеж {:7d} : {:.2f} руб.".format(j + 1, p))


                    else:
                        messages.info(request, "Всего выплачено будет: {:.2f} руб.".format(v))



            elif percent != bid:
                messages.info(request, f'Ваша процентная ставка должна быть:{bid}')
            else:
                messages.info(request, f'Вам не одобрили кредит :{info}')
    else:
        form = login_form(request.POST)
    context = {

        'form': form,
        'percent': bid,
    }
    return render(request, 'bank/credit1.html', context)


def score(request):
    if request.method == 'POST':
        p_form = cartForm2(request.POST)
        try:
            term = request.POST.get('term')
            сard_number = request.POST.get('card_number')
            Balance = request.POST.get('balance')
            cvv = request.POST.get('Cvv')
            x = card.objects.get(pk=сard_number)
            remainders = x.card_number
            remainder = x.balance
            if cvv == str(x.Cvv) and term == str(x.term):
                df = int(Balance) + remainder
                number = card.objects.filter(pk=remainders).update(balance=df)
                messages.info(request, f' Баланс:{df}')
            else:
                messages.info(request, f'вы ввели неверные данные')
        except card.DoesNotExist:
            messages.info(request, f'вы ввели неверные данные')
    else:

        p_form = cartForm2(request.POST)

    context = {
        'p_form': p_form
    }
    return render(request, 'bank/score.html', context)


# @login_required(login_url='login')

def show_post(request, post_id):

    post = get_object_or_404(homes, pk=post_id)
    posts = homes.objects.get(complex=post_id)
    housing = housing_cost.objects.get(complex=post_id)
    d = estateform(request.POST)
    login = request.POST.get('login')
    context = {
        'post': str(post),
        'cat_selected': post.complex,
        'housing': housing,
        'posts': posts,
        "d": d
    }
    if request.method == 'POST':
        prise = request.POST.get('test')
        balances = card.objects.get(name=login).balance
        if str(prise) == 'Выберите квартиру':
            messages.info(request, f' Выбери тип квартиры  :{login}')

        else:
            if int(balances) >= int(prise):
                # messages.info(request, f'Вам  купили  квартиру :{login}')
                cv=(
                    login,
                    post_id,
                   prise
                )
                sd = estate(
                    login=personal_data1.objects.get(last_name=login),
                    name_complex=post_id,
                    price=prise
                ).save()
                dd.append(cv)
                balances = card.objects.get(name=login).balance
                s = int(balances) - int(prise)
                number = card.objects.filter(name=login).update(balance=s)
                messages.info(request, f' :{dd}')
                context = {
                    'post': str(post),
                    'cat_selected': post.complex,
                    'housing': housing,
                    'posts': posts,
                    "d": d
                }
            elif int(balances) >= int(prise) *0.10:


                #                   Сумма,  процент, срок(год)
                diff = BankInterest(int(prise), 7, int(15)).diff_int()
                messages.info(request, f' Нужна Ипотека :{login}')
# не реальзовал
            else:
                messages.info(request, f' У вас недостаточно средств:{login}')


    return render(request, 'bank/post.html', context=context)


