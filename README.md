# River Crossing Puzzle Project Proposal

- [Executive Summary](#executive-summary)
- [Problem Statement](#problem-statement)
- [Project Objectives](#project-objectives)
- [Technical Approach](#technical-approach)
  - [PEAS Framework Analysis](#peas-framework-analysis)
    - [Performance Measure](#performance-measure)
    - [Environment](#environment)
    - [Actuators](#actuators)
    - [Sensors](#sensors)
  - [ODESDA Environment Properties Analysis](#odesda-environment-properties-analysis)
    - [Agent Type](#agent-type)
- [Implementation Specifications](#implementation-specifications)
  - [Algorithm Implementation](#algorithm-implementation)
    - [Representation](#representation)
    - [Core Operations](#core-operations)
    - [Parameters](#parameters)
  - [User Interface Components](#user-interface-components)
    - [Visualization Panel](#visualization-panel)
    - [Control Panel](#control-panel)
    - [Statistics Display](#statistics-display)
  - [Visual Design](#visual-design)
    - [Item Representation](#item-representation)
    - [Environment Representation](#environment-representation)
    - [UI Design](#ui-design)
- [Technical Requirements](#technical-requirements)
  - [Development Environment](#development-environment)
  - [System Requirements](#system-requirements)
  - [Dependencies](#dependencies)
- [Project Timeline](#project-timeline)
- [Conclusion](#conclusion)

## Executive Summary
This proposal outlines the development of a Python-based Tkinter application that implements the classic Wolf, Goat, and Cabbage river crossing puzzle. The application provides an interactive graphical interface with real-time visualization, manual gameplay, and an automated solver using a breadth-first search (BFS) algorithm. The project aims to demonstrate problem-solving through state-space search while offering an engaging user experience.

## Problem Statement
The Wolf, Goat, and Cabbage puzzle is a well-known constraint satisfaction problem: a farmer must transport a wolf, a goat, and a cabbage across a river using a boat that can carry only one item at a time, ensuring that the wolf and goat or the goat and cabbage are never left together unsupervised. This problem has applications in AI planning, constraint-based reasoning, and state-space search.

## Project Objectives
- Implement a state-space search algorithm (BFS) to solve the river crossing puzzle  
- Develop an interactive graphical interface for manual gameplay and visualization  
- Provide an automated solver to demonstrate optimal solutions  
- Track and display performance metrics (e.g., move count)  
- Create an intuitive and visually appealing user experience  

## Technical Approach

### PEAS Framework Analysis

#### Performance Measure
- **Primary:** Minimum number of moves to solve the puzzle (lower is better)  
- **Secondary:**  
  - Computation time for automated solver  
  - User interaction responsiveness  
  - Clarity of visual feedback  
  - Memory usage efficiency  

#### Environment
- Two banks (left and right) with sets of items (wolf, goat, cabbage, farmer)  
- Boat with binary position (left or right bank) and capacity for farmer plus one item  
- User interface with canvas and control elements  
- System resources (CPU, memory)  

#### Actuators
- Move farmer and optional item across the river  
- Update game state (item positions, boat position)  
- Render graphical elements (banks, boat, items)  
- Display move count and status messages  
- Execute automated solution steps  
- Respond to user inputs (clicks, buttons)  

#### Sensors
- User input detection (mouse clicks on items or boat, button presses)  
- Game state evaluation (item positions, boat position)  
- Constraint violation checker (unsafe states)  
- Move counter  
- Timer for automated solution steps  

### ODESDA Environment Properties Analysis

| Property               | Type                                                                 |
|------------------------|----------------------------------------------------------------------|
| **Observable**         | Fully Observable: All item positions, boat position, and game state |
| **Deterministic**      | Deterministic: State transitions follow fixed rules                |
| **Episodic**           | Sequential: Each move depends on the previous state                |
| **Static**             | Static problem (fixed items and constraints), dynamic user inputs  |
| **Discrete**           | Discrete states, moves, and item positions                         |

#### Agent Type
- **Single-agent:** One solver managing the game state  
- **Multi-agent perspective:** Farmer as an agent navigating state constraints  

## Implementation Specifications

### Algorithm Implementation

#### Representation
- Game state as two sets (left_bank, right_bank) and boat position (left/right)  
- Items: wolf, goat, cabbage, farmer  
- Valid states ensure no unsafe combinations (wolf-goat or goat-cabbage without farmer)  

#### Core Operations
- **Manual Play:** User selects an item and moves the boat with the farmer and optional item  
- **Automated Solver:** Breadth-first search to find the shortest sequence of valid moves  
- **State Validation:** Check for constraint violations (unsafe states)  
- **Move Tracking:** Increment move counter per boat trip  

#### Parameters
- **Boat capacity:** Farmer + one optional item  
- **Animation delay:** 800ms per step in auto-solve mode  
- **Item set:** Fixed (wolf, goat, cabbage, farmer)  

### User Interface Components

#### Visualization Panel
- Tkinter canvas (800x600) with graphical elements:  
  - Banks (brown rectangles with grass)  
  - River (blue wavy lines)  
  - Boat (wood-colored with motion effect)  
  - Items (emoji-based with colored backgrounds)  
  - Sun and clouds for aesthetic background  
- Real-time state updates  

#### Control Panel
- Buttons: Reset Game, Auto Solve  
- Move counter display  
- Status message label for user feedback  

#### Statistics Display
- Move count  
- Game status (e.g., win, loss, or progress messages)  

### Visual Design

#### Item Representation
- Wolf: 🐺 (gray background)  
- Goat: 🐐 (white background)  
- Cabbage: 🥬 (green background)  
- Farmer: 👨‍🌾 (peach background)  

#### Environment Representation
- Left/right banks: Brown with green grass  
- River: Blue with wave effect  
- Boat: Wooden texture with farmer/item display  
- Background: Light blue with sun and clouds  

#### UI Design
- Clean, modern layout with pastel colors  
- Fixed window size (800x600) for consistency  
- Bold fonts for buttons and labels  
- Responsive click-based interaction  

## Technical Requirements

### Development Environment
- Python 3.8+  
- Tkinter library (standard with Python)  
- Visual Studio Code or PyCharm  

### System Requirements
- Windows, macOS, or Linux  
- Minimum 2GB RAM  
- Single-core processor or higher  

### Dependencies
- `tkinter` (GUI framework)  
- `collections.deque` (for BFS queue)  

## Project Timeline

| Week | Milestone                                  |
|------|--------------------------------------------|
| 1    | Core Logic Development: Game state, move validation, BFS solver |
| 2    | Visualization System: Canvas rendering, item and boat graphics |
| 3    | User Interface: Controls, status display, interaction handling |
| 4    | Testing and Refinement: Bug fixes, UI polish, documentation |

## Conclusion
This project delivers an educational and interactive tool for exploring the Wolf, Goat, and Cabbage river crossing puzzle. By combining a graphical interface with a BFS-based solver, it demonstrates state-space search in AI while providing an engaging user experience. The application’s clear visualization and intuitive controls allow users to experiment with manual and automated solutions, offering insights into constraint-based problem-solving. The PEAS and ODESDA analyses ensure a robust design, making this a valuable showcase of AI and UI development principles.
