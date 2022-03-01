from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from . import forms, models

@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    return render(request, 'reviewsapp/home.html', context={'tickets': tickets, 'reviews': reviews})

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
    if request.method == 'POST':
        # supprimer le groupe de la base de données
        ticket.delete()
        # rediriger vers la liste des groupes
        messages.success(request, "Ticket has been deleted" )
        return redirect('home')

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
                {'ticket': ticket})


@login_required
def review_create(request, ticket_id=None):
    form = forms.ReviewForm()
    if ticket_id is not None:
        ticket = get_object_or_404(models.Ticket, id=ticket_id)
    else:
        ticket = None

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        
        
        if form.is_valid():

            

            review = form.save(commit=False)
            if ticket is None:
                review.ticket = get_object_or_404(models.Ticket, id=20)
            review.user = request.user
            
            review.save()
            return redirect('home')
    return render(request, 'reviewsapp/review_create.html', context={'form': form, 'ticket': ticket})


@login_required
def review_details(request, review_id):

    review = get_object_or_404(models.Review, id=review_id)
    if request.method == 'POST':
        # supprimer le groupe de la base de données
        review.delete()
        # rediriger vers la liste des groupes
        messages.success(request, "Review has been deleted" )
        return redirect('home')

    return render(request, 'reviewsapp/review_details.html', {'review': review})


@login_required
def review_update(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES, instance=review)
        #form.ticket = review.ticket
        if form.is_valid():          
            review.save()
            return redirect('review-details', review.id)
    else:
        form = forms.ReviewForm(instance=review)

    return render(request,
                'reviewsapp/review_update.html',
                {'review': review})