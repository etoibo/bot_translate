from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

til = InlineKeyboardMarkup(
    inline_keyboard = [
    	[
    	InlineKeyboardButton(text = '🇺🇿 Uzbekcha', callback_data='uz'),
    	InlineKeyboardButton(text = '🇷🇺 Russian', callback_data='ru')
    	],
    	[
    	InlineKeyboardButton(text = '🇺🇸 English', callback_data='us'),
    	InlineKeyboardButton(text = '🇸🇦 Arabish', callback_data='ar')
    	],
    	[
    	InlineKeyboardButton(text = '🇹🇷 Turkish', callback_data='tr'),
    	InlineKeyboardButton(text = '🇮🇳 Indish', callback_data='in')
    	],
    	[
    	InlineKeyboardButton(text = '🇰🇷 Korean', callback_data='kr'),
    	InlineKeyboardButton(text = '🇰🇿 Kazakcha', callback_data='kz')
        ],
        [
        InlineKeyboardButton(text = '🇩🇪 German', callback_data='ge'),
        InlineKeyboardButton(text = '🇫🇷 French', callback_data='fr')
        ],
        [
        InlineKeyboardButton(text = '🇰🇬 Kyrgz', callback_data='ky'),
        InlineKeyboardButton(text = '🇵🇱 Polish', callback_data='pl')
        ],
        [
        InlineKeyboardButton(text = '🇹🇯 Tajik', callback_data='tj'),
        InlineKeyboardButton(text = '🇺🇦 Ukrainian', callback_data='ukr')
        ],
        [
        InlineKeyboardButton(text = '🇧🇬 Bulgarian', callback_data='bul'),
        InlineKeyboardButton(text = '🇫🇮 Filipino', callback_data='fi')
        ],
        [
        InlineKeyboardButton(text = '🇬🇦 Irish', callback_data='ir'),
        InlineKeyboardButton(text = '🇱🇦 Latin', callback_data='lat')
    	],
    ],
)