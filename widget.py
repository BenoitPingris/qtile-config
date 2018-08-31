from libqtile import widget
import math

class Volume(widget.Volume):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icons_vol = {
            'mute': '',
            'low': '',
            'high': ''
        }

    def _update_drawer(self):
        c = ''
        volume = ' {}%'.format(self.volume)
        if self.volume > 50:
            c = self.icons_vol['high']
        elif self.volume > 0:
            c = self.icons_vol['low']
        elif self.volume > -10:
            c = self.icons_vol['mute']
            volume = 'x'
        self.text = '{} {}'.format(c, volume)


class Battery(widget.Battery):
    def _get_text(self):
        info = self._get_info()
        if info is False:
            return '---'
        if info['full']:
            no = math.floor(info['now'] / info['full'] * 100)
        else:
            no = 0
        if info['stat'] == 'Discharging':
            char = self.discharge_char
            if no < 20:
                self.layout.colour = self.low_foreground
            else:
                self.layout.colour = self.foreground
        elif info['stat'] == 'Charging':
            char = self.charge_char
            #elif info['stat'] == 'Unknown':                                         
        else:
            char = '■'
        return '{} {}{}'.format(char, no, '%')#chr(0x1F506)) 
        
class Backlight(widget.Backlight):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def poll(self):
        info = self._get_info()
        if not info:
            return 'Error'
        percent = info['brightness'] / info['max']
        return ''+self.format.format(percent=percent)
