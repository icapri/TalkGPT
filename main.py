import openai
import os
import speech_recognition

# Set the openAI API Key.
openai.api_key = os.getenv("OPENAI_API_KEY")

# Contains a new instance of the Recognizer.
recognizer = speech_recognition.Recognizer()

# Generates a string answer for the specified question.
def answer(question):
    response = openai.Completion.create(
        engine="MODEL",
        messages=[
            {
                'role': 'user',
                'content': question,
            }
        ],
        temperature=0,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0
    )
    response = response['choices'][0]['message']['content']
    return response

# Contains the question asked by the user.
question = ''

while question != 'quit':
    print('Hello! How may I help you?')
    with speech_recognition.Microphone() as source:
        # wait a while in order to have the recognizer adjust the energy
        # threshold based on the surrounding noise level
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.record(source, duration=5)

    # Generate a string from the specified audio.
    question = recognizer.recognize_google(audio)

    print(question)
    if question != 'quit':
        answer(question)
