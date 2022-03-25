from itertools import chain

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models


@login_required
def feed(request):
    followed_users = [
        obj.followed_user
        for obj in models.UserFollows.objects.filter(user__exact=request.user)
    ]
    followed_users.append(request.user)
    
    tickets = models.Ticket.objects.filter(user__in=followed_users)
    reviews = models.Review.objects.filter(user__in=followed_users)

    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True,
    )
    context = {
        "tickets_and_reviews": tickets_and_reviews,
    }

    return render(request, "reviewsapp/posts.html", context=context)


@login_required
def my_posts(request):

    tickets = models.Ticket.objects.filter(user__exact=request.user)
    reviews = models.Review.objects.filter(user__exact=request.user)

    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True,
    )
    context = {
        "tickets_and_reviews": tickets_and_reviews,
    }
    return render(request, "reviewsapp/posts.html", context=context)


@login_required
def ticket_create(request):
    form = forms.TicketForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():

            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, "Le ticket a été publié")
            return redirect("home")
    return render(request, "reviewsapp/ticket_create.html", context={"form": form})


@login_required
def ticket_delete(request, ticket_id):

    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.method == "POST":
        # supprimer le groupe de la base de données
        ticket.delete()
        # rediriger vers la liste des groupes
        messages.success(request, "Le ticket a été supprimé")
        return redirect("home")

    return render(request, "reviewsapp/ticket_delete.html", {"ticket": ticket})


@login_required
def ticket_update(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            messages.success(request, "Le ticket a été modifié")
            return redirect("home")
    else:
        form = forms.TicketForm(instance=ticket)

    return render(request, "reviewsapp/ticket_update.html", {"ticket": ticket})


@login_required
def review_create(request, ticket_id=None):
    review_form = forms.ReviewForm()
    ticket_form = forms.TicketForm()

    if ticket_id is not None:
        ticket = get_object_or_404(models.Ticket, id=ticket_id)
    else:
        ticket = None

    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST, request.FILES)
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if all([ticket_form.is_valid(), review_form.is_valid()]) or all(
            [ticket is not None, review_form.is_valid()]
        ):
            if ticket is None:
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
                ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            messages.success(request, "La critique a été publiée")
            return redirect("home")

    return render(
        request,
        "reviewsapp/review_create.html",
        context={
            "review_form": review_form,
            "ticket_form": ticket_form,
            "ticket": ticket,
        },
    )


@login_required
def review_delete(request, review_id):

    review = get_object_or_404(models.Review, id=review_id)
    if request.method == "POST":
        # supprimer le groupe de la base de données
        review.delete()
        # rediriger vers la liste des groupes
        messages.success(request, "La critique a été supprimée")
        return redirect("home")

    return render(request, "reviewsapp/review_delete.html", {"review": review})


@login_required
def review_update(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)

    if request.method == "POST":
        form = forms.ReviewForm(request.POST, request.FILES, instance=review)
        # form.ticket = review.ticket
        if form.is_valid():
            review.save()
            messages.success(request, "La critique a été modifiée")
            return redirect("home")
    else:
        form = forms.ReviewForm(instance=review)

    return render(request, "reviewsapp/review_update.html", {"review": review})


@login_required
def follow(request):
    all_users = get_user_model().objects.all()
    followed_users = [
        obj.followed_user
        for obj in models.UserFollows.objects.filter(user__exact=request.user)
    ]
    not_followed_users = [
        user
        for user in all_users
        if user.username != request.user.username and user not in followed_users
    ]
    followed_by = [
        obj.user
        for obj in models.UserFollows.objects.filter(followed_user__exact=request.user)
    ]

    if request.method == "POST":
        follow = models.UserFollows()
        follow.user = request.user
        follow.followed_user = get_object_or_404(
            get_user_model(), username__exact=request.POST["followed_user"]
        )
        follow.save()
        messages.success(request, f"Vous vous êtes abonné à {follow.followed_user}")
        return redirect("follow")

    context = {
        "followed_users": followed_users,
        "not_followed_users": not_followed_users,
        "followed_by": followed_by,
    }

    return render(request, "reviewsapp/follow.html", context=context)


@login_required
def follow_delete(request, follow_user_id):
    follow = get_object_or_404(
        models.UserFollows,
        user__exact=request.user.id,
        followed_user__exact=follow_user_id,
    )
    followed_user = get_object_or_404(get_user_model(), id=follow_user_id)
    if request.method == "POST":
        # supprimer l'abonnement de la base de données
        follow.delete()
        # rediriger vers la page abonnement
        messages.success(request, f"Vous vous êtes désabonné de {followed_user}")
        return redirect("follow")

    return render(
        request, "reviewsapp/follow_delete.html", {"followed_user": followed_user}
    )
