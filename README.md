
# Telegram Voice-to-Text and Text-to-Speech Bot

## Overview:

This repository contains a Python script for a Telegram bot capable of processing voice messages, converting them to text, and responding with a synthesized speech audio file. Additionally, it can convert text messages to speech and send the resulting audio file. The bot leverages the Telepot library for Telegram integration, the gTTS library for text-to-speech conversion, and the SpeechRecognition library for voice-to-text functionality.

## Features:

- **Voice-to-Text Conversion:**
  - Handles incoming voice messages and converts them to text using Google's SpeechRecognition API.
  - Sends the recognized text back to the user.

- **Text-to-Speech Conversion:**
  - Converts incoming text messages to speech using the gTTS (Google Text-to-Speech) library.
  - Sends the synthesized audio file back to the user.

- **User-Friendly Telegram Interaction:**
  - Seamless integration with Telegram for easy communication.

## Usage:

1. Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token.

2. Run the script, and the bot will start listening for incoming messages on Telegram.

3. Send a voice message to get the text conversion or send a text message to get the corresponding speech audio.

## Requirements:

- `telepot==13.5`
- `gtts==2.2.2`
- `SpeechRecognition==3.8.1`

Feel free to contribute, report issues, or enhance the functionality of this Telegram Voice-to-Text and Text-to-Speech bot. Happy botting!
