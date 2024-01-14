import telepot
from gtts import gTTS
import speech_recognition as sr

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
bot = telepot.Bot('YOUR_BOT_TOKEN')

def handle(msg):
    chat_id = msg['chat']['id']
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'voice':
        file_id = msg['voice']['file_id']
        file_info = bot.getFile(file_id)
        file_path = file_info['file_path']

        # Download the voice message
        voice_file = bot.download_file(file_path)
        with open('voice_message.ogg', 'wb') as file:
            file.write(voice_file)

        # Convert speech to text
        recognizer = sr.Recognizer()
        with sr.AudioFile('voice_message.ogg') as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        
        bot.sendMessage(chat_id, f'Text from voice: {text}')

        # Convert text to speech
        tts = gTTS(text=text, lang='en')
        tts.save('text_to_speech.mp3')

        # Send the audio file
        with open('text_to_speech.mp3', 'rb') as audio_file:
            bot.sendAudio(chat_id, audio_file)

    elif content_type == 'text':
        text_message = msg['text']

        # Convert text to speech
        tts = gTTS(text=text_message, lang='en')
        tts.save('text_to_speech.mp3')

        # Send the audio file
        with open('text_to_speech.mp3', 'rb') as audio_file:
            bot.sendAudio(chat_id, audio_file)

# Set the bot's message handler
bot.message_loop(handle)

print('Bot is listening...')

# Keep the program running
while True:
    pass
