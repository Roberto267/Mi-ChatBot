import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola',  'saludos', 'buenas'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes', 'onda'], single_response=True)
        response('Si', ['eres', 'inteligente', 'sabes'], single_response=True)
        response('no tengo sabor para poder decirte pero te recomiendo los tacos de barbacoa xd', ['cual', 'gusta', 'comida'], single_response=True)
        response('lo se :( ', ['triste', 'que'], single_response=True)
        response('estoy hecho para responder solo algunas preguntas :( ', ['para', 'estas', 'hecho'], single_response=True)
        response('4', ['2', 'mas'], single_response=True)
        response('lo siento no  hablo ese idioma', ['hi', 'hello'], single_response=True)
        response('te menti xd nose', ['por', 'menos', 'entre'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
        

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['nose, puedes decirlo de nuevo?', 'No estoy seguro de lo quieres',][random.randrange(3)]
    return response

while True:
    print("ChatBot: " + get_response(input('Persona: ')))