import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pawpal_system import Owner, Pet, Task, Scheduler

def test_sort_by_time():
    """Test that sort_by_time sorts tasks by durationHrs ascending."""
    owner = Owner(name="Test Owner", hrs_available=10.0)
    pet = Pet(name="Test Pet", type="dog", age=1)
    
    task1 = Task(title="Short Task", durationHrs=1.0, priority="high", type="exercise", pet=pet)
    task2 = Task(title="Long Task", durationHrs=3.0, priority="medium", type="feeding", pet=pet)
    task3 = Task(title="Medium Task", durationHrs=2.0, priority="low", type="grooming", pet=pet)
    
    scheduler = Scheduler(owner=owner, pet=pet, tasks=[task2, task1, task3])  # Unsorted order
    
    scheduler.sort_by_time()
    
    # Check that tasks are sorted by durationHrs
    durations = [t.durationHrs for t in scheduler.tasks]
    assert durations == [1.0, 2.0, 3.0], f"Expected [1.0, 2.0, 3.0], got {durations}"
    print("test_sort_by_time passed")

def test_filter_by_completion():
    """Test that filterByCompletion returns tasks filtered by completion status."""
    owner = Owner(name="Test Owner", hrs_available=10.0)
    pet = Pet(name="Test Pet", type="dog", age=1)
    
    task1 = Task(title="Task 1", durationHrs=1.0, priority="high", type="exercise", pet=pet, ifCompleted=True)
    task2 = Task(title="Task 2", durationHrs=2.0, priority="medium", type="feeding", pet=pet, ifCompleted=False)
    task3 = Task(title="Task 3", durationHrs=3.0, priority="low", type="grooming", pet=pet, ifCompleted=True)
    
    scheduler = Scheduler(owner=owner, pet=pet, tasks=[task1, task2, task3])
    
    completed = scheduler.filterByCompletion(True)
    incomplete = scheduler.filterByCompletion(False)
    
    assert len(completed) == 2, f"Expected 2 completed tasks, got {len(completed)}"
    assert all(t.ifCompleted for t in completed), "All completed tasks should have ifCompleted=True"
    assert len(incomplete) == 1, f"Expected 1 incomplete task, got {len(incomplete)}"
    assert all(not t.ifCompleted for t in incomplete), "All incomplete tasks should have ifCompleted=False"
    print("test_filter_by_completion passed")

def test_detect_conflicts():
    """Test that detect_conflicts identifies overlapping schedules."""
    owner = Owner(name="Test Owner", hrs_available=10.0)
    pet = Pet(name="Test Pet", type="dog", age=1)
    
    task1 = Task(title="Task 1", durationHrs=1.0, priority="high", type="exercise", pet=pet)
    task2 = Task(title="Task 2", durationHrs=2.0, priority="medium", type="feeding", pet=pet)
    
    scheduler = Scheduler(owner=owner, pet=pet, tasks=[task1, task2])
    
    # No conflicts: sequential
    schedule_no_conflict = [(task1, 0.0, 1.0), (task2, 1.0, 3.0)]
    assert not scheduler.detect_conflicts(schedule_no_conflict), "Should not detect conflicts in sequential schedule"
    
    # With conflicts: overlap
    schedule_conflict = [(task1, 0.0, 2.0), (task2, 1.0, 3.0)]
    assert scheduler.detect_conflicts(schedule_conflict), "Should detect conflicts in overlapping schedule"
    
    # Edge case: empty schedule
    assert not scheduler.detect_conflicts([]), "Empty schedule should not have conflicts"
    
    print("test_detect_conflicts passed")

if __name__ == "__main__":
    test_sort_by_time()
    test_filter_by_completion()
    test_detect_conflicts()
    print("All tests passed!")
