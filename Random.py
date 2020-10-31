import maya.cmds as cmds
import random

def DuplicateAndScatter(numOfDuplicates, minX, maxX, minY, maxY, minZ, maxZ):
    sels = cmds.ls(selection=True)

    for item in range(len(cmds.ls(selection=True))):
        index = item

        for items in range(numOfDuplicates):
            tempObj = (cmds.duplicate(sels[index], rr=True))
            randX = random.uniform(minX, maxX)
            randY = random.uniform(minY, maxY)
            randZ = random.uniform(minZ, maxZ)

            cmds.select(tempObj)
            cmds.xform(worldSpace=True, translation=[randX, randY, randZ])


DuplicateAndScatter(3, -5, 5, -.5, .5, -5, 5)

