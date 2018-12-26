define qiu = Character('秋小姐', color="#c8ffc8")
define sklt = Character('Scarlet', color="#c8c8ff")
define MINCREDIT = 12

label start:
    scene bg sjtu eastgate
    with fade
    "开学了，又到了秋色宜人的季节。"
    show qiu back with dissolve
    "早早被钦定为临召的秋小姐来到了SJTU。"
    qiu "我就是在这样的风景环绕之中成长起来的。这里的秋天格外秀美。"
    qiu "童年时，我经常在高贵的THU里玩耍，所以对着这所垃圾SJTU充斥着鄙夷。"
    show qiu back:
        ease 0.5 left
    show scarlet happy at right with dissolve
    sklt "嗯呣……你是否可以……"

label CourseChosing:
    scene bg painted ji
    with dissolve
    "秋小姐早就知道，进入JI的第一件事就是选课。"
    "Vv186（Honors Mathmatics)是最难的数学，像秋小姐这样水平的学生一定要选上。"
    "至于Vg101(Intro to programming) 和 Vg100(Intro to engineering), 熟悉的学长们都推荐精通编程的秋小姐先学工导。"
    "剩下的Vc210（化学）应该很轻松就能搞定。。。"
    window hide 
    show ani plane1
    pause 0.05
    show ani plane2
    pause 0.05
    show ani plane3
    pause 0.05
    show ani plane4
    pause 0.05
    show ani plane5
    pause 0.05
    show ani plane6
    pause 0.05
    show ani plane7
    pause 0.05
    show ani plane8
    pause 0.05
    show ani plane9
    pause 0.05
    show ani plane10
    pause 0.05
    show ani plane11
    pause 0.05
    show ani plane12
    pause 0.05
    show ani plane13
    pause 0.05
    show ani plane14
    pause 0.05
    show ani plane15
    pause 0.05
    show ani plane16
    pause 0.05
    show ani plane17
    pause 0.05
    show ani plane18
    pause 0.05
    window auto
    "小飞机转进去的时候可以选的课已经没多少了呢。。。。"
    python:
        Vg101_1 = False
        Vg101_2 = False
        Vg100 = False
        Vc210 = False
        Vy100 = False
        Vv186 = False
        Vv156 = False
        credit = 0
    while credit < MINCREDIT:
        menu:
            "Course Registration\r\n
            Credit: [credit]/[MINCREDIT]" 
            "Vg100 Intro to Engineering 40/100" if not Vg100:
                $ Vg100 = True
                $ credit += 4
                "已选择 Vg100"
            # "Vg100 Intro to Engineering 41/100 selected"(what_color="#71E346") if Vg100:
                # pass
            "Vg101 Intro to Programing jigang section 120/120":
                "这个课已经满了呢。。。"
            "Vg101 Intro to Programing Maunel section 100/100":
                "这个课已经满了呢。。。"
            "Vc210 Chemistry 180/330" if not Vc210:
                $ Vc210 = True
                $ credit+=4
                "已选择 Vc210"
            # "Vc210 Chemistry 180/330"(what_color="#71E346")if Vc210:
                # pass
            "vv156 Calculus 80/160":
                "像我这样数学功底的学生才不需要学高数呢"
            "Vv186 Honors Mathematics 120/160" if not Vv186:
                $ Vv186 = True;
                $credit += 4
                "已选择 Vv86"
            # "Vv186 Honors Mathematics 120/160"(what_color="#71E346") if Vv186:
                # pass        "至少要修够[MINCREDIT]学分呢。。。。现在有[credit]学分了"
    