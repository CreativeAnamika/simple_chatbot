# from django.shortcuts import render
# from django.http import StreamingHttpResponse
# from .config import get_gemini_chat
# import time

# # Create your views here.

# chat = get_gemini_chat()

# def index(request):
#     return render(request, "chat.html")

# def chat_with_gemini(request):
#     user_msg = request.GET.get("msg", "")

#     def stream():
#         response = chat.send_message(user_msg, stream=True)
       

#         for chunk in response:
#             yield chunk.text
#             time.sleep(0.2)  
#         if len(chat.history) > 3:
#             chat.history = chat.history[-3:]    
        

#     return StreamingHttpResponse(stream(), content_type="text/plain")
# chatbot_app/views.py
from django.shortcuts import render
from django.http import StreamingHttpResponse
from .config import get_gemini_chat
from .websearch import perform_web_search
import time

chat = get_gemini_chat()

def index(request):
    return render(request, "chat.html")

def chat_with_gemini(request):
    user_msg = request.GET.get("msg", "")

    def stream():
        if user_msg.lower().startswith("search:"):
            query = user_msg[len("search:"):].strip()
            search_result = perform_web_search(query)
            yield search_result
        else:
            response = chat.send_message(user_msg, stream=True)
            for chunk in response:
                yield chunk.text
                time.sleep(0.2)

        if len(chat.history) > 3:
            chat.history = chat.history[-3:]

    return StreamingHttpResponse(stream(), content_type="text/plain")
