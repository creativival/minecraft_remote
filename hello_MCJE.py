# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Edition
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello Minecraft Java Edition 1.16.5')
mc.setBlocks(-5, 63, 5,  -5, 127, 5,  param.GOLD_BLOCK)

x, y, z = -175, 4, -7
mc.setBlock(x + 1, y + 1, z + 1, param.GOLD_BLOCK)
position = mc.player.getPos()
print(position)
