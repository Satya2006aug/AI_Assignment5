# AI Assignment 5

The assignment includes:

1. Minimax Search Algorithm
2. Alpha-Beta Pruning
3. Heuristic Alpha-Beta Search
4. Monte-Carlo Tree Search (MCTS)
5. AI-Based Travel Planner
6. Knowledge Graphs
7. Bayesian Networks

---

# 1. Minimax Search Algorithm

## Aim

To implement the Minimax algorithm for decision-making in a two-player game.

## Working

1. Generate all possible moves
2. Simulate each move
3. Evaluate outcomes recursively
4. Choose the move with best score

## Test Case

Expected:
- AI chooses winning or best possible move

## Result

The Minimax algorithm successfully selected the optimal move.

---

# 2. Alpha-Beta Pruning

## Aim

To improve Minimax performance using Alpha-Beta pruning.

## Working

1. Perform Minimax search
2. Track alpha and beta values
3. Stop exploring useless branches
4. Return optimal score

## Test Case

Input:
Partial Tic-Tac-Toe board

Expected:
- Same result as Minimax
- Faster execution

## Result

Alpha-Beta pruning reduced search complexity and produced correct output.

---

# 3. Heuristic Alpha-Beta Search

## Aim

To implement depth-limited Alpha-Beta search using heuristic evaluation.

## Working

1. Limit search depth
2. Evaluate board using heuristic
3. Apply Alpha-Beta pruning
4. Return best estimated move

## Test Case

Board state with multiple possible moves.

Expected:
- Heuristic score generated correctly

## Result

The heuristic Alpha-Beta search worked successfully and evaluated board states efficiently.

---

# 4. Monte-Carlo Tree Search (MCTS)

## Aim

To implement Monte-Carlo Tree Search for game playing.

## Working

1. Select best node
2. Expand tree
3. Run random simulation
4. Update statistics

## Test Case

Empty Tic-Tac-Toe board.

Expected:
- Best child node selected after simulations

## Result

MCTS successfully performed simulations and selected promising moves.

---

# 5. AI-Based Travel Planner

## Aim

To design an AI-based travel planner using existing knowledge bases.

## Features

- Tourist place recommendation
- Food recommendation
- Budget estimation
- Personalized travel plans

## Knowledge Base Used

The system stores:
- Tourist attractions
- Food items
- Daily travel budget

Cities included:
- Paris
- Tokyo
- Delhi

## Working

1. User enters city and number of days
2. System retrieves information
3. Recommendations are generated
4. Estimated budget is calculated

## Sample Output

City: Paris

Tourist Places:
- Eiffel Tower
- Louvre Museum

Food:
- Croissant
- Macarons

Estimated Cost:
600

## Result

The travel planner generated personalized travel recommendations successfully.

---

# 6. Knowledge Graphs

## What is a Knowledge Graph?

A Knowledge Graph is a structured representation of entities and relationships.

Example:

Alice → studies → AI

AI → related_to → Machine Learning

## Components

- Entities
- Relationships
- Attributes
- Ontologies

## Tools Used for Building Knowledge Graphs

| Tool | Purpose |
|---|---|
| Neo4j | Graph database |
| Protégé | Ontology editor |
| RDFLib | RDF processing |
| Apache Jena | Semantic web framework |
| NetworkX | Graph modelling in Python |

## Python Implementation

A small Knowledge Graph was created using NetworkX.

## Applications

- Search engines
- Recommendation systems
- AI assistants
- Semantic search

## Result

The graph was generated successfully with nodes and relationships.

---

# 7. Bayesian Networks

## Aim

To explore probabilistic reasoning using Bayesian Networks.

## Theory

A Bayesian Network is a probabilistic graphical model.

It represents:
- Random variables as nodes
- Dependencies as edges

## Example Used

Rain → WetGrass

Sprinkler → WetGrass

## Tools Used

- pgmpy
- Python

## Working

1. Create network structure
2. Define probability tables
3. Perform inference
4. Predict probabilities

## Advantages

- Handles uncertainty
- Supports probabilistic reasoning
- Useful in prediction systems

## Applications

- Medical diagnosis
- Spam filtering
- Robotics
- Risk analysis

## Result

The Bayesian Network performed inference successfully.

# Technologies Used

- Python
- NetworkX
- pgmpy
- Matplotlib

---
