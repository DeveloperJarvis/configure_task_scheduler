# Low-Level Design (LLD)

## Configurable Task Scheduler (Cron-like)

**Skills Focused**:

- Task scheduling (`sched` module)
- Background jobs
- Configuration file handling
- System design in Python

---

## 1. Problem Statement

Design a task scheduler that:

- Runs predefined tasks at fixed intervals or scheduled times
- Works continuously in the background
- Loads task definitions from a configuration file
- Mimics basic cron functionality (interval-based scheduling)

---

## 2. Assumptions

- Scheduler runs as a long-lived Python process
- Tasks are Python callables or shell commands
- Configuration is stored in a file (JSON / YAML / INI)
- Time granularity is seconds/minutes (not full cron expressions)
- Focus is on **interval-based execution**, not calendar rules

---

## 3. High-Level Architecture

```
+--------------------+
|  Config File       |
| (tasks.json)       |
+----------+---------+
           |
           v
+--------------------+
| Config Loader      |
+----------+---------+
           |
           v
+--------------------+
| Task Registry      |
+----------+---------+
           |
           v
+--------------------+
| Scheduler Engine   |
| (sched module)     |
+----------+---------+
           |
           v
+--------------------+
| Background Worker  |
+--------------------+
```

---

## 4. Core Components (LLD)

---

### 4.1 Task Configuration File

**Purpose**
Defines which tasks to run and how often.

**Example Fields**

- `task_id`
- `task_name`
- `interval_seconds`
- `enabled`
- `task_type` (python / shell)
- `entry_point`

**Responsibilities**

- Externalize scheduling logic
- Allow runtime behavior changes without code edits

---

### 4.2 Config Loader

**Purpose**
Reads and validates task configuration from file.

**Input**

- Path to config file

**Output**

- List of task definitions

**Responsibilities**

- Parse configuration file
- Validate required fields
- Ignore disabled tasks
- Handle malformed config gracefully

---

### 4.3 Task Model

**Purpose**
Represents a scheduled task in memory.

**Attributes**

- `task_id`
- `name`
- `interval`
- `next_run_time`
- `callable / command`
- `enabled`

**Responsibilities**

- Store task metadata
- Track execution timing
- Update next scheduled run

---

### 4.4 Task Registry

**Purpose**
Central in-memory store for all tasks.

**Responsibilities**

- Add / remove tasks
- Fetch enabled tasks
- Support reload of configuration
- Prevent duplicate task IDs

---

### 4.5 Scheduler Engine

**Purpose**
Core scheduling mechanism using Python’s `sched` module.

**Responsibilities**

- Schedule tasks based on intervals
- Maintain event queue
- Re-schedule tasks after execution
- Calculate next execution time

**Key Behavior**

- Uses system time (`time.time`)
- Runs in a loop
- Executes callbacks at scheduled times

---

### 4.6 Background Worker

**Purpose**
Executes tasks without blocking the scheduler.

**Responsibilities**

- Run tasks in background threads
- Prevent long-running tasks from delaying others
- Capture execution status and errors

**Design Choice**

- Use threads for simplicity
- One thread per task execution

---

### 4.7 Task Executor

**Purpose**
Executes the actual task logic.

**Responsibilities**

- Execute Python callable OR shell command
- Handle execution errors
- Log success/failure
- Return execution status

---

### 4.8 Logger (Cross-Cutting Concern)

**Purpose**
Track system activity.

**Logs**

- Task start / completion
- Errors and failures
- Scheduler startup/shutdown
- Configuration reloads

---

## 5. Data Flow (Step-by-Step)

1. Scheduler starts
2. Config Loader reads task config file
3. Task Registry stores enabled tasks
4. Scheduler Engine schedules tasks via `sched`
5. Background Worker executes tasks
6. Task Executor runs the task
7. Task completion triggers re-scheduling
8. Logs are written throughout

---

## 6. Scheduling Strategy

| Feature             | Behavior              |
| ------------------- | --------------------- |
| Interval scheduling | Fixed seconds/minutes |
| Re-scheduling       | After task execution  |
| Missed runs         | Executed immediately  |
| Parallel tasks      | Supported             |
| Blocking prevention | Background threads    |

---

## 7. Error Handling Design

| Scenario          | Handling                |
| ----------------- | ----------------------- |
| Invalid config    | Skip task, log error    |
| Task failure      | Log, continue scheduler |
| Long-running task | Run in background       |
| Duplicate task ID | Reject task             |
| Scheduler crash   | Graceful shutdown       |

---

## 8. Extensibility

The design supports future features:

- Full cron expressions
- Task priorities
- Retry policies
- Task dependencies
- Distributed scheduling
- REST API control
- Persistent job state

---

## 9. Non-Functional Requirements

- **Reliability**: Tasks continue running despite failures
- **Scalability**: Supports multiple concurrent tasks
- **Maintainability**: Clear module separation
- **Portability**: Cross-platform Python execution
- **Configurability**: No hard-coded schedules

---

## 10. Comparison to Cron

| Feature            | Cron         | This System    |
| ------------------ | ------------ | -------------- |
| Language           | Shell        | Python         |
| Config             | Crontab      | JSON/YAML      |
| Dynamic reload     | No           | Yes            |
| Programmatic tasks | Limited      | Full           |
| Portability        | OS-dependent | Cross-platform |

---

## 11. Summary

This LLD:

- Uses Python’s `sched` module as the scheduling core
- Separates configuration, scheduling, and execution
- Supports background task execution
- Mimics cron behavior while remaining flexible
- Is interview-ready and production-extensible
