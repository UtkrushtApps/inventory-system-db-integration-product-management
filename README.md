# InventoryPro: Product Management DB Implementation Task

## Task Overview
InventoryPro is building a backend inventory management system using FastAPI. All routing and API scaffolding is already in place, but the database integration is missing. Your responsibility is to design and implement the PostgreSQL schema for products and write the async-compatible logic to allow adding and fetching products through existing endpoints. Proper schema design and async DB handling are critical for ensuring smooth operations under real-world load.

## Guidance
- Work only within the provided `app/database.py`, `app/models.py`, and `schema.sql` files for the database integration.
- The FastAPI application and endpoints are complete in `app/main.py`.
- Use `run.sh` and `docker-compose.yml` to set up and run the infrastructure. PostgreSQL is pre-configured.

## Objectives
- Create a PostgreSQL table named `products` with well-typed columns for product id, name, sku, quantity, and price.
- Enforce data integrity with appropriate constraints (uniqueness, not null, correct numeric types) and define at least one useful index.
- Implement SQLAlchemy model(s) to match the schema and provide async database access logic for creating a product and fetching all products, using the provided FastAPI endpoints.
- Ensure that all database operations are performed asynchronously (non-blocking) and follow safe transactional patterns.

## How to Verify
- Use `run.sh` to initialize and launch the system.
- POST product data to `/products/` and confirm the row is inserted in the PostgreSQL database.
- GET `/products/` and verify products are correctly and efficiently retrieved from the DB, and that results match the stored data.
- Use a DB client (pgAdmin, DBeaver, psql) to check that schema, constraints, and index are created as intended.
- Ensure the API remains responsive under multiple rapid add/list operations.
