import maya.cmds as cmds


def renamer(input_string):
    num_of_chars = input_string.count("#")

    string_tuple = input_string.partition('#' * num_of_chars)

    tempName = "name"

    replaceValue = '#' * num_of_chars

    if string_tuple[1]:
        sels = cmds.ls(selection=True)
        index = 0
        for sel in sels:
            current_count = str(index)
            tempName = "00" + current_count
            cmds.rename(string_tuple[0] + tempName + string_tuple[2])
            index += 1


    else:
        cmds.error('Input String is not valid. Please enter a name with the formatting of "Name_##_Type"')

renamer("head_##_geo")