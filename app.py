"""
Main Streamlit application file.
This script creates the user interface and orchestrates the entire workflow:
1.  Accepts user input (image and text).
2.  Saves the image temporarily for attachment.
3.  Shows a spinner while quickly processing the text data with the LLM.
4.  Displays the final, accurate JSON output to the user.
5.  Sends the data via email.
"""

import os
import streamlit as st
from dotenv import load_dotenv
from llm_processor import get_structured_car_data
from email_sender import send_car_listing_email
from image_classifier import get_car_body_type

load_dotenv()

#UI Configuration
st.set_page_config(page_title="Car Listing Assistant", layout="centered")
st.title("🚗 Car Listing Assistant")
st.markdown("Upload a car image and provide a description to automatically generate a structured listing and send it for review.")

TEMP_DIR = "temp"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

uploaded_image = st.file_uploader(
    "1. Upload a picture of the car",
    type=["png", "jpg", "jpeg"]
)
description_text = st.text_area(
    "2. Provide a detailed description of the car",
    height=200,
    placeholder="e.g., Blue Ford Fusion produced in 2015 featuring a 2.0-liter engine..."
)

#Submission Button and Logic
if st.button("Submit Listing", type="primary"):
    if uploaded_image is None or not description_text.strip():
        st.warning("⚠️ Please upload an image and provide a description before submitting.")
    else:
        with st.spinner("Analyzing text..."):
            try:
                image_path = os.path.join(TEMP_DIR, uploaded_image.name)
                with open(image_path, "wb") as f:
                    f.write(uploaded_image.getbuffer())
                st.info("Image saved temporarily.")

                st.info("Contacting the AI model for text analysis...")
                car_data = get_structured_car_data(description_text)

                if car_data:
                    st.success("✅ Text analysis complete!")
                    

                    final_body_type = car_data.body_type
                    if final_body_type == "Not Specified":
                        st.info("Body type not found in text. Using image classifier as a fallback...")
                        image_body_type = get_car_body_type(image_path)
                        final_body_type = image_body_type
                    
                    car_data.body_type = final_body_type
                    final_data_dict = car_data.model_dump()

                    st.subheader("Extracted Car Data:")
                    st.json(final_data_dict)

                    st.info("Sending data for review...")
                    email_sent = send_car_listing_email(final_data_dict, image_path)

                    if email_sent:
                        st.success("✅ Success! Your car listing has been submitted for review.")
                    else:
                        st.error("❌ Failed to send the listing email. Please check the application logs or your .env configuration.")
                else:
                    st.error("❌ Failed to process the text. The LLM might be unavailable or there could be an issue with the input.")

            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
            
            finally:
                if 'image_path' in locals() and os.path.exists(image_path):
                    os.remove(image_path)
                    print(f"INFO: Cleaned up temporary file: {image_path}")
