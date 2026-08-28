# ⚔️ Project 2 - Deadpool Real-Time Webhook Alert Engine

A high-performance asynchronous webhook processor built with **FastAPI** and **Pydantic**. This engine receives real-time event telemetry from external clients, validates payload schemas, logs system audits, and dispatches dynamic alerts to a custom Telegram channel.

---

## 🚀 Key Features

* **Real-Time Webhook Ingestion**: Ingests HTTP POST JSON events dynamically.
* **Data Validation**: Strict schema enforcement using Pydantic models.
* **Telegram Integration**: Dynamic message formatting and automated dispatch.
* **Production Logging**: Dual-stream logging (Console + File Audit) with UTF-8 encoding support.
* **Error & Network Resiliency**: Explicit HTTP status modeling (`502 Bad Gateway`, `500 Internal Server Error`) with configurable request timeouts.
* **Traffic Simulator Included**: Standalone client testing script to simulate multi-priority enterprise payloads.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Framework**: FastAPI / Uvicorn
* **Data Validation**: Pydantic
* **HTTP Client**: Requests
* **Logging**: Standard Python Logging (`FileHandler` + `StreamHandler`)

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone (https://github.com/abhishtnarayan28007/deadpool-webhook-engine.git)
cd deadpool-webhook-engine
