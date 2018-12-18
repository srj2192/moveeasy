
import json
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from moveeasy_service.settings import PAGE_LIMIT
from .models import Address


class AddressListController(View):

    def get(self, request, page):
        try:
            address_all = Address.objects.all()

            paginator = Paginator(address_all, PAGE_LIMIT)
            try:
                address = paginator.page(page)
            except EmptyPage:
                address = paginator.page(paginator.num_pages)
            address_list = list(
                map(lambda add: add.as_dict(), list(address))
            )

            request_url = "address/{page_num}/"
            previous_page = request_url.format(
                page_num=address.previous_page_number()
            ) if address.has_previous() else ""
            next_page = request_url.format(
                page_num=address.next_page_number()
            ) if address.has_next() else ""

            json_data = {
                "address": address_list,
                "previous": previous_page,
                "next": next_page
            }
        except Exception:
            return HttpResponse({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return HttpResponse(
            json.dumps(json_data),
            status=status.HTTP_200_OK
        )


class UpdateAddressController(View):

    @csrf_exempt
    def post(self, request):
        post_request = json.loads(request.body)
        user = User.objects.get(username=post_request.get("username"))
        from_date = datetime.strptime(post_request.get("available_from"), '%Y%m%d %H:%M:%S')
        to_date = datetime.strptime(post_request.get("available_to"), '%Y%m%d %H:%M:%S')
        new_address = Address()
        new_address.user = user
        new_address.address = post_request.get("address")
        new_address.available_from = from_date
        new_address.available_to = to_date
        new_address.save()

        return HttpResponse("Address Created Successfully !!!", status=status.HTTP_200_OK)
