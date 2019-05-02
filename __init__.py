from mycroft import MycroftSkill, intent_file_handler


class PlantWaterLevel(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('level.water.plant.intent')
    def handle_level_water_plant(self, message):
        self.speak_dialog('level.water.plant')


def create_skill():
    return PlantWaterLevel()

