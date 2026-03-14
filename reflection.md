# PawPal+ Project Reflection

## 1. System Design

**3 core actions**
- Add owner/pet information
- Add and edit tasks
- View daily schedule/plan

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
 * Owner
    * Attributes:
        * name: string
        * pets: List of Pet objects
        * hrs_available: int
        * tasks: List of Tasks
    * Methods:
        * addPet: adds a pet to owners list
        * removePet: removes a pet from owners list
        * getPets: gets a list of pets owned by owner
        * getTasks: gets a list of tasks for owner
        * addTask: add task to list of tasks for owner
        * removeTask: remove task from list of tasks for owner
 * Pet
    * Attributes:
        * name: string
        * type: string
        * age: int
    * Methods:
 * Task
    * Attributes:
        * title: string
        * durationHrs: int
        * priority: string
        * type: string
        * pet: Pet
        * ifCompeleted: boolean
    * Methods:
        * complete: marks ifCompeleted as true
 * Scheduler
    * Attributes:
        * owner: Owner
        * pet: Pet
        * tasks: List of Tasks
    * Methods:
        * generatePlan: generate plan

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
    * Yes, the AI suggested removing a pet attribute, which I initially added to the scheduler. But this would be a logic error as that would assume a 1:1 relationship between Pet and a Schedule.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
