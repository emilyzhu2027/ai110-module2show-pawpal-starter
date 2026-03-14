from dataclasses import dataclass
from typing import List

@dataclass
class Pet:
    name: str
    type: str
    age: int

@dataclass
class Task:
    title: str
    durationHrs: int
    priority: str
    type: str
    pet: Pet
    ifCompleted: bool

    def complete(self):
        pass

@dataclass
class Owner:
    name: str
    pets: List[Pet]
    hrs_available: int
    tasks: List[Task]

    def addPet(self, pet: Pet):
        pass

    def removePet(self, pet: Pet):
        pass

    def getPets(self) -> List[Pet]:
        pass

    def getTasks(self) -> List[Task]:
        pass

    def addTask(self, task: Task):
        pass

    def removeTask(self, task: Task):
        pass

@dataclass
class Scheduler:
    owner: Owner
    tasks: List[Task]

    def generatePlan(self):
        pass
