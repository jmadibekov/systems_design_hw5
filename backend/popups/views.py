from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Group, UserGroup, AdPopup, PopupGroup
from .serializers import UserSerializer, AdPopupSerializer


@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    users_groups = UserGroup.objects.filter(user=user)
    popup_groups = PopupGroup.objects.filter(
        group__id__in=[x.group.id for x in users_groups]
    )
    ad_popups = (
        AdPopup.objects.filter(id__in=[x.popup.id for x in popup_groups])
        .filter(time_to_send__gte=user.last_logged_in)
        .filter(time_to_send__lte=timezone.now())
        .order_by("-time_to_send")
    )
    ad_to_show = None if not ad_popups else ad_popups[0]

    response_dict = dict(UserSerializer(user).data)
    if ad_to_show is not None:
        ad_dict = AdPopupSerializer(ad_to_show).data
        response_dict |= {
            "ad_popup_id": ad_dict["id"],
            "ad_popup_text": ad_dict["text"],
        }

    # Since this user info has been requested, it means she has logged in
    user.last_logged_in = timezone.now()
    user.save()

    return Response(response_dict)
