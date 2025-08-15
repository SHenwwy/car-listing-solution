from pydantic import BaseModel, Field
from typing import List, Optional

class Tire(BaseModel):
    """A model to represent the car's tires."""
    type: str = Field(..., description="The condition of the tires, e.g., 'brand-new', 'used'.")
    manufactured_year: Optional[int] = Field(None, description="The manufacturing year of the tires.")

class Notice(BaseModel):
    """A model for any special notices about the car, like repairs or accidents."""
    type: str = Field(..., description="The type of notice, e.g., 'collision', 'maintenance'.")
    description: str = Field(..., description="A detailed description of the notice.")

class Price(BaseModel):
    """A model to represent the car's price, including amount and currency."""
    amount: int = Field(..., description="The numerical price of the car.")
    currency: str = Field(..., description="The currency of the price, e.g., 'L.E', 'USD'.")

class Car(BaseModel):
    """The main model representing a complete car listing."""
    body_type: str = Field(
        "sedan", 
        description="The body type of the car (e.g., sedan, SUV). This is a placeholder and will be updated by the image classifier."
    )
    color: str = Field(..., description="The primary color of the car.")
    brand: str = Field(..., description="The brand or manufacturer of the car, e.g., 'Ford'.")
    model: str = Field(..., description="The model of the car, e.g., 'Fusion'.")
    manufactured_year: int = Field(..., description="The year the car was manufactured.")
    motor_size_cc: int = Field(..., description="The engine size in cubic centimeters (cc).")
    tires: Tire = Field(..., description="Information about the car's tires.")
    windows: str = Field(..., description="Description of the car's windows, e.g., 'tinted', 'clear'.")
    notices: List[Notice] = Field(..., description="A list of important notices about the car.")
    price: Price = Field(..., description="The selling price of the car.")
    mileage_km: Optional[int] = Field(None, description="The car's mileage in kilometers. Extract if available.")
    mileage_miles: Optional[int] = Field(None, description="The car's mileage in miles. Extract if available.")

