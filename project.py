import pyttsx3
import re
import answers as l
import gui as gu
from tkinter import *
from tkinter import ttk
import time
engine = pyttsx3.init()


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words)

    response('Hello! How can I help you?', [
             'hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)

    response('See you!', ['bye', 'goodbye'], single_response=True)

    response('I\'m doing fine, and you?', [
             'how', 'are', 'you', 'doing'], required_words=['you', 'doing'])

    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)

    response('Thank you!', ['i', 'love', 'code', 'palace'],
             required_words=['code', 'palace'])

    response('For Emergency Call Airport Officers', [
             'is', 'emergency'], required_words=['emergency'])

    response('Love is an abstract thing that cant be done by Bots',
             ['i', 'love', 'you'], required_words=['love'])

    response('We will accommodate you on the next available flight and ensure that you reach your destination.', [
             'i', 'miss', 'my', 'flight'], required_words=['miss'])

    response('Serving of alcohol or consumption of alcohol is strictly prohibited on Domestic flights.', [
             'drink', 'consume', 'offered', 'alcohol'], required_words=['alcohol'])

    response('Smoking is strictly prohibited on-board flights',
             ['i', 'smoke', 'ciggarette', 'flight'], required_words=['smoking'])

    response('Water up to 100ml is permissible to carry onboard. Bottled water is also available on board for sale.', [
             'i', 'carry', 'water'], required_words=['water'])

    response('We allow customers to bring food items on-board.',
             ['i', 'carry', 'food', 'flight'], required_words=['food'])

    response('Valid photo ID for both the unaccompanied minor and the parent/guardian is required at the point of check-in.',
             ['valid', 'id', 'proof', 'photo'], required_words=['id'])

    response('Our security office is at 2nd floor of the Airport',
             ['valid', 'id', 'proof', 'photo'], required_words=['security'])

    response(l.R_CANCEL, ['how', 'to', 'cancel',
             'ticket'], required_words=['cancel', 'ticket'])

    response(l.R_ADVICE, ['give', 'advice'], required_words=['advice'])

    response(l.R_EATING, ['what', 'you', 'eat'],
             required_words=['you', 'eat'])

    response(l.R_VIEW, ['how', 'can', 'view', 'ticket',
             'i', 'want'], required_words=['view', 'ticket'])
             
    response(l.R_ChangeDestination, [
             'how', 'to', 'update', 'change', 'destination'], required_words=['destination'])

    response(l.R_REFUND, ['how', 'to', 'get', 'refund',
             'i', 'want', 'get'], required_words=['refund'])

    response(l.R_LUGGAGE, ['how', 'much', 'maximum',
             'weight', 'luggage', 'carry'], required_words=['luggage'])

    response(l.R_LOST, ['i', 'my', 'forget', 'forgot',
             'luggage', 'lost'], required_words=['lost'])

    response(l.R_MEDICAL, ['if', 'there', 'any', 'medical',
             'emergency', 'asisstance'], required_words=['medical'])

    response(l.R_FARERULES, ['what', 'are',
             'fare', 'rules'], required_words=['fare'])

    response(l.R_FARERULES, ['what', 'are', 'fare',
             'rules', 'price'], required_words=['price'])

    response(l.R_INFANT, ['what', 'is', 'the', 'age', 'group',
             'infants', 'children', 'child'], required_words=['infants'])

    response(l.R_INFANT, ['what', 'is', 'the', 'age', 'group',
             'infants', 'children', 'child'], required_words=['child'])

    response(l.R_CHECKIN, ['what', 'is', 'checkin',
             'requirements', 'proces'], required_words=['checkin'])


    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return l.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def get_input():
    usr = user_input_value.get()
    txt_area.insert(END, "User: " + usr + '\n')
    # Label(text="User :"+ usr).pack(anchor=W)
    data = get_response(usr)
    txt_area.insert(END, "Bot: " + data + '\n')
    # Label(text="Bot: "+data).pack(anchor=W)
    user_input.set("")
    # time.sleep(1)
    file = open("Data.txt", "a")
    file.writelines('You: ' + usr + "\n")
    file.writelines('Bot: ' + data + "\n")
    file.close()
    engine.say(data)
    engine.runAndWait()


root = Tk()
root.geometry("400x600")
root.configure(background="light grey")
root.title("-- CHATBOT --")
# Frame(root,bg="grey").pack(side=TOP)
Label(text="Aman Kumar Sahu -- BT21CSE005 \nRohith Raj -- BT21CSE006 \nIshu Raj -- BT21CSE007 \nAditya Deokar -- BT21CSE008",
      bg="light grey").pack(pady=10)
Label(text="--- AIRLINE CHATBOT - --", font="aireal",
      bg="light grey", fg="red").pack()
# main_frame = Frame(root,bd=4,width=300,height=400).pack()
scrb = ttk.Scrollbar(root, orient=VERTICAL)
txt_area = Text(root, bg="white", width=250, bd=4, yscrollcommand=scrb.set)
scrb.pack(side=RIGHT, fill=Y)
user_input = StringVar()


def ent(event):
    b.invoke()


root.bind('<Return>', ent)
user_input_value = Entry(root, textvariable=user_input, width=50)

b = Button(root, fg="blue", text="SEND", command=get_input, width=20)
txt_area.pack(side=TOP, pady=10, padx=10)
user_input_value.pack(pady=10)
b.pack(pady=10)
root.mainloop()
