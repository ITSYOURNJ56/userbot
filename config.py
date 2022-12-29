# FILL THESE VALUES ACCORDINGLY.

from RomeoBot.config.hell_config import Config

class Development(Config):
  # get these values from my.telegram.org. 
  APP_ID = 15637856    # 6 is a placeholder. Fill your 6 digit api id
  API_HASH = "521a26ceed82a85420d580989373d817"   # replace this with your api hash

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "mongodb+srv://itmebro:itsnj@cluster1.685hnrh.mongodb.net/?retryWrites=true&w=majority"

  # After cloning the repo and installing requirements...
  # Do `python string.py` and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  ROMEOBOT_SESSION = "1BVtsOHEBu7eBGFgaeiorJ11EJibe68jJBWcuF2EYm9lDA6NyPHSU7asDFdulpZQbwXIHnUTGmWGnVO3_W-2HDhpzP-guFcwu0jj3xGCaLDBYsPIowcz00eNhBvOlg5f9Vkn3Dj9r9NIMC61I-U3OsaYsrrXM3C_nsJ2_VfrtaB9zSdAOiUfnX891zUHfXcZylksb5Tk0MgyUoL6aVtoS_MHvXbf3w1p03vx5cPDoXD4_mbLXS665UStvU4iBhmHo81KI9WVIAmceJ5pQzpf_jt4v0IjRGhYXUEZWhfsANLrI_Vqdk_zLaySxmP0sbzk9SJZPdoGVHMtXSiBXfLRR8dX5HGlFY1k="

  # Create a bot in @BotFather
  # And fill the following values with bot token and username.
  BOT_TOKEN = "5824879205:AAEum45stp6RsQ1Pw272lvi7HrfDFc-IVt0" #token

  # Custom Command Handler. 
  HANDLER = "."

  # Custom Command Handler for sudo users.
  SUDO_HANDLER = "."


# end of required config
# bot
