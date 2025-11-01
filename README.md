## Sentiment-Analysis-for-Movies-Reviews-and-Translation

A **Machine Learning** and **NLP-based** project for performing **sentiment analysis** on IMDB movie reviews.  
This project demonstrates **data preprocessing**, **model training**, **Flask-based deployment**, and **AWS CI/CD automation** using GitHub Actions.

---

## 📦 Dataset  
**Source:** IMDB Movie Review Dataset  
- 50,000 labeled reviews (Positive / Negative)  
- CSV Format: `IMDB-Dataset.csv`

---

## ⚙️ Installation  

Clone the repository and install dependencies:

```bash
git clone https://github.com/prasad939/Sentiment-Analysis-for-Movies-Reviews-and-Translation.git
cd "Sentiment Analysis for Movies Reviews and Translation"
pip install -r requirements.txt

### Model Training

- Train the sentiment classifier model:
python main.py

This will:

Load and preprocess IMDB dataset

Train a TF-IDF + Classifier pipeline

Save the model in:
sentimentanalysis/models/model/classifier.pkl

## Flask Application (Local Deployment)

- Run the Flask API to serve the trained model:
python SentimentAnalyzerEngine.py

- Endpoints:

/ → Home Page (Input text)

/predict → Returns sentiment result (Positive / Negative)

## AWS Deployment (CI/CD Pipeline)
1. Continuous Integration (CI)

GitHub Actions workflow (.github/workflows/ci-cd.yml) automatically:

Installs dependencies

Runs tests (tests/test_app.py)

Checks code quality

Builds Docker image

 2. Continuous Deployment (CD)

On successful CI:

Docker image is pushed to Amazon ECR

Flask app is deployed to AWS EC2 / Elastic Beanstalk


## Project Structure
📦 sentiment-analysis-for-movie-reviews
│
├── sentimentanalysis/
│   ├── models/
│   │   └── model/classifier.pkl
│   └── __init__.py
│
├── dataloader/
│   └── dataload.py
│
├── datapreprocessing/
│   ├── datapreprocessing.py
│   └── vectorizer.py
│
├── evaluation/
│   └── evaluationmetrics.py
│
├── Templates/
│   ├── home.html
│   └── predict.html
│
├── SentimentAnalyzerEngine.py   # Flask app
├── main.py                      # Model training
├── awsengine.py                 # AWS Integration
├── requirements.txt
├── Dockerfile
├── .github/workflows/ci-cd.yml
└── README.md


## pytest tests/
pytest tests/


## Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to modify.

Ensure all tests pass before merging.

## License

MIT


## Author

- Prasad @prasad939

M.Sc Chemistry (NIT Silchar) | Machine Learning Engineer


---

Would you like me to also include **badges** (e.g., build passing ✅, Python version, license, AWS deploy) at the top for a more professional GitHub look?

