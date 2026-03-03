# Kafka Local Development Lab

This project demonstrates a complete end-to-end Apache Kafka setup using Docker. It covers infrastructure provisioning, broker configuration, CLI-based administrative tasks, and custom application development using Python.

## 🚀 Project Overview

The goal of this lab was to establish a robust local Kafka environment and master the core components of the Kafka ecosystem.

### 1. Infrastructure (Docker & Compose)
* **Cluster:** Orchestrated a Kafka broker and Zookeeper instance using Confluent Community Docker images.
* **Network Configuration:** Configured `KAFKA_ADVERTISED_LISTENERS` to enable seamless communication between the Linux-based Docker containers and the host Windows environment via `localhost:9092`.

### 2. Kafka Configuration & Internals
* Analyzed `server.properties` within the containerized environment.
* Mastered key parameters:
    * `listeners`: The internal interface Kafka binds to.
    * `advertised.listeners`: The metadata shared with clients for connection routing.
    * `security.protocol.map`: Mapping internal and external traffic to the `PLAINTEXT` protocol.

### 3. CLI Power-User Exercises
Demonstrated proficiency with the following Kafka CLI tools:
* **Topic Management:** Created and described topics with specific partition and replication factors.
* **Data Streams:** Utilized `kafka-console-producer` and `kafka-console-consumer` to test real-time data flow.
* **Performance Testing:** Executed `kafka-producer-perf-test` to stress-test the cluster with **100,000 records**, achieving consistent throughput and low latency.
* **Group Management:** Monitored consumer progress and **LAG** using `kafka-consumer-groups`.

### 4. Custom Python Implementation
Developed high-performance scripts using the `confluent-kafka` library:
* **Producer:** Simulates real-time sensor data (JSON) with delivery reports.
* **Consumer:** Implements a consumer group that processes the data backlog from the performance tests using `auto.offset.reset: earliest`.

---

## 🛠️ How to Run

### Prerequisites
* Docker Desktop
* Python 3.12+
* `pip install confluent-kafka`

### Setup
1. **Start the Cluster:**
   ```bash
   docker-compose up -d
