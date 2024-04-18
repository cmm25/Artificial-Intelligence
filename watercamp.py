class Container:
    def __init__(self, capacity, current_amount=0):
        self.capacity = capacity
        self.current_amount = current_amount

    def fill(self):
        self.current_amount = self.capacity

    def empty(self):
        self.current_amount = 0

    def pour_into(self, other_container):
        available_space = other_container.capacity - other_container.current_amount
        if available_space >= self.current_amount:
            other_container.current_amount += self.current_amount
            self.empty()
        else:
            self.current_amount -= available_space
            other_container.current_amount = other_container.capacity

    def __str__(self):
        return f"{self.current_amount}/{self.capacity}"


def get_steps_to_target(target_amount, container1, container2):
    steps = []
    visited = set()
    while container1.current_amount != target_amount and container2.current_amount != target_amount:
        if (container1.current_amount, container2.current_amount) in visited:
            return ["No solution found!"]
        visited.add((container1.current_amount, container2.current_amount))

        if container1.current_amount == 0:
            container1.fill()
            steps.append(f"Fill the {container1.capacity} liter container ({container1})")
        elif container2.current_amount == container2.capacity:
            container2.empty()
            steps.append(f"Empty the {container2.capacity} liter container ({container2})")
        else:
            container1.pour_into(container2)
            steps.append(f"Pour water from the {container1.capacity} liter container ({container1}) to the {container2.capacity} liter container ({container2})")
    return steps


# Initialize containers
container1 = Container(11)
container2 = Container(7)

# Target amount of water 
target_amount = 3

# Get steps to obtain the target amount of water
steps = get_steps_to_target(target_amount, container1, container2)

# Print steps
for step in steps:
    print(step)