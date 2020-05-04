
#################################################################
#                                                               #
#                                                               #
#        The protagonist class in the jaibreak game.            #
#                                                               #
#                                                               #
#################################################################

from Characters.Character import Character


class Protagonist(Character):

    def __init__(self, position, image):
        super().__init__(position, image)
        self.id = 'protagonist'
        self.has_key = False
        self.mvmnt_speed = 10
        self.dash_cooldown = None
        self.rocks = 3
        

        # What else can I implement?
        # Health, items, ...


    