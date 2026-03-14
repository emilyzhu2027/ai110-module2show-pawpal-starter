from pawpal_system import Owner, Pet, Task, Scheduler

# Create an Owner
owner = Owner(name="John Doe", hrs_available=8.0)

# Create two Pets
pet1 = Pet(name="Buddy", type="dog", age=3)
pet2 = Pet(name="Whiskers", type="cat", age=2)

# Add pets to owner
owner.addPet(pet1)
owner.addPet(pet2)

# Create Tasks with different durations
task1 = Task(title="Morning Walk", durationHrs=1.0, priority="high", type="exercise", pet=pet1)
task2 = Task(title="Feeding", durationHrs=0.5, priority="high", type="feeding", pet=pet1)
task3 = Task(title="Grooming", durationHrs=2.0, priority="medium", type="grooming", pet=pet2)

# Add tasks to owner
owner.addTask(task1)
owner.addTask(task2)
owner.addTask(task3)

# Print Today's Schedule
print("Today's Schedule")
print("=" * 20)

for pet in owner.getPets():
    scheduler = Scheduler(owner=owner, pet=pet, tasks=owner.getTasks())
    schedule = scheduler.generatePlan()
    
    print(f"\nSchedule for {pet.name} ({pet.type}):")
    if schedule:
        for task, start, end in schedule:
            print(f"- {task.title}: {start:.1f} - {end:.1f} hours ({task.priority} priority)")
    else:
        print("No tasks scheduled.")

