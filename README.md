# FastAPI Food Ordering System

This is a simple FastAPI-based food ordering system that allows users to view a menu, place orders, and retrieve order receipts.

## Features

- View the menu items with their details.
- Place orders with specified quantities.
- Retrieve order receipts with order details and total cost.

## Project Structure

- `main.py`: Contains the FastAPI application and API routes.
- `menu.py`: Contains the menu items and the menu API routes.
- `order.py`: Contains the order-related data and the order API routes.
- `models/`: Directory containing data models used in the application.
- `tests/`: Directory containing test files for the application.

## Setup

1. Clone the repository.

```
git clone https://github.com/aphommathep/food_ordering_api.git
cd food_ordering_api
```

1. Install the required dependencies.
```
pip install -r requirements.txt
```

2. Run the FastAPI application.
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API should now be accessible at http://localhost:8000.

## API Endpoints

GET /menu: Get a list of available menu items.
POST /order: Submit an order.
GET /order/{id}: Get an order receipt by order ID.

## Sample Requests and Responses

You can find sample requests and responses for these endpoints in the project's `samples` directory.

## Testing

To run the test suites, use pytest.

```
pytest
```

## Contributing

Pull requests and issues are welcome. Feel free to contribute to this project.

## License

This project is licensed under the MIT License.