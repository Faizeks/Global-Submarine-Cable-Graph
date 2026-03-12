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

### Node Types
| Node Label           | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| **Cables**           | Submarine fiber optic cables connecting different regions                 |
| **Companies**        | Companies that own or operate submarine cables                            |
| **Countries**        | Countries where landing stations are located                              |
| **Landing_stations** | Physical landing points where cables connect to land-based infrastructure |
| **Oceans**           | Oceans through which submarine cables are routed                          |

### Relationship Types
| Relationship     | Description                                        |
| ---------------- | -------------------------------------------------- |
| **OWNS**         | A company owns or operates a submarine cable       |
| **LANDS_AT**     | A cable connects to a landing station              |
| **LOCATED_IN**   | A landing station is located in a specific country |
| **RUNS_THROUGH** | A cable passes through a particular ocean          |
This graph structure enables efficient exploration of network connectivity, infrastructure ownership, and geographical distribution.

## Full Network Visualization
The following query visualizes the relationships between all nodes in the graph.
```cypher
MATCH (n)-[r]->(m)
RETURN n,r,m
LIMIT 500
```
This visualization provides a high-level overview of the network and highlights the relationships between:
- Companies and cables
- Cables and landing stations
- Landing stations and countries
- Cables and oceans
  
The resulting graph illustrates the global connectivity structure of submarine fiber optic infrastructure.

## Business Questions & Graph Analysis
The following analytical queries explore key aspects of the submarine cable network.

1. Countries with the Highest Number of Landing Stations
   Landing stations serve as critical infrastructure points where submarine cables connect to terrestrial networks.
    ```cypher
    MATCH (ls:Landing_stations)-[:LOCATED_IN]->(c:Countries)
    RETURN c.country_name AS country,
           count(ls) AS total_landing_stations
    ORDER BY total_landing_stations DESC
    LIMIT 10
    ```
    Countries with the highest number of landing stations often act as major international connectivity hubs.

2. Companies Owning the Largest Number of Submarine Cables
   This analysis identifies the companies that play the most significant role in the global submarine cable ecosystem.
    ```
    MATCH (comp:Companies)-[:OWNS]->(c:Cables)
    RETURN comp.company_name AS company,
           count(c) AS total_cables
    ORDER BY total_cables DESC
    LIMIT 10
    ```
    Major telecommunications providers and technology companies typically dominate submarine cable ownership.
  
3. Longest Submarine Cables in the Network
   Understanding the longest cables provides insight into the scale of global internet infrastructure.
    ```
    MATCH (c:Cables)
    RETURN c.cable_name AS cable,
           c.length_km AS length_km
    ORDER BY length_km DESC
    LIMIT 10
    ```
    Many of these cables span thousands of kilometers and connect multiple continents.

4. Countries Connected by Each Cable
   Submarine cables often connect multiple countries through a series of landing stations.
   ```
   MATCH (c:Cables)-[:LANDS_AT]->(ls:Landing_stations)-[:LOCATED_IN]->(country:Countries)
   RETURN c.cable_name AS cable,
     collect(DISTINCT country.country_name) AS connected_countries
   LIMIT 20
   ```
   This query highlights how individual cables contribute to multi-country connectivity networks.

5. Cables Running Through Specific Oceans
   The following query identifies cables that pass through the Pacific Ocean.
   ```
   MATCH (c:Cables)-[:RUNS_THROUGH]->(o:Oceans)
   WHERE o.ocean_name = "Pacific Ocean"
   RETURN c.cable_name
   ```
   The Pacific Ocean hosts a large number of submarine cables due to the high volume of data exchange between Asia and North America.

6. Submarine Cables Landing in Indonesia
   This query identifies cables that connect to Indonesia through landing stations.
   ```
   MATCH (c:Cables)-[:LANDS_AT]->(ls:Landing_stations)-[:LOCATED_IN]->(country:Countries)
   WHERE country.country_name = "Indonesia"
   RETURN DISTINCT c.cable_name
   ```
   Indonesia, as a geographically distributed archipelago, relies heavily on submarine cables for international internet connectivity.

## Key Insights
Several important insights can be derived from this graph analysis:
- The global internet infrastructure is supported by a highly interconnected submarine cable network.
- Certain countries act as major connectivity hubs due to the concentration of landing stations.
- Large telecommunications and technology companies play a significant role in building and maintaining submarine cable infrastructure.
- Many submarine cables connect multiple countries simultaneously, forming complex global communication routes.

## Technologies Used
- Neo4j Graph Database
- Cypher Query Language
- Python (Neo4j Driver)
- CSV Dataset

## Project Motivation

This project demonstrates how graph databases can be used to model and analyze complex infrastructure networks. By representing submarine cable systems as a graph, it becomes easier to explore connectivity patterns, infrastructure ownership, and global communication pathways.

Graph databases provide powerful tools for analyzing network-based data, making them particularly suitable for applications such as telecommunications infrastructure, transportation systems, and social networks.
