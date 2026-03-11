from neo4j import GraphDatabase
from dotenv import load_dotenv
from pathlib import Path
import os
import csv

env_path = Path (__file__).resolve().parent/".env"
load_dotenv(dotenv_path= env_path)

URL = os.getenv ("NEO4J_URL_LOCAL")
USERNAME = os.getenv ("NEO4J_USERNAME")
PASSWORD = os.getenv ("NEO4J_PASSWORD_LOCAL")

AUTH = (USERNAME, PASSWORD)

class Neo4jProvider:
    def __init__ (self):
        try:
            self.driver = GraphDatabase.driver(URL, auth=AUTH)
            self.driver.verify_connectivity()
            print("Succesfully Connected to Neo4j")

        except Exception as e:
            print("Error Connecting to Neo4j:",e)
            raise

    def closeConnection(self):
        if self.driver:
            self.driver.close()
            print("Connection to Neo4J Closed")

    def create_nodes_cables_csv(self, csv_file):
        with self.driver.session()as session:
            with open(csv_file, 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    session.run(
                        """
                        CREATE (a: Cables{
                            cable_id: $cable_id,
                            cable_name: $cable_name,
                            length_km: $length_km,
                            rfs_year: $rfs_year
                        })
                        """,
                        cable_id=int(row["cable_id"]),
                        cable_name=row["cable_name"],
                        length_km=int(row["length_km"]),
                        rfs_year=int(row["rfs_year"])
                    )
                print(f"Nodes Created from{csv_file}")

    def create_nodes_companies_csv(self, csv_file):
        with self.driver.session()as session:
            with open(csv_file, 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    session.run(
                        """
                        CREATE (b: Companies{
                            company_id: $company_id,
                            company_name: $company_name
                        })
                        """,
                        company_id=int(row["company_id"]),
                        company_name=row["company_name"]
                    )
                print(f"Nodes Created from{csv_file}")

    def created_nodes_countries_csv(self, csv_file):
        with self.driver.session()as session:
            with open(csv_file, 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    session.run(
                        """
                        CREATE (c: Countries{
                            country_id: $country_id,
                            country_name: $country_name
                        })
                        """,
                        country_id=int(row["country_id"]),
                        country_name=row["country_name"]
                    )
                print(f"Nodes Created from{csv_file}")
                      

    def created_nodes_landing_stations_csv(self, csv_file):
        with self.driver.session()as session:
            with open(csv_file, 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    session.run(
                        """
                        CREATE (d: Landing_stations{
                        station_id: $station_id,
                        station_name: $station_name,
                        country: $country,
                        latitude: $latitude,
                        longitude: $longitude
                        })
                        """,
                        station_id=int(row["station_id"]),
                        station_name=row["station_name"],
                        country=row["country"],
                        latitude=row["latitude"],
                        longitude=row['longitude']
                    )
                print(f"Nodes Created from{csv_file}")

    def created_nodes_oceans_csv(self, csv_file):
        with self.driver.session()as session:
            with open(csv_file, 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    session.run(
                        """
                        CREATE (e: Oceans{
                        ocean_id: $ocean_id,
                        ocean_name: $ocean_name
                        })
                        """,
                        ocean_id=int(row["ocean_id"]),
                        ocean_name=row["ocean_name"]
                    )
                print(f"Nodes Created from {csv_file}")

if __name__ == "__main__":
    neo4j = Neo4jProvider()
    neo4j.create_nodes_cables_csv("Data/cables.csv")
    neo4j.create_nodes_companies_csv("Data/companies.csv")
    neo4j.created_nodes_countries_csv("Data/countries.csv")
    neo4j.created_nodes_landing_stations_csv("Data/landing_stations.csv")
    neo4j.created_nodes_oceans_csv("Data/oceans.csv")
    neo4j.closeConnection()