from rest_framework.decorators import api_view
from rest_framework.response import Response

import logging
from . import words_counter

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S',level=logging.INFO)

@api_view(['POST'])
def count_words(request):
    
    if not ('sort_method' in request.data.keys()):
        request.data['sort_method'] = None

    try:
        result = words_counter.main(request.data['url'], request.data['sort_method'])
        return Response(result)
    except Exception as exception:
        logging.exception(f"The following exception has occurred:\n" + str(exception))
        return
