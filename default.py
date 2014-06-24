import xbmc
import xbmcgui
import sys
import monitorext

debug = True
remote = False
if debug:
    if remote:
        sys.path.append(r'C:\\Users\\Ken User\\AppData\\Roaming\\XBMC\\addons\\script.ambibox\\resources\\lib\\pycharm-debug.py3k\\')
        import pydevd
        pydevd.settrace('192.168.1.103', port=51234, stdoutToServer=True, stderrToServer=True)
    else:
        sys.path.append('C:\Program Files (x86)\JetBrains\PyCharm 3.1.3\pycharm-debug-py3k.egg')
        import pydevd
        pydevd.settrace('localhost', port=51234, stdoutToServer=True, stderrToServer=True)


def notification(text):
    """
    Display an XBMC notification box
    @type text: str
    """
    text = text.encode('utf-8')
    dialog = xbmcgui.Dialog()
    dialog.notification('MonitorEx', text)


class MyPlayer(xbmc.Player):
    def __init__(self):
        super(MyPlayer, self).__init__()

    def onPlayBackStartedEx(self):
        notification('Playback Started')


class MyMonitor(monitorext.MonitorEx):

    def __init__(self, monitorStereoMode, monitorProfiles, monitorPlayback, player):
        """
        @type monitorStereoMode: bool
        @type monitorProfiles: bool
        @type monitorPlayback: bool
        @type player: xbmc.Player()
        """
        monitorext.MonitorEx.__init__(self, monitorStereoMode, monitorProfiles, monitorPlayback)
        self.player = player

    def onStereoModeChange(self):
        mode = self.getCurrentStereoMode()
        notification('StereoMode changed to %s' % mode)

    def onProfileChange(self):
        prfl = self.getCurrentProfile()
        notification('Profile changed to %s' % prfl)

    def onPlaybackStarted(self):
        self.player.onPlayBackStartedEx()

"""
class MyMonitor(monitorext.MonitorEx):

    def __init__(self, monitorStereoMode, monitorProfiles, monitorPlayback):
        monitorext.MonitorEx.__init__(self, monitorStereoMode, monitorProfiles, monitorPlayback)
        self.player = player

    def onStereoModeChange(self):
        mode = self.getCurrentStereoMode()
        notification('StereoMode changed to %s' % mode)

    def onProfileChange(self):
        prfl = self.getCurrentProfile()
        notification('Profile changed to %s' % prfl)

    def onPlaybackStarted(self):
        notification('Playback started')
"""


def Main():
    try:
        player = MyPlayer()

        mm = MyMonitor(monitorStereoMode=True, monitorProfiles=True, monitorPlayback=True, player=player)
        # mm = MyMonitor(monitorStereoMode=True, monitorProfiles=True, monitorPlayback=True)

        mm.Listen(interval=1000, stereoInterval=500)

        while not xbmc.abortRequested:
            xbmc.sleep(250)

        mm.StopListening()
        del mm
        del player
    except Exception, e:
        pass

Main()

