🚀 Multi-Exchange Real-Time Analytics Engine
A high-performance Python backend designed to ingest, process, and alert on live cryptocurrency market data. This project demonstrates asynchronous programming, multi-source data integration, and modular software architecture—essential skills for modern fintech and backend roles.

🛠 Project Roadmap
Phase 1: Ingestion Engine (Current Status ✅)
Multi-Exchange Support: Built-in drivers for Binance (Global/US) and Coinbase Advanced Trade.

Asynchronous I/O: Utilizes asyncio and websockets to handle high-throughput data streams without blocking.

Regional Compliance: Configured to handle US-based API restrictions (HTTP 451) by routing through compliant endpoints.

Phase 2: The "Brain" (Logic & Thresholds 🏗️)
State Management: Transition from hard-coded variables to dynamic alert configurations.

Price Thresholds: Logic to trigger events when an asset crosses a specific price point.

Volatility Monitoring: Calculate "Percent Change" over time (e.g., alert if BTC drops 2% in 5 minutes).

Data Validation: Ensure price data is sanitized and converted from strings to floats for mathematical operations.

Phase 3: The "Messenger" (Notifications & Persistence)
Alert Delivery: Integration with Telegram Bot API, Twilio (SMS), or SMTP for real-time notifications.

Database Integration: Use SQLite or Redis to store user-defined alerts so they persist even if the script restarts.

Logging: Implementation of a professional logging system to track alert history and system health.

Phase 4: Deployment & DevOps
Containerization: Wrapping the engine in Docker for "one-click" deployment.

CI/CD: GitHub Actions to automatically run unit tests (pytest) on every push.