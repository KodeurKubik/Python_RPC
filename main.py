# ====== ====== #
app_id = "PUT YOUR APP ID HERE"

details = "A text"
state = "Another text but below the details"

big_text = "A text that is displayed when the mouse is on the big image"
small_text = "A text that is displayed when the mouse is on the small image"

big_img = "The name of the big image"
small_img = "The name of the big image"

buttons = [
        { "label": "A text", "url": "http://example.com" },
        { "label": "Another text", "url": "http://example.com" }
] # Notice that you can't click on the buttons on your profile
# ====== ====== #

if app_id == "PUT YOUR APP ID HERE":
  app_id = prompt('Enter your app id here please: ')

import time
from pypresence import Presence

RPC = Presence(app_id)
RPC.connect()


RPC.update(
    details = details,
    state = state,
    large_image = big_img,
    large_text = big_text,
    small_image = small_img,
    small_text = small_text,
    buttons = buttons
)

while True:
    time.sleep(15)
