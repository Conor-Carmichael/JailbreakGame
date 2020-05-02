
#################################################################
#                                                               #
#                                                               #
#        The protagonist class in the jaibreak game.            #
#                                                               #
#                                                               #
#################################################################

from Character import Character


class Protagonist(Character):

    def __init__(self, position, step, size):
        super().__init__(position, step, size)
        self.id = 'protagonist'
        self.has_key = False
        self.mvmnt_speed = 10
        self.dash_cooldown = None

        # What else can I implement?
        # Health, items, ...


    