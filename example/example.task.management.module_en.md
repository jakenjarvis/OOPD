## example.task.management.module

Task Management Module: This module represents the concepts of a task management system.

### Interfaces: Defines the interfaces used within the task management module.

#### Completable: Represents elements that can be marked as complete or incomplete.

**Methods:**

- `complete(): Boolean`: Executes the process to mark the element as complete. Returns True on success.
- `revertCompletion(): Boolean`: Executes the process to revert the element to an incomplete state. Returns True on success.

#### Prioritizable: Represents elements that can have a priority assigned.

**Properties:**

- `priority: Priority`: The priority level of the element.

**Methods:**

- `setPriority(newPriority: Priority): Void`: Sets the priority of the element.

### Base Classes: Defines the base classes for work items.

#### WorkItem: Base class for work items such as tasks and projects.

**Properties:**

- `itemId: UniqueID`: Unique identifier for each work item.
- `name: String`: The name of the work item.
- `description: String, Optional`: Detailed description of the work item.
- `createdAt: Instant`: The date and time when the work item was created.
- `updatedAt: Instant`: The date and time when the work item was last updated.
- `createdBy: User`: The user who created this work item (Aggregation).

**Methods:**

- `constructor(name: String, createdBy: User): Void`: Initializes the work item with a name and creator.
- `changeName(newName: String): Void`: Changes the name of the work item.
- `updateDescription(newDescription: String): Void`: Updates the description of the work item.

**Events:**

- `updated()`: Occurs when the work item's information is updated.
- `nameChanged(oldName: String, newName: String)`: Occurs when the name is changed.

### Core Classes: Defines the core classes for tasks and projects.

#### Task: Represents an individual task.

**Base Class:** WorkItem
**Interfaces:** Completable, Prioritizable

**Properties:**

- `status: TaskStatus`: The current status of the task.
- `dueDate: Instant, Optional`: The deadline for completing the task (optional).
- `assignee: User, Optional`: The user assigned to this task (Aggregation, optional).
- `priority: Priority`: The priority level of the task.

**Methods:**

- `constructor(name: String, createdBy: User, priority: Priority = MEDIUM): Void`: Initializes the task.
- `assignUser(user: User): Void`: Assigns a user to the task.
- `unassignUser(): Void`: Removes the assignee from the task.
- `changeStatus(newStatus: TaskStatus): Boolean`: Changes the status of the task. Returns True on success.
- `setDueDate(newDueDate: Instant): Void`: Sets or updates the due date of the task.
- `complete(): Boolean`: Changes the task status to "Completed".
- `revertCompletion(): Boolean`: Reverts the task status to "Not Started" or "In Progress".
- `setPriority(newPriority: Priority): Void`: Sets the priority of the task.

**Events:**

- `statusChanged(oldStatus: TaskStatus, newStatus: TaskStatus)`: Occurs when the task status changes.
- `assigneeChanged(oldAssignee: User, newAssignee: User)`: Occurs when the task assignee changes.
- `dueDateChanged(oldDueDate: Instant, newDueDate: Instant)`: Occurs when the task due date changes.

#### Project: Represents a project that groups multiple tasks.

**Base Class:** WorkItem
**Interfaces:** Completable

**Properties:**

- `taskList: List<Task>`: The list of tasks included in the project (Composition).
- `participantList: List<User>`: The list of users participating in the project (Aggregation).
- `isCompleted: Boolean`: Indicates whether the entire project is completed.

**Methods:**

- `constructor(name: String, createdBy: User): Void`: Initializes the project.
- `addTask(taskToAdd: Task): Boolean`: Adds a task to the project.
- `removeTask(taskId: UniqueID): Boolean`: Removes the task with the specified ID from the project.
- `addParticipant(userToAdd: User): Boolean`: Adds a participant to the project.
- `removeParticipant(userId: UniqueID): Boolean`: Removes the participant with the specified ID from the project.
- `complete(): Boolean`: Marks the project as completed (can be set independently of the status of included tasks).
- `revertCompletion(): Boolean`: Reverts the project to an incomplete state.
- `calculateProgress(): Number`: Calculates and returns the progress percentage (0-100) based on the completion status of tasks within the project.

**Events:**

- `taskAdded(addedTask: Task)`: Occurs when a task is added to the project.
- `taskRemoved(removedTaskId: UniqueID)`: Occurs when a task is removed from the project.
- `participantAdded(addedParticipant: User)`: Occurs when a participant is added to the project.
- `participantRemoved(removedParticipantId: UniqueID)`: Occurs when a participant is removed from the project.
- `completionStatusChanged(newCompletionStatus: Boolean)`: Occurs when the completion status of the project changes.

### Related Classes: Defines related classes such as User.

#### User: Represents a user of the system.

**Properties:**

- `userId: UniqueID`: Unique identifier for each user.
- `username: String`: The user's account name.
- `displayName: String`: The user's display name shown on the screen.
- `email: String`: The user's email address.

**Methods:**

- `constructor(username: String, displayName: String, email: String): Void`: Initializes the user.
- `changeDisplayName(newDisplayName: String): Void`: Changes the user's display name.
- `changeEmail(newEmail: String): Void`: Changes the user's email address.

### Enums: Defines enumeration types used in the module.

- `TaskStatus`: NOT_STARTED, IN_PROGRESS, COMPLETED, ON_HOLD
- `Priority`: LOW, MEDIUM, HIGH, URGENT
