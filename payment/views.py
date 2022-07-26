import stripe

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from basket.basket import Basket


@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51LPPeBAFKFk66VzJmrD8Y4NenIhgdnbNg11Lx6Pn0l1fEjRYKI2eFzlB1XpEHp5jH7dYecbGePtoTydhj4MbQtSG00jrXgkkGQ'
    intent = stripe.PaymentIntent.create(
        amount = total,
        currency = 'usd',
        metadata = {'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
