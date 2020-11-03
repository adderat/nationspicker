import random
from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set('graphics', 'width', '540')
Config.set('graphics', 'height', '960')
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 100)
Config.set('graphics', 'top', 100)


class Mymainpage(Screen):
    pass


class Myresults(Screen):
    pass


class Mymanager(ScreenManager):
    playerslider = ObjectProperty(None)
    china = ObjectProperty(None)
    egypt = ObjectProperty(None)
    greece = ObjectProperty(None)
    persia = ObjectProperty(None)
    rome = ObjectProperty(None)
    america = ObjectProperty(None)
    arabs = ObjectProperty(None)
    ethiopia = ObjectProperty(None)
    india = ObjectProperty(None)
    japan = ObjectProperty(None)
    korea = ObjectProperty(None)
    mali = ObjectProperty(None)
    mongolia = ObjectProperty(None)
    poland = ObjectProperty(None)
    portugal = ObjectProperty(None)
    venice = ObjectProperty(None)
    vikings = ObjectProperty(None)
    britain = ObjectProperty(None)
    carthage = ObjectProperty(None)
    france = ObjectProperty(None)
    holy = ObjectProperty(None)
    hungary = ObjectProperty(None)
    inca = ObjectProperty(None)
    khmer = ObjectProperty(None)
    netherlands = ObjectProperty(None)
    ottoman = ObjectProperty(None)
    russia = ObjectProperty(None)
    spain = ObjectProperty(None)
    pickedteamsstring = StringProperty()

    def randomizeteams(self):
        numplayer = self.ids.main.playerslider.value
        activeteams = []
        teams = [
            "china",
            "egypt",
            "greece",
            "persia",
            "rome",
            "america",
            "arabs",
            "ethiopia",
            "india",
            "japan",
            "korea",
            "mali",
            "mongolia",
            "poland",
            "portugal",
            "venice",
            "vikings",
            "britain",
            "carthage",
            "france",
            "holy",
            "hungary",
            "inca",
            "khmer",
            "netherlands",
            "ottoman",
            "russia",
            "spain"
        ]
        for team in teams:
            a = getattr(self.ids.main, team)
            if a.state == "normal":
                activeteams.append(a.text)

        random.shuffle(activeteams)
        random.shuffle(activeteams)

        pickedteams = []
        for player in range(0, numplayer):
            pickedteams.append(activeteams[player])

        self.pickedteamsstring = ""
        for item in pickedteams:
            self.pickedteamsstring = self.pickedteamsstring + "\n" + item
        print(self.pickedteamsstring)

        return


class Nationspicker(App):
    def build(self):
        return


if __name__ == "__main__":
    Nationspicker().run()
