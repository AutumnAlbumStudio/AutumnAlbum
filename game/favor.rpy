# 您可以在此编写游戏的脚本。
# Favor 好感度显示窗口
screen favor_icon():
    zorder 50

    frame:
        background None
        padding(10, 10)
        xalign 1.0
        vbox:
            imagebutton auto "images/btn/heart_%s.png" action ShowTransient('favor')

screen favor():
    zorder 100

    frame:
        xfill True
        yfill True
        # background  None
        margin(50, 50)
        grid 4 2:
            xfill True
            yfill True
            vbox:
                xalign 0.5
                frame:
                    background  None
                    margin(0, 30, 0, 0)
                    add im.Scale("images/avatar/avatar bmm square.png", 200, 200)
                    # background  Frame("images/avatar/avatar yaa square.png")
                    # padding(50, 50)
                    xalign 0.5
                frame:
                    background  None
                    xalign 0.5
                    text "bmm"
                frame:
                    background  None
                    xalign 0.5
                    text "好感度:0"
            vbox:
                xalign 0.5
                frame:
                    background  None
                    margin(0, 30, 0, 0)
                    add im.Scale("images/avatar/avatar yaa square.png", 200, 200)
                    xalign 0.5
                frame:
                    background  None
                    xalign 0.5
                    text "djc"
                frame:
                    background  None
                    xalign 0.5
                    text "好感度:0"
            vbox:
                xalign 0.5
                frame:
                    background  None
                    margin(0, 30, 0, 0)
                    add im.Scale("images/avatar/avatar yaa square.png", 200, 200)
                    xalign 0.5
                frame:
                    background  None
                    xalign 0.5
                    text "dyx"
                frame:
                    background  None
                    xalign 0.5
                    text "好感度:0"
            vbox:
                xalign 0.5
                frame:
                    background  None
                    margin(0, 30, 0, 0)
                    add im.Scale("images/avatar/avatar yaa square.png", 200, 200)
                    xalign 0.5
                frame:
                    background  None
                    xalign 0.5
                    text "ncj"
                frame:
                    background  None
                    xalign 0.5
                    text "好感度:0"
            vbox:
                xalign 0.5
                frame:
                    background  None
                    margin(0, 30, 0, 0)
                    add im.Scale("images/avatar/avatar sklt square.png", 200, 200)
                    xalign 0.5
                frame:
                    background  None
                    xalign 0.5
                    text "ktt"
                frame:
                    background  None
                    xalign 0.5
                    text "好感度:0"
            vbox:
                xalign 0.5
                frame:
                    background  None
                    margin(0, 30, 0, 0)
                    add im.Scale("images/avatar/avatar yaa square.png", 200, 200)
                    xalign 0.5
                frame:
                    background  None
                    xalign 0.5
                    text "yaa"
                frame:
                    background  None
                    xalign 0.5
                    text "好感度:0"
            vbox:
                xalign 0.5
                frame:
                    background  None
                    margin(0, 30, 0, 0)
                    add im.Scale("images/avatar/avatar yaa square.png", 200, 200)
                    xalign 0.5
                frame:
                    background  None
                    xalign 0.5
                    text "zgt"
                frame:
                    background  None
                    xalign 0.5
                    text "好感度:0"
            vbox:
                xalign 0.5
                frame:
                    background  None
