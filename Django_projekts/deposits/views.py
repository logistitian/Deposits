from .models import Deposit
from django.views.generic import FormView, ListView
from deposits.forms import AddDeposit


class DepositView(ListView):
    model = Deposit
    template_name = "index.html"


class AddNewDeposit(FormView):
    form_class = AddDeposit
    template_name = "add_new.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response

