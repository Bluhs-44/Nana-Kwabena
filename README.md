# Simple E-commerce Platform

This repository contains a minimal example of an e-commerce web application built
with [Flask](https://flask.palletsprojects.com/). It provides product listings,
a simple shopping cart and a mock checkout flow.

## Setup

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000`.

## Features

- View a list of products
- Add items to a shopping cart
- Review cart contents
- Mock checkout that generates an order confirmation ID

This project is intended as a starting point for a more complete
implementation. For a production deployment you should add persistent data
storage and integrate with a real payment gateway.
