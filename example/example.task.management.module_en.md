# example.task.management.module

Task Management Module: Module representing the concepts of a task management system

## Interface Definitions

### Completable

**Methods:**
  - `complete(): Boolean`: Executes the process to set the element to a completed state. Returns True on success.
  - `reopen(): Boolean`: Executes the process to revert the element to a non-completed state. Returns True on success.

### Prioritizable

**Properties:**
  - `priority (Priority)`: The priority of the element.

**Methods:**
  - `setPriority(newPriority: Priority): Void`: Sets the priority of the element.

## Base Class Definitions

### WorkItem: Base class for work items such as tasks and projects

**Properties:**
  - `itemId (UniqueID)`: Unique identifier for each work item.
  - `name (String)`: The name of the work item.
  - `description (String, Optional)`: Detailed description of the work item.
  - `createdAt (Instant)`: The date and time the work item was created.
  - `updatedAt (Instant)`: The date and time the work item was last updated.
  - `createdBy (User)`: The user who created this work item (Aggregation).

**Methods:**
  - `constructor(name: String, createdBy: User): Void`: Initializes the work item with a name and creator.
  - `setName(newName: String): Void`: Changes the name of the work item.
  - `setDescription(newDescription: String): Void`: Updates the description of the work item.

**Events:**
  - `Updated()`: Triggered when the work item information is updated.
  - `NameChanged(oldName: String, newName: String)`: Triggered when the name is changed.

## Core Class Definitions

### Task: Represents an individual task

**Base Class:** WorkItem
**Interfaces:** Completable, Prioritizable

**Properties:**
  - `status (TaskStatus)`: The current status of the task.
  - `dueDate (Instant, Optional)`: The deadline for completing the task (Optional).
  - `assignee (User, Optional)`: The user assigned to this task (Aggregation, Optional).
  - `priority (Priority)`: The priority of the task.

**Methods:**
  - `constructor(name: String, createdBy: User, priority: Priority = MEDIUM): Void`: Initializes the task.
  - `assignUser(user: User): Void`: Assigns a user to the task.
  - `unassignUser(): Void`: Removes the assignee from the task.
  - `setStatus(newStatus: TaskStatus): Boolean`: Changes the status of the task. Returns True on success.
  - `setDueDate(newDueDate: Instant): Void`: Sets or updates the due date of the task.
  - `complete(): Boolean`: Changes the task status to "COMPLETED".
  - `reopen(): Boolean`: Reverts the task status to "NOT_STARTED" or "IN_PROGRESS".
  - `setPriority(newPriority: Priority): Void`: Sets the priority of the task.

**Events:**
  - `StatusChanged(oldStatus: TaskStatus, newStatus: TaskStatus)`: Triggered when the task status changes.
  - `AssigneeChanged(oldAssignee: User, newAssignee: User)`: Triggered when the task assignee changes.
  - `DueDateChanged(oldDueDate: Instant, newDueDate: Instant)`: Triggered when the task due date changes.

### Project: Represents a project that groups multiple tasks

**Base Class:** WorkItem
**Interfaces:** Completable

**Properties:**
  - `tasks (List<Task>)`: List of tasks included in the project (Composition).
  - `participants (List<User>)`: List of users participating in the project (Aggregation).
  - `isCompleted (Boolean)`: Whether the entire project is completed.

**Methods:**
  - `constructor(name: String, createdBy: User): Void`: Initializes the project.
  - `addTask(task: Task): Boolean`: Adds a task to the project.
  - `removeTask(taskId: UniqueID): Boolean`: Removes a task with the specified ID from the project.
  - `addParticipant(user: User): Boolean`: Adds a participant to the project.
  - `removeParticipant(userId: UniqueID): Boolean`: Removes a participant with the specified ID from the project.
  - `complete(): Boolean`: Sets the project to a completed state (can be set independently of included task statuses).
  - `reopen(): Boolean`: Reverts the project to a non-completed state.
  - `calculateProgress(): Number`: Calculates and returns the progress percentage (0-100) based on the completion status of tasks within the project.

**Events:**
  - `TaskAdded(addedTask: Task)`: Triggered when a task is added to the project.
  - `TaskRemoved(removedTaskId: UniqueID)`: Triggered when a task is removed from the project.
  - `ParticipantAdded(addedParticipant: User)`: Triggered when a participant is added to the project.
  - `ParticipantRemoved(removedParticipantId: UniqueID)`: Triggered when a participant is removed from the project.
  - `CompletionStatusChanged(newCompletionStatus: Boolean)`: Triggered when the project's completion status changes.

## Related Class Definitions

### User: Represents a user of the system

**Properties:**
  - `userId (UniqueID)`: Unique identifier for each user.
  - `username (String)`: The user's account name.
  - `displayName (String)`: The user's display name shown on screen.
  - `email (String)`: The user's email address.

**Methods:**
  - `constructor(username: String, displayName: String, email: String): Void`: Initializes the user.
  - `setDisplayName(newDisplayName: String): Void`: Changes the user's display name.
  - `setEmail(newEmail: String): Void`: Changes the user's email address.

## Enum Definitions
  - `TaskStatus`: NOT_STARTED, IN_PROGRESS, COMPLETED, ON_HOLD
  - `Priority`: LOW, MEDIUM, HIGH, URGENT
