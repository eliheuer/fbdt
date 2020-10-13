#!/usr/bin/env python3
import os
import wx


class FileDrop(wx.FileDropTarget):

    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.window.WriteText("Drag & drop a font file here, then look for a markdown report on your desktop.")

    def OnDropFiles(self, x, y, filenames):
        for fontpath in filenames:
            try:
                print('fontpath = ',fontpath)
                os.system('fontbakery check-googlefonts ' + fontpath + ' -l WARN --ghmarkdown ~/Desktop/fontbakery-report.md')
            except IOError as error:
                msg = "Error opening file\n {}".format(str(error))
                dlg = wx.MessageDialog(None, msg)
                dlg.ShowModal()
                return False
        return True


class FontBakeryGUI(wx.Frame):

    def __init__(self, *args, **kw):
        super(FontBakeryGUI, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        self.text = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        dt = FileDrop(self.text)
        self.text.SetDropTarget(dt)
        self.SetTitle('Font Bakery Desktop GUI')
        self.Centre()


def main():

    app = wx.App()
    fb = FontBakeryGUI(None)
    fb.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
