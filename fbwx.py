#!/usr/bin/env python3
import os
import wx

class FileDrop(wx.FileDropTarget):

    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        for fontpath in filenames:
            try:
                print('fontpath = ',fontpath)
                print('fontbakery check-googlefonts ' + fontpath + ' -l WARN --ghmarkdown ~/Desktop/fontbakery-report.md')
                os.system('fontbakery check-googlefonts ' + fontpath + ' -l WARN --ghmarkdown ~/Desktop/fontbakery-report.md')
                #file = open(name, 'r')
                #text = file.read()
                #self.window.WriteText(text)
            except IOError as error:
                msg = "Error opening file\n {}".format(str(error))
                dlg = wx.MessageDialog(None, msg)
                dlg.ShowModal()
                return False
            except UnicodeDecodeError as error:
                msg = "Cannot open non ascii files\n {}".format(str(error))
                dlg = wx.MessageDialog(None, msg)
                dlg.ShowModal()
                return False
            finally:
                print("Done :-)")
                #file.close()
        return True

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        self.text = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        dt = FileDrop(self.text)
        self.text.SetDropTarget(dt)
        self.SetTitle('File drag and drop')
        self.Centre()

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
