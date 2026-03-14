from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Pet:
    name: str
    type: str
    age: int

@dataclass
class Task:
    title: str
    durationHrs: float
    priority: str
    type: str
    pet: Pet
    ifCompleted: bool = False

    def complete(self):
        self.ifCompleted = True

@dataclass
class Plan:
    scheduled_tasks: List[Task]
    total_time: float
    explanation: str

@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)
    hrs_available: float = 0.0
    tasks: List[Task] = field(default_factory=list)

    def addPet(self, pet: Pet):
        if pet not in self.pets:
            self.pets.append(pet)

    def removePet(self, pet: Pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def getPets(self) -> List[Pet]:
        return self.pets

    def getTasks(self) -> List[Task]:
        return self.tasks

    def addTask(self, task: Task):
        if task not in self.tasks:
            self.tasks.append(task)

    def removeTask(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)

@dataclass
class Scheduler:
    owner: Owner
    pet: Pet
    tasks: List[Task]

    def generatePlan(self) -> List[Tuple[Task, float, float]]:
        # Filter tasks for this pet, excluding completed ones
        pet_tasks = [t for t in self.tasks if t.pet == self.pet and not t.ifCompleted]
        
        # Sort by priority: high > medium > low (case-insensitive)
        priority_map = {'high': 3, 'medium': 2, 'low': 1}
        pet_tasks.sort(key=lambda t: priority_map.get(t.priority.lower(), 0), reverse=True)
        
        # Schedule tasks sequentially within available hours
        schedule = []
        current_time = 0.0
        available = self.owner.hrs_available
        
        for task in pet_tasks:
            if current_time + task.durationHrs <= available:
                start_time = current_time
                end_time = current_time + task.durationHrs
                schedule.append((task, start_time, end_time))
                current_time = end_time
        
        return schedule

    def sort_by_time(self):
        """Sorts the tasks in this scheduler by durationHrs (ascending, shortest first)."""
        self.tasks.sort(key=lambda t: t.durationHrs)

    def filterByCompletion(self, ifCompleted: bool) -> List[Task]:
        """Returns a list of tasks filtered by their completion status."""
        return [t for t in self.tasks if t.ifCompleted == ifCompleted]

    def detect_conflicts(self, schedule: List[Tuple[Task, float, float]]) -> bool:
        """Detects if there are any time conflicts (overlapping tasks) in the given schedule.
        Returns True if conflicts exist, False otherwise."""
        if not schedule:
            return False
        
        # Sort the schedule by start time
        sorted_schedule = sorted(schedule, key=lambda x: x[1])
        
        # Check for overlaps
        for i in range(1, len(sorted_schedule)):
            current_start = sorted_schedule[i][1]
            previous_end = sorted_schedule[i-1][2]
            if current_start < previous_end:
                return True
        
        return False
