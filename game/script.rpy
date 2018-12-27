define qiu = Character('秋小姐', color="#c8ffc8")
define sklt = Character('Scarlet', color="#c8c8ff")

label start:
    scene bg sjtu eastgate
    with fade
    "开学了，又到了秋色宜人的季节。"
    show qiu back with dissolve
    "早早被钦定为临召的秋小姐来到了SJTU。"
    qiu "我就是在这样的风景环绕之中成长起来的，这里的秋天格外秀美。"
    qiu "童年时，我经常在高贵的THU里和学长学姐们谈笑风生，对这所SJTU充斥着鄙夷。"
    qiu "初中以来，我无数次设想过我未来在THU中的快乐生活。"
    qiu "却不曾想到在领军计划与高考中我大意失荆州……"
    qiu "也罢，不知道这里的同学会和THU的同学们有多大的差距呢？"
    "正在秋小姐回忆过往之时，迎面走来了一位什么都不会的魔法少女。"
    show qiu back:
        ease 0.5 left
    show scarlet happy at right with dissolve
    "原来是早在 QQ 群中结识的 Scarlet。"
    sklt "嗯呣……你是否可以……"

label courseChosing:
    scene bg painted ji
    with dissolve
    "秋小姐早就知道，进入JI的第一件事就是选课。"
    "VV186(Honors Mathmatics) 是最难的数学，像秋小姐这样水平的学生一定要选上。"
    "至于 VG101(Intro to Programming) 和 vg100(Intro to Engineering) , 熟悉的学长学姐们都推荐精通programming的秋小姐先学VG100。"
    "剩下的 VC210(Chemistry) 以及 VY100(Academic Writing) 应该很轻松就能搞定。。。"
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
    qiu "等小飞机转进去的时候好多课程的已选人数已经快要达到人数上限了。。。"
    python:
        REQUIRED_MIN_CREDIT = 16
        vg100 = False
        vg101_1 = False
        vg101_2 = False
        vc210 = False
        vv186 = False
        vy100 = False
        creditNow = 0
    while creditNow < REQUIRED_MIN_CREDIT:
        menu:
            "Course Registration\nCredit: [creditNow]/[REQUIRED_MIN_CREDIT]"
            "VG100 Intro to Engineering (40/100)" if not vg100:
                $ vg100 = True
                $ creditNow += 4
                "已选择 VG100\nCredit +4"
            "VG100 Intro to Engineering (41/100) (disabled)" if vg100:
                pass
            "VG101 Intro to Programing Jigang section (118/120)" if not vg100 and not vg101_1:
                $ vg101_1 = True
                "真不巧，这门课最后剩下的名额刚刚被选满了呢。。。"
            "VG101 Intro to Programing Jigang section (120/120) (disabled)" if vg100 or vg101_1:
                pass
            "VG101 Intro to Programing Maunel section (99/100)" if not vg100 and not vg101_2:
                $ vg101_2 = True
                "哎呀，没抢到最后的一个名额。。。"
            "VG101 Intro to Programing Maunel section (100/100) (disabled)" if vg100 or vg101_2:
                pass
            "VC210 Chemistry (180/330)" if not vc210:
                $ vc210 = True
                $ creditNow += 4
                "已选择 VC210\nCredit +4"
            "VC210 Chemistry (181/330) (disabled)" if vc210:
                pass
            "VV156 Calculus (80/160)" if not vv186:
                qiu "像我这样数学功底的学生才不需要学高数呢！"
            "VV156 Calculus (80/160) (disabled)" if vv186:
                pass
            "VV186 Honors Mathematics (120/160)" if not vv186:
                $ vv186 = True;
                $ creditNow += 4
                "已选择 VV186\nCredit +4"
            "VV186 Honors Mathematics (121/160) (disabled)" if vv186:
                pass
            "VY100 Academic Writing(Andrew Yang) (28/30)" if not vy100:
                $ vy100 = True;
                $ creditNow += 4
                "已选择 VY100\nCredit +4"
            "VY100 Academic Writing(Andrew Yang) (30/30) (disabled)" if vy100:
                pass
            # "至少要修够[REQUIRED_MIN_CREDIT]学分呢。。。。现在有[creditNow]学分了"
    qiu "呼~选课总算是结束了呢。"
    qiu "诶？有一部分课我已经都会了啊。"
    qiu "看来这学期3门A+是少不了了。"
