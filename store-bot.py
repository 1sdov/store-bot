from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Bot token
TOKEN = "7572242303:AAFaI-l8HSsByrWVNk4g3tm2p8wWyJrC5FM"

# Do‘kon manzili
STORE_LOCATION = (https://maps.app.goo.gl/7uZv2gYoHdwjwWS76?g_st=com.google.maps.preview.copy)  # Shahrisabz markazi koordinatalari

# Mahsulot kategoriyalari
categories = [
    ["🍺 Ichimliklar", "🥛 Sut mahsulotlari"],
    ["🍪 Pechenyelar", "🍫 Shokoladlar"],
    ["🍜 Kunlik yeguliklar", "🍎 Mevalar"],
    ["🍨 Muzqaymoqlar", "🪙 Gigiyena vositalari"],
    ["🚿 Tozalash vositalari"],
    ["🔙 Orqaga"]
]

# Start komanda
def start(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("📍 Manzilni ko‘rish")], *categories]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("Assalomu alaykum! Kategoriyani tanlang yoki manzilni ko‘ring.", reply_markup=reply_markup)

# Lokatsiya yuborish
def send_location(update: Update, context: CallbackContext):
    update.message.reply_location(latitude=STORE_LOCATION[0], longitude=STORE_LOCATION[1])
    update.message.reply_text("Do‘konimiz manzili shu yerda!")

# Xabarlarni qayta ishlash
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    if text == "📍 Manzilni ko‘rish":
        send_location(update, context)
    elif text in sum(categories, []):
        update.message.reply_text(f"Siz {text} tanladingiz. Hozircha mahsulotlar mavjud emas.")
    elif text == "🔙 Orqaga":
        start(update, context)
    else:
        update.message.reply_text("Noto‘g‘ri buyruq, iltimos, menyudan tanlang.")

# Botni ishga tushirish
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()
