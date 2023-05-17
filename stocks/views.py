from rest_framework.decorators import api_view
from rest_framework.response import Response
from jugaad_data.nse import NSELive

@api_view(['GET'])
def stock_price(request, symbol):
    n = NSELive()
    q = n.stock_quote(symbol)
    return Response({'price': q['priceInfo']})
