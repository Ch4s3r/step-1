controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    spritePlayer.left = spritePlayer.left - spritePlayer.width
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    spritePlayer.left = spritePlayer.left + spritePlayer.width
})
let spritePlayer: Sprite = null
scene.setBackgroundColor(1)
spritePlayer = sprites.create(assets.image`george`, SpriteKind.Player)
spritePlayer.bottom = scene.screenHeight() - 3
spritePlayer.setBounceOnWall(true)
