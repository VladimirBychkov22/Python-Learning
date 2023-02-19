# Telegrambot-Api-openAI
import telebot
import openai

bot= telebot.TeleBot("6255000225:AAHrRn-Gkv376jNvmCs-DuyCEfx8wyYRbcU")
openai. api_key = "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"

@bot.message_handler(content_types=["text"])
def handle_text(message):
   response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"{message.text}",
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
   )
   bot.send_message(message.chat.id, response.choices[0].text)


bot.polling()
