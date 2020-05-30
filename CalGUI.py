import wx


class CalcFrame(wx.Frame):
    """
    フレームを継承したトップレベルウィンドウクラス
    """

    def __init__(self):

        super().__init__(None, wx.ID_ANY, '計算レイアウト', size=(300, 280))
        root_panel = wx.Panel(self, wx.ID_ANY)
        root_layout = wx.BoxSizer(wx.VERTICAL)
        # root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)


if __name__ == '__main__':

    # カスタムフレームを初期化してアプリケーションを開始
    application = wx.App()
    frame = CalcFrame()
    frame.Show()
    application.MainLoop()
