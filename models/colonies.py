from models.ants import Worker


class Colony:
    def __init__(self, map, name, ant_colour):
        self.map = map
        self.name = name
        self.ant_colour = ant_colour
        self.ants = []

    def birth_ant(self, ant_class=Worker):
        new_ant = ant_class(colony=self, colour=self.ant_colour)
        self.ants.append(new_ant)
        self.map.add_sprite(new_ant)

    def update(self):
        for ant in self.ants:
            nearest_leaf = self.map.get_nearest_object_by_type(ant, "Leaf")
            if not nearest_leaf:
                ant.destination_coordinates = None
                continue
            distance_to_nearest_leaf = self.map.get_distance_between_objects(ant, nearest_leaf)
            if ant.rect.colliderect(nearest_leaf.rect):  # The ant collides with the leaf
                self.map.remove_sprite(nearest_leaf)
                ant.collide(nearest_leaf)
            elif distance_to_nearest_leaf <= ant.vision:  # The ant is close enough to see the leaf
                ant.speed = ant.max_speed
                ant.destination_coordinates = (nearest_leaf.x_pos, nearest_leaf.y_pos)
            else:  # The ant can't see any leaf. It has no specific destination
                ant.destination_coordinates = None
                ant.speed = ant.max_speed
