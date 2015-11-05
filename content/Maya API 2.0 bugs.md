Title: Maya Python API 2.0 bug
Date: 2015-11-4 11:13
Modified: 2015-11-4 10:52
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
    # Error: line 1: TypeError: file <maya console> line 9: next() takes exactly one argument (0 given) #

很明显的一个bug，*next()* 肯定是不需要任何参数的，这个bug存在Maya2015和2016

既然想要做得更好，为什么还是while的用法呢，为什么就不能更pythonic，既然是Iterator为什么不能使用for呢。对于根本没有API经验而又非常熟悉python的人来说，下面的代码应该更能理解和好用

    #!python
    import maya.api.OpenMaya as om
    ball = cmds.polySphere()
    sellist = om.MSelectionList().add(ball[0])
    
    mpIt = om.MItMeshPolygon(sellist.getDagPath(0))
    
    for mp in mpIt:
        print mp.index()