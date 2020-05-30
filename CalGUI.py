import wx


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
        calc_btn = wx.Button(self, wx.ID_ANY, "計算")
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(calc_text, 1)
        layout.Add(calc_btn)
        self.SetSizer(layout)


class PanelResult(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        resultlabel = wx.StaticText(self, wx.ID_ANY, "結果:")
        result_text = wx.TextCtrl(self, wx.ID_ANY, size=(280, 20))
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(resultlabel)
        layout.Add(result_text)
        self.SetSizer(layout)


if __name__ == '__main__':

    # カスタムフレームを初期化してアプリケーションを開始
    application = wx.App()
    frame = CalcFrame()
    frame.Show()
    application.MainLoop()
