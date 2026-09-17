# Rule based of ai python chatbot
import datetime
import time

name = input("Namaste! plse enter your name here:")
presentHour = datetime.datetime.now().hour
if 5 <= presentHour <= 11:
    print("Good morning dear:", name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon dear:", name)
elif 17<= presentHour <= 22:
    print("Good evening dear:", name)
else:
    print("Good night dear:",name)


print("welcome to your AI chatbot:")
print("Ask me some question . type  bye to exit from the bot:")

#chatbot memory creation[dictionary of responses]
responses = {
    "hello":"Welcome! Hii how i can help you?",
    "how are you":"i am fine . thank you for ask me.",
    "who are you":"I am the AI chatbot.",
    "What is function ?":"I dont no but i want to try to learn what is function.",
    "motivate me":"keep going.every bug for your project make you a better developer."
    }
# Function getResponseOfChatbot()
def getResponseOfChatbot(UserQuestion):
    UserQuestion = UserQuestion.lower()
    for eachkey in responses:
        if eachkey in UserQuestion :
            return responses[eachkey]
    else:
        return "mujhe nhi aate . i will try to learn it"

# Take UserInput
while True :

    UserInput = input("Ask me any question based on my knowledge:")
    reply = getResponseOfChatbot(UserInput)
    print(reply)
    if "bye" in UserInput.lower():
        break