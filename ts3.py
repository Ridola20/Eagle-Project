import pyttsx3
import openai
import time

# openai.api_key = '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'

# from claude import Claude
# cookie = "sessionKey=..."
# claude = Claude(cookie)


def speak(wrd):
    engt = pyttsx3.init()
    engt.say(wrd)
    engt.runAndWait()

# def get_response(cmd):
#     # using OpenAI's Completion module that helps execute 
#     # any tasks involving text 
#     response = openai.Completion.create(
#         # model name used here is text-davinci-003
#         # there are many other models available under the 
#         # umbrella of GPT-3
#         model="text-davinci-003",
#         # passing the user input 
#         prompt=cmd,
#         # generated output can have "max_tokens" number of tokens 
#         max_tokens=20,
#         # number of outputs generated in one call
#         n=1
#     )
#     # creating a list to store all the outputs
#     output = list()
#     for k in response['choices']:
#         output.append(k['text'].strip())
    # return output
# speak("Good Morning")
# speak("My name is ridola, a prebuilt artificial intelligent bot programmed, managed and designed by Ridwan Sanusi")
# speak("Whenever you need me, just call on my name, Ridola")

cmds = ["This Is Your AI Virtual Assistant Tagged Ridola"]


while True:
    if len(cmds) != 0:
        cpo = cmds.pop()
        f = open("Saved.txt", "r")
        j = f.read()
        f.close()

        j = j.split(";")


        cd = j.pop()
        cmd = j.pop()

        if cpo == cmd:
            pass

        elif cpo != cmd:
            print("Command: " + cmd + "\n")
            speak(cmd)

        # resp = get_response(cmd)
        
        # print(resp)
        # Say(resp)

        cmds.append(cmd)




