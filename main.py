def on_b_pressed():
    sprites.destroy(spritePlayer)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global spritePlayer
    spritePlayer = sprites.create(assets.image("""
        george
    """), SpriteKind.player)
    spritePlayer.left = spritePlayer.width * 4
    spritePlayer.bottom = scene.screen_height()
    spritePlayer.say_text(spritePlayer.left, 500, False)
    spritePlayer.set_bounce_on_wall(True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    spritePlayer.x += spritePlayer.width * -1
    spritePlayer.x = 0
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    spritePlayer.x += spritePlayer.width * 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

spritePlayer: Sprite = None
scene.set_background_color(1)
spritePlayer = sprites.create(assets.image("""
    george
"""), SpriteKind.player)
spritePlayer.left = spritePlayer.width * 4.5
spritePlayer.bottom = scene.screen_height() - 3
spritePlayer.say_text(spritePlayer.left, 500, False)
spritePlayer.set_bounce_on_wall(True)