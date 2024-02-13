import nltk

responses = {
    "hi": "Hellow ,how can i help you?",
    "how are you ": "I am doing well, thank you for asking",
    "bye": "GoodBye!",
    "thank you ": "You are welcome!"

}


def chatbot_response(user_input):
    user_input_tokens = nltk.word_tokenize(user_input.lower())
    for word in user_input_tokens:
        if word in responses:
            return responses[word]
    return "I am sorry I didn't understand your question"


while True:
    user_input = input("You:")
    response = chatbot_response(user_input)
    print("Chatbot: ", response)