from config import CONFIG


def user_is_irc_bot(ctx):
    return ctx.author.id == CONFIG.UWCS_DISCORD_BRIDGE_BOT_ID


def get_name_string(message):
    # if message.clean_content.startswith("**<"): <-- FOR TESTING
    if user_is_irc_bot(message):
        return message.clean_content.split(" ")[0][3:-3]
    else:
        return f"{message.author.mention}"


def pluralise(l, word, single="", plural="s"):
    if len(l) > 1:
        return word + plural
    else:
        return word + single
