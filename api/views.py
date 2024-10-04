from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ocpp_lib.call import Call
from ocpp_lib.types import RemoteStartTransaction_Req, IdToken
@csrf_exempt
async def test_view(request):
    return JsonResponse({'yes': 'yes'})
