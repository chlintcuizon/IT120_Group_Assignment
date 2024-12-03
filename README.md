
# Django SMS Application with Twilio  

## Overview  
This application is a Django-based project that allows users to send SMS messages using Twilio. 
It demonstrates how to integrate Twilio's messaging API with Django to enable SMS functionality.  

## Features  
- Simple and user-friendly interface for sending SMS.  
- Integration with Twilio for reliable message delivery.  
- Form validation to ensure correct phone number format and message content.  

## How It Works  

1. **Setup**:  
   - Install the necessary dependencies, including Django and Twilio SDK.  
   - Configure Twilio account credentials (Account SID, Auth Token, and Phone Number) in the project settings.  

2. **User Interface**:  
   - A form is provided on the web page for users to input the recipient's phone number and the message text.  

3. **Backend Logic**:  
   - When the form is submitted, the application validates the input.  
   - The Twilio SDK is used to send the SMS to the recipient.  

4. **Confirmation**:  
   - After sending the SMS, the user receives a confirmation message indicating success or failure.  

## How to Run  

1. **Clone the Repository**:  
   ```bash  
   git clone <repository-url>  
   cd <project-directory>  
   ```  

2. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Set Up Twilio Credentials**:  
   - Add your Twilio `ACCOUNT_SID`, `AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` to the `.env` file or directly into the `settings.py` file.  

4. **Run the Server**:  
   ```bash  
   python manage.py runserver  
   ```  

5. **Access the Application**:  
   Open your browser and go to `http://127.0.0.1:8000`.  

## Dependencies  
- Django  
- Twilio Python SDK  

## Notes  
- Ensure your Twilio account is active and has enough credits to send SMS messages.  
- Follow the proper format for phone numbers (E.164 format recommended).  

## License  
This project is for educational purposes and is not licensed for commercial use.  
