import streamlit as st
import joblib

# Load the trained model once when the script starts
model = joblib.load("spam_classifier_pipeline.joblib")


def predict_spam(message):
    if isinstance(message, str):
        # Predict using the loaded model
        prediction = model.predict([message])[0]
        return "Spam" if prediction == "spam" else "Not Spam"
    else:
        raise ValueError("Input should be a string")


def main():
    # Set up Streamlit app UI
    st.set_page_config(page_title="Spam Message Classifier", page_icon="📩")

    # Title with colorful text
    st.markdown(
        """
        <h1 style='text-align: center; color: #ff6347;'>Spam Message Classifier</h1>
        <p style='text-align: center; color: #008080;'>Enter a message and get the prediction.</p>
        """,
        unsafe_allow_html=True
    )

    # Change background color of the app
    st.markdown(
        """
        <style>
            .reportview-container {
                background-color: #f0f8ff;
            }
            .css-1d391kg {
                color: #ff6347;
            }
            .css-1aumxhk {
                background-color: #008080;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input form for message
    user_input = st.text_input("Enter your message:", key="user_message")

    # Display prediction result
    if user_input:
        result = predict_spam(user_input)
        if result == "Spam":
            st.markdown(f"<h3 style='text-align: center; color: red;'>{result}</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='text-align: center; color: green;'>{result}</h3>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
