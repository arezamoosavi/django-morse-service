from rest_framework import generics, status
from .models import ReceiveSentence
from rest_framework.response import Response
from utils.morse_codes import get_morse_code
from .serializers import QueueSerializer
from .tasks import queue_messege
import logging

logger = logging.getLogger(__name__)

class TranslatetoMorse(generics.GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        if 'sentence' in request.data:
            sentence = request.data['sentence']
            receive_sentence = ReceiveSentence(sentence = sentence)
            receive_sentence.save()

            words = list(sentence.lower())
            result = []

            for word in words:
                if word == ' ':
                    morse = '/'
                else:
                    try:
                        morse = get_morse_code(word = word)
                    except Exception as e:
                        logger.info('morse code translate Error!')
                        return Response({"error": "Unsupport word. Only alphabet", "sentence": request.data['sentence']})

                result.append(morse)

            data = {"morse_code": ''.join(result)}
            logger.info('successfull Translation')    
            return Response(data = data,status=status.HTTP_200_OK)
        logger.error("Error!")
        return Response({"error": "Please format", "format": {"sentence": "Hello"}, "data": request.data})


class QueueMesseges(generics.GenericAPIView):
    serializer_class = QueueSerializer

    def post(self, request, *args, **kwargs):
        serializer = QueueSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        queue_messege.delay(msg = serializer.data['messege'])
        logger.info("end of queue")
        return Response(data ={"Task": "Done"} ,status=status.HTTP_200_OK)