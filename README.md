# DevDash

A modern desktop dashboard application for developers to manage workspaces and monitor system resources in real-time.

## Description

DevDash is a Python-based GUI application built with CustomTkinter that provides a clean, dark-themed interface for managing development environments and monitoring system performance. It features real-time resource tracking and workspace configuration for different development scenarios.

## Features

- **Multi-Page Dashboard**: Navigate between Dash, Config, and Environment pages
- **System Monitoring**: Real-time CPU, RAM, and GPU usage tracking
- **Workspace Management**: Create and manage different development environments (e.g., Coding, Streaming)
- **Theme Support**: Switch between light and dark modes
- **Modern UI**: Clean, responsive interface with CustomTkinter
- **Environment Configuration**: JSON-based workspace definitions with associated applications

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd devdash
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install customtkinter psutil pynvml
   ```

## Usage

Run the application:

```bash
python main.py
```

### Interface Overview

- **Dash Page**: View real-time system resource usage
- **Config Page**: Adjust theme and startup settings
- **Env Page**: Manage and switch between different workspaces

### Workspace Configuration

Workspaces are created in Env page.

## Dependencies

- **customtkinter**: Modern Python GUI framework
- **psutil**: System and process utilities for resource monitoring
- **pynvml**: NVIDIA GPU monitoring library

## Requirements

- Python 3.7+
- NVIDIA GPU (optional, for GPU monitoring)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source. Please check the license file for details.
