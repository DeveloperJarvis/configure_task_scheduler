# configure_task_scheduler

**configure_task_scheduler** is a Python-based, cron-like task scheduling library that allows users to configure and execute recurring tasks at fixed intervals. It leverages Python’s built-in **`sched` module**, supports **background job execution**, and reads task definitions from **configuration files**.

This project is designed for educational, interview, and lightweight automation use cases.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Design](#system-design)
- [Configuration](#configuration)
- [Architecture Components](#architecture-components)
- [Installation](#installation)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Extensibility](#extensibility)
- [License](#license)
- [Contact](#contact)

---

## Overview

The goal of this project is to provide a **configurable task scheduler** similar to Unix `cron`, but implemented entirely in Python. Tasks are defined externally using configuration files and executed at fixed intervals in the background.

The scheduler runs as a long-lived process and continuously monitors scheduled jobs.

---

## Key Features

- Cron-like interval-based scheduling
- Uses Python’s built-in `sched` module
- Background task execution (non-blocking)
- Task definitions loaded from configuration files
- Enable/disable tasks without code changes
- Graceful handling of task failures
- Modular and extensible design

---

## System Design

High-level workflow:

```
Configuration File
        |
        v
Config Loader
        |
        v
Task Registry
        |
        v
Scheduler Engine (sched)
        |
        v
Background Worker Threads
```

---

## Configuration

Tasks are defined using an external configuration file (e.g., JSON or YAML).

### Typical Task Attributes

- `task_id` – Unique identifier
- `task_name` – Human-readable name
- `interval_seconds` – Execution interval
- `enabled` – Enable/disable flag
- `task_type` – Python function or shell command
- `entry_point` – Callable path or command string

This approach allows task schedules to be modified without restarting or editing the codebase.

---

## Architecture Components

### 1. Config Loader

- Reads and validates configuration files
- Filters out invalid or disabled tasks
- Supports runtime reloads

### 2. Task Model

- Represents a single scheduled task
- Tracks execution interval and next run time

### 3. Task Registry

- Stores all loaded tasks in memory
- Prevents duplicate task definitions
- Enables dynamic task management

### 4. Scheduler Engine

- Core scheduling logic using `sched`
- Maintains event queue
- Re-schedules tasks after execution

### 5. Background Worker

- Executes tasks in separate threads
- Prevents blocking the scheduler loop

### 6. Task Executor

- Executes Python callables or shell commands
- Captures execution status and errors

---

## Installation

### Requirements

- Python 3.8+
- No external dependencies (standard library only)

### Clone the Repository

```bash
git clone https://github.com/DeveloperJarvis/configure_task_scheduler.git
cd configure_task_scheduler
```

---

## Usage

Typical usage flow:

1. Define tasks in a configuration file
2. Start the scheduler
3. Scheduler loads tasks and begins execution
4. Tasks run repeatedly at configured intervals

The scheduler runs continuously until stopped.

---

## Error Handling

The system is designed to be fault-tolerant:

| Scenario               | Handling                    |
| ---------------------- | --------------------------- |
| Invalid config entry   | Task skipped, error logged  |
| Task execution failure | Logged, scheduler continues |
| Long-running task      | Executed in background      |
| Duplicate task ID      | Rejected during load        |
| Scheduler shutdown     | Graceful exit               |

---

## Extensibility

The architecture supports future enhancements such as:

- Full cron expression support
- Task priorities
- Retry and backoff policies
- Persistent job state
- REST API for task control
- Distributed task execution
- Web-based dashboard

---

## License

This project is licensed under the **GNU General Public License v3.0**.

See the [LICENSE](LICENSE) file for full license details.

---

## Contact

**Author**: Developer Jarvis (Pen Name)
**GitHub**: [https://github.com/DeveloperJarvis](https://github.com/DeveloperJarvis)

For issues, feature requests, or contributions, please open an issue or submit a pull request.

## Creating tag

```bash
# 1. Check existing tags
git tag
# 2. Create a valid tag
git tag -a v1.0.0 -m "Release version 1.0.0"
# or lightweight tag
git tag v1.0.0
# push tag to remote
git push origin v1.0.0
```
