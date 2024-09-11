class Ant:
    def __init__(self, position):
        self.hunger = 0
        self.thirst = 0
        self.position = position  # Position could be a tuple (x, y)
    
    def eat(self, food_amount):
        self.hunger -= food_amount
        if self.hunger < 0:
            self.hunger = 0

    def drink(self, water_amount):
        self.thirst -= water_amount
        if self.thirst < 0:
            self.thirst = 0

    def move_towards(self, target_position):
        # Simple movement logic; adjust as needed
        if self.position[0] < target_position[0]:
            self.position = (self.position[0] + 1, self.position[1])
        elif self.position[0] > target_position[0]:
            self.position = (self.position[0] - 1, self.position[1])
        
        if self.position[1] < target_position[1]:
            self.position = (self.position[0], self.position[1] + 1)
        elif self.position[1] > target_position[1]:
            self.position = (self.position[0], self.position[1] - 1)

    def check_and_move(self, food_position, water_position):
        if self.hunger > 10:
            self.move_towards(food_position)
        elif self.thirst > 10:
            self.move_towards(water_position)

    def status(self):
        return f"Hunger: {self.hunger}, Thirst: {self.thirst}, Position: {self.position}"

# Example usage:
ant1 = Ant(position=(0, 0))
food_position = (10, 10)
water_position = (5, 5)

ant1.hunger = 15
ant1.check_and_move(food_position, water_position)
print(ant1.status())
