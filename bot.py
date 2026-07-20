
import os
from dotenv import load_dotenv

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from game import create_board, make_move, check_winner
from ai import bot_move


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

games = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    games[user_id] = create_board()

    await update.message.reply_text(
        "🎮 Astra TicTacToe\n\n"
        "تو ❌ هستی\n"
        "ربات ⭕ است\n\n"
        "شروع کن:",
        reply_markup=board_keyboard(games[user_id])
    )


def board_keyboard(board):
    keyboard = []

    for i in range(3):
        row = []
        for j in range(3):
            value = board[i][j]

            row.append(
                InlineKeyboardButton(
                    value if value != " " else "⬜",
                    callback_data=f"{i}{j}"
                )
            )
        keyboard.append(row)

    return InlineKeyboardMarkup(keyboard)


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if user_id not in games:
        games[user_id] = create_board()


    row = int(query.data[0])
    col = int(query.data[1])


    board = games[user_id]


    if board[row][col] != " ":
        return


    make_move(board, row, col, "❌")


    winner = check_winner(board)

    if winner:
        await query.edit_message_text(
            f"🏆 برنده: {winner}"
        )
        return


    bot_move(board)


    winner = check_winner(board)

    if winner:
        await query.edit_message_text(
            f"🏆 برنده: {winner}"
        )
        return


    await query.edit_message_reply_markup(
        reply_markup=board_keyboard(board)
    )



def main():

    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        CallbackQueryHandler(play)
    )


    print("Astra TicTacToe Started 🎮")

    app.run_polling()



if __name__ == "__main__":
    main()
