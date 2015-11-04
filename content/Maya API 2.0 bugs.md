Title: Maya Python API 2.0 bug
Date: 2015-11-4 11:13
Category: Maya Python API
Tags: Maya Python API, Maya, Python
Author: Mack Stone
Summary: Python API 2.0 bug

有一段时间没使用Maya了，前段时间想到个问题，想快速的测试一下，然后发现了这个bug。

    #!python
    import maya.api.OpenMaya as om
    ball = cmds.polySphere()
    sellist = om.MSelectionList().add(ball[0])
    
    mpIt = om.MItMeshPolygon(sellist.getDagPath(0))
    
    while not mpIt.isDone():
        print mpIt.index()
        mpIt.next()

执行上面的命令你会得到一个报错

    :::python
    # Error: line 1: TypeError: file <maya console> line 8: next() takes exactly one argument (0 given) #

很明显的一个bug，*next()* 肯定是不需要任何参数的，这个bug存在Maya2015和2016