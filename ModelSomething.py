import maya.cmds as cmds

cmds.polySphere(name = "bulb", radius=1, subdivisionsX = 8, subdivisionsY = 8)

cmds.select("bulb.f[0:7]", "bulb.f[48:55]")

cmds.scale(0.7, 1.3, 0.7)

cmds.select("bulb.f[48:55]")

cmds.polyExtrudeFacet(constructionHistory=1, translate= [0.0, -.5, 0.0])

cmds.select("bulb.f[48:55]", "bulb.f[64:71]")

cmds.polyExtrudeFacet(constructionHistory=1, scale= [.88, 1, .88])

cmds.select("bulb.vtx[8:15]")

cmds.scale(1.2,1,1.2)

