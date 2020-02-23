from discord.ext import commands
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjgwOTU1MTQ3MDk0MTk2MjQ0.XlHctA.dwJgCPJk9utj_MUqfwnH53IfqHM'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「!sensi」と発言したら「mouce sensitivity(URL)」が返る処理
    if message.content == '!sensi':
        await message.channel.send('他ゲームとのマウスの感度を揃えたいならココ！(※一部課金必※)\nhttps://www.mouse-sensitivity.com')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
