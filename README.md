# SMS Spam Classification Using Naive Bayes

  Open App:
  <a href="https://sms-spam-classification-using-naive-bayes-sjwvf85xws5rdvz86bz3.streamlit.app/">
    <img src="https://img.shields.io/badge/Launch%20App-Streamlit-orange?logo=streamlit&logoColor=white" alt="Streamlit App"/>
  </a>
  
## Dataset Credits
This dataset is taken from the UCI Machine Learning Repository:  
[SMS Spam Collection Dataset](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)

## Project Objective
- Develop a machine learning model to distinguish between spam and ham (non-spam) SMS messages.
- Analyze SMS data through exploratory data analysis (EDA) and word frequency visualization.
- Implement and evaluate classification algorithms (e.g., Naive Bayes, SVM, Logistic Regression) using accuracy, precision, recall, and F1-score.
- Build a high-performance classifier for real-time SMS spam filtering.
- Contribute to automated messaging systems to improve communication safety and reduce spam.

## Model Performance Summary
- **Overall Accuracy**: 99% (1,115 out of 1,127 messages correctly classified)
  
### Ham Classification:
- **Precision**: 99%
- **Recall**: 100% (No ham messages misclassified)

### Spam Classification:
- **Precision**: 98%
- **Recall**: 96% (Small number of spam messages missed)
- **F1-Score (Spam)**: 0.97 (Strong balance between precision and recall)

- **Macro and Weighted Averages**: High performance across both classes

These metrics confirm the model's effectiveness for real-world SMS spam detection tasks.

## Conclusion
The Naive Bayes model demonstrates excellent performance in classifying SMS messages as either spam or ham. With an overall accuracy of **99%**, the model efficiently identifies both spam and ham messages, achieving:

- **High precision and recall for ham messages**: No ham messages were misclassified.
- **Strong precision and recall for spam messages**: Only a small number of spam messages were missed.
- **F1-Score of 0.97 for spam**: Reflecting a strong balance between precision and recall.

These metrics confirm that the model is highly reliable and suitable for real-world SMS spam detection tasks. The model can be applied in **real-time SMS filtering systems** to improve communication safety by reducing unwanted or malicious messages.

Further improvements could involve exploring other classification algorithms, refining the model for real-time performance, and addressing potential edge cases in spam detection.
