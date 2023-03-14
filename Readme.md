# AI learnings

This project allows you to talk with ChatGPT through whatsapp.

Our whatsapp implementation defines a Flask API that receives messages from a whatsapp conversation, process it with ChatGPT and replies the response.
You can also send a voice message and our API will use our text2speech implementation of openai's whisper to transform it to text, send it to ChatGPT and replies with its response.

## Whatsapp

This implementation uses:

- [Flask API](https://github.com/pallets/flask)
- [Facebook whatsapp webhook](https://github.com/Neurotech-HQ/heyoo/#setting-up)
- [heyoo library](https://github.com/Neurotech-HQ/heyoo/) to send messages in a whatsapp conversation.

### Process

1. Set up a facebook app
2. Fork this [glitch project](https://glitch.com/edit/#!/splashy-suave-muskox) and update .env with your API keys
3. Configure the webhooks integration on your facebook app
4. Configure the whatsapp webhook integration on your facebook app
5. Enable the webhook for messages
6. Test by sending messages through whatsapp, you should see them logged on glitch
7. Continue with ChatGPT integration

Notes:

- Facebook recommends to use glitch web to deploy and validate a webhook, tried using ngrok and localtunnel to just tunnel it from my local but they got them banned
- Useful links [1](https://developers.facebook.com/docs/whatsapp/sample-app-endpoints#cloud-api-sample-app-endpoint) [2](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started#configure-webhooks)

## ChatGPT

This implementation uses:

- [openai library](https://github.com/openai/openai-python)

### Process

1. [Implement ChatGPT API](https://platform.openai.com/docs/guides/speech-to-text/quickstart)

We define a very simple function that uses the ChatGPT API and returns its response, this implementation doesn't have memory to optimize token usage

## Text2Speech

This implementation uses:

- [Whisper](https://github.com/openai/whisper/)

### Process

WIP

## How to use locally

```bash
make wsp
make chat t="How many offspring can a cat give birth?"
```
