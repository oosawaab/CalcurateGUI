import wx


def click_btn(event):
    siki = KakkoYusen(CalText[0].GetValue())
    print("式", siki)
    Clear()
    answer = PlusMinus(siki)
    # answer = PlusMinus(CalText[0].GetValue())
    CalText[1].SetValue(str(answer))
    print("答え", answer, type(answer))
    print("入力値", Regsterlist)
    print("演算", NumEnzanlist)
    print("掛け算割り算", MulDivlist)
    Clear()


def Regster(String):
    i = 0
    while String[i] != "=":
        Regsterlist.append(String[i])
        i = i + 1
    Regsterlist.append("=")


def NumRegster(String):
    Regster(String)
    i = 0
    while i < len(Regsterlist):
        if '0' <= Regsterlist[i] <= '9':
            num = ""
            j = i
            while j < len(Regsterlist):
                if '0' <= Regsterlist[j] <= '9' or Regsterlist[j] == ".":
                    num = num + Regsterlist[j]
                elif Regsterlist[j] == " ":
                    i = j - 1
                    break
                j = j + 1
            NumEnzanlist.append(num)
        else:
            NumEnzanlist.append(Regsterlist[i])

        i = i + 2


def MulDiv(String):
    NumRegster(String)
    result = 1.0
    i = 0
    # False:掛け算と割り算が1回以上行われたTrue:掛け算と割り算が1回も行われてない
    loop = True
    while i < len(NumEnzanlist):
        if NumEnzanlist[i] == "*":
            if loop:
                result = float(NumEnzanlist[i - 1])
            result = result * float(NumEnzanlist[i + 1])
            loop = False
        elif NumEnzanlist[i] == "/":
            if loop:
                result = float(NumEnzanlist[i - 1])
            result = result / float(NumEnzanlist[i + 1])
            loop = False
        elif NumEnzanlist[i] == "+" or NumEnzanlist[i] == "-" or NumEnzanlist[i] == "=":
            if loop:
                result = float(NumEnzanlist[i - 1])
            MulDivlist.append(result)
            MulDivlist.append(NumEnzanlist[i])
            loop = True
        i = i + 1
# 5 - 2 * 3 / 4 + 2 =


def PlusMinus(String):
    MulDiv(String)
    i = 0
    result = 0.0
    loop = True
    while i < len(MulDivlist):
        if MulDivlist[i] == "+":
            if loop:
                result = MulDivlist[i - 1]
            result = result + MulDivlist[i + 1]
            loop = False
        elif MulDivlist[i] == "-":
            if loop:
                result = MulDivlist[i - 1]
            result = result - MulDivlist[i + 1]
            loop = False
        elif MulDivlist[i] == "=":
            # print("答えは、", result)
            if loop:
                result = MulDivlist[i - 1]
            return result
        i = i + 1

# 4 - 2 * 5 + 2.5 * 4 - 7 =


def Clear():
    Regsterlist.clear()
    NumEnzanlist.clear()
    MulDivlist.clear()


def KakkoYusen(String):  # ( 1 + 2 ) * 3 - 2 =
    i = 0
    siki = ""
    # print("GET式", String)
    while String[i] != "=":
        print("String", i, String[i])
        if String[i] == "(":
            Clear()
            j = i + 2  # j=2:String[2] = 1
            value = ""
            while String[j] != ")":
                value = value + String[j]
                j = j + 1

            value = value + "="
            # print("value", value, PlusMinus(value))
            siki = siki + str(PlusMinus(value))  # ()計算
            i = j
        else:
            Clear()
            # print("value", String[i], i)
            siki = siki + String[i]
        i = i + 1
        # print("siki", siki, "i=", i)
    siki = siki + "="
    return siki


# ( 12 + 56 ) / 34 -9 =
# 12 + 56 = 58.0


class CalcFrame(wx.Frame):
    """
    フレームを継承したトップレベルウィンドウクラス
    """

    def __init__(self):

        super().__init__(None, wx.ID_ANY, '計算レイアウト', size=(300, 280))
        root_panel = wx.Panel(self, wx.ID_ANY)
        panel_label = Label(root_panel)
        panel_in = Panelin(root_panel)
        panel_result = PanelResult(root_panel)
        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(panel_label)
        root_layout.Add(panel_in)
        root_layout.Add(panel_result)
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)


class Label(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        calclabel = wx.StaticText(self, wx.ID_ANY, "計算式を入力しください。")
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(calclabel)
        self.SetSizer(layout)


class Panelin(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        calc_text = wx.TextCtrl(self, wx.ID_ANY, size=(200, 20))
        CalText.append(calc_text)
        calc_btn = wx.Button(self, wx.ID_ANY, "計算")
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(calc_text, 1)
        layout.Add(calc_btn)
        self.SetSizer(layout)
        calc_btn.Bind(wx.EVT_BUTTON, click_btn)


class PanelResult(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        resultlabel = wx.StaticText(self, wx.ID_ANY, "結果:")
        result_text = wx.TextCtrl(self, wx.ID_ANY, size=(280, 20))
        CalText.append(result_text)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(resultlabel)
        layout.Add(result_text)
        self.SetSizer(layout)


if __name__ == '__main__':

    # カスタムフレームを初期化してアプリケーションを開始
    CalText = []
    Regsterlist = []  # 入力値を配列に登録
    NumEnzanlist = []  # 数値を演算子を配列を登録
    MulDivlist = []  # 掛け算と割り算計算して登録
    PlusMinulist = []  # 足し算引き算を計算して登録
    Sikilist = []  # かっこの中のリスト
    application = wx.App()
    frame = CalcFrame()
    frame.Show()
    application.MainLoop()
