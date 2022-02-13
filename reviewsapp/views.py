from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from . import forms, models

@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'reviewsapp/home.html', context={'tickets': tickets})

@login_required
def ticket_create(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():

            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'reviewsapp/ticket_create.html', context={'form': form})

@login_required
def ticket_details(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'reviewsapp/ticket_details.html', {'ticket': ticket})

@login_required
def ticket_update(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)

    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('ticket-details', ticket.id)
    else:
        form = forms.TicketForm(instance=ticket)

    return render(request,
                'reviewsapp/ticket_update.html',
                {'form': form})

@login_required
def ticket_delete(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        # supprimer le groupe de la base de données
        #ticket.delete()
        # rediriger vers la liste des groupes
        messages.success(request, "Ticket has been deleted" )
        return redirect('home')

    return render(request,
           'reviewsapp/ticket_delete.html',
           {'ticket': ticket})