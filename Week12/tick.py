# Tick class for aggregation
class Tick:
    def __init__(self):
        print("Aggregation: Tick is created")
        
    def consume_blood(self):
        print("Tick is consuming blood..")

    def _del_(self):
        print("The aggregator is destroying")