"""
This module contains the dummy function for car body type classification.
It mimics the behavior of a real computer vision model.
When the real model is ready, you can replace the logic in this function
without changing any other part of the application.
"""

import random

def get_car_body_type(image_path: str) -> str:
    """
    Simulates a computer vision model to classify the car's body type from an image.

    Args:
        image_path (str): The file path to the car image. Although unused in this
                          dummy version, it's included to match the real model's signature.

    Returns:
        str: A randomly selected car body type.
    """
    print(f"INFO: [DUMMY] Classifying image at {image_path}...")
    
    # Predefined list of possible car body types.
    body_types = ["sedan", "SUV", "hatchback", "coupe", "convertible", "minivan", "truck"]
    
    # In a real-world scenario, you would load your CV model here and
    classified_type = random.choice(body_types)
    
    print(f"INFO: [DUMMY] Classified body type as: {classified_type}")
    return classified_type

