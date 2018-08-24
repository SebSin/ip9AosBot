from telegram.ext import Updater, CommandHandler
import requests


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('643749064:AAFnFeGE8sXSreSuCDampDd97l-nJvlT6HE')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()


url = "https://mobileapp.apple.com/mnm/p/hk/product-locator/quotes?stores=R610%2CR485%2CR673%2CR499%2CR409%2CR428%2CR484%2CR697%2CR672%2CR639%2CR577&pn=MQA62ZP%2FA"
headers = {
    'X-DeviceConfiguration': 'ss=3.00;dim=1125x2436;m=iPhone;v=iPhone10,3;vv=5.1;sv=11.4.1',
    'x-ma-pcmh': 'REL-5.1.0'
}

r = requests.get(url, headers=headers)


print(r.content)