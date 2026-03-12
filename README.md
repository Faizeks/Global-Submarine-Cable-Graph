# Global Submarine Fiber Optic Cable Network Analysis (Neo4j)
## Project Overview

The global internet infrastructure relies heavily on submarine fiber optic cables, which form the backbone of international data communication. These cables connect continents, countries, and major communication hubs through a complex network of landing stations and ocean routes.

This project models the global submarine cable ecosystem using a Neo4j graph database to analyze relationships between cables, companies, landing stations, countries, and oceans. By representing the dataset as a graph, the relationships between these entities can be explored more intuitively and efficiently compared to traditional relational databases.

The objective of this project is to explore the structure of the global submarine cable network and answer several analytical questions, such as:
- Which countries act as major connectivity hubs?
- Which companies own the largest number of submarine cables?
- What are the longest submarine cables in the network?
- How do cables connect multiple countries through landing stations?

## Dataset Description

The dataset represents the global submarine fiber optic cable infrastructure using several core entities.

Node Types
| Node Label           | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| **Cables**           | Submarine fiber optic cables connecting different regions                 |
| **Companies**        | Companies that own or operate submarine cables                            |
| **Countries**        | Countries where landing stations are located                              |
| **Landing_stations** | Physical landing points where cables connect to land-based infrastructure |
| **Oceans**           | Oceans through which submarine cables are routed                          |

