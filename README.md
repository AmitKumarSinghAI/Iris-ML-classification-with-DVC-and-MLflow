# Iris ML Classification with MLflow, DVC, AWS, CI/CD & Docker

## 📌 Project Overview

This project implements an **end-to-end Machine Learning (MLOps) pipeline** for Iris flower classification.

The project demonstrates how a machine learning model can be developed, versioned, tracked, automated, containerized, and deployed using modern **MLOps tools and cloud services**.

The complete workflow integrates:

* 🐍 Python
* 🤖 Machine Learning
* 📊 MLflow
* 🔄 DVC
* ☁️ AWS S3
* 🔐 AWS IAM & GitHub OIDC
* ⚙️ GitHub Actions
* 🐳 Docker
* 🐳 Docker Hub
* 🔁 DVC Pipeline (`dvc.yaml`)

The goal of this project is to understand and implement a **production-style ML workflow**, from dataset management and model training to CI/CD and containerization.

---

## 🏗️ Project Architecture

```text
                    ┌──────────────────┐
                    │   Iris Dataset   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      DVC         │
                    │ Data Versioning  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     AWS S3       │
                    │ Remote Storage   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Data Processing  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Model Training   │
                    │ Scikit-learn     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     MLflow       │
                    │ Experiment Track │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Trained Model   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Docker      │
                    │ Containerization │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Docker Hub     │
                    │ Image Registry   │
                    └──────────────────┘

             GitHub Actions CI/CD
                     │
                     ▼
          Automated Build & Pipeline
```

---

# 🚀 Features

### 1. Machine Learning

The project uses the **Iris dataset** to train a classification model capable of predicting the species of an Iris flower.

The ML workflow includes:

* Data loading
* Data preprocessing
* Train/test split
* Model training
* Model evaluation
* Model saving

---

### 2. DVC – Data Version Control

[DVC](https://dvc.org/) is used to version and manage the dataset and ML pipeline.

Instead of storing large datasets directly in Git, DVC tracks the dataset and stores the actual data in remote storage.

Example:

```bash
dvc add data/iris.csv
```

The project also uses:

```text
dvc.yaml
```

to define the ML pipeline stages.

DVC helps make the ML workflow:

* Reproducible
* Version controlled
* Trackable
* Easier to collaborate on

---

### 3. DVC Pipeline

The complete ML workflow is defined using `dvc.yaml`.

Example pipeline structure:

```text
Data
 ↓
Preprocessing
 ↓
Training
 ↓
Evaluation
```

The pipeline can be reproduced using:

```bash
dvc repro
```

This allows the complete ML pipeline to run automatically when dependencies or parameters change.

---

### 4. AWS S3

AWS S3 is used as remote storage for DVC.

The workflow is:

```text
Local Dataset
      ↓
     DVC
      ↓
   AWS S3
```

This allows datasets and DVC-tracked files to be stored remotely rather than only on the local machine.

DVC remote configuration is used to connect the project with an AWS S3 bucket.

---

### 5. MLflow

[MLflow](https://mlflow.org/) is used for **experiment tracking and model management**.

During training, MLflow can track:

* Parameters
* Metrics
* Model information
* Experiments
* Runs

Typical workflow:

```text
Model Training
      ↓
    MLflow
      ↓
Parameters + Metrics + Model
```

This makes it easier to compare different experiments and understand model performance.

---

### 6. AWS IAM & GitHub OIDC

AWS IAM is integrated with GitHub Actions to provide secure authentication.

Instead of storing long-term AWS access keys inside GitHub, the workflow uses **GitHub OIDC** to authenticate with AWS.

The basic flow is:

```text
GitHub Actions
      ↓
GitHub OIDC
      ↓
AWS IAM Role
      ↓
AWS Services
```

This provides a more secure approach for CI/CD authentication.

---

### 7. GitHub Actions CI/CD

GitHub Actions is used to automate the ML workflow.

The CI/CD pipeline can automatically:

1. Checkout the repository
2. Set up Python
3. Install dependencies
4. Authenticate with AWS
5. Access DVC data
6. Run the ML pipeline
7. Run tests
8. Build the Docker image
9. Push the Docker image to Docker Hub

Example workflow:

```text
Git Push
   ↓
GitHub Actions
   ↓
Install Dependencies
   ↓
AWS Authentication
   ↓
DVC Data
   ↓
Run ML Pipeline
   ↓
Run Tests
   ↓
Build Docker Image
   ↓
Push to Docker Hub
```

---

# 🐳 Docker

Docker is used to containerize the ML application.

The project includes a:

```text
Dockerfile
```

The Docker image contains the required environment and dependencies needed to run the application.

Build the image locally:

```bash
docker build -t iris-ml-classification .
```

Run the container:

```bash
docker run iris-ml-classification
```

---

# 🐳 Docker Hub

After building the Docker image, it can be pushed to Docker Hub.

Example:

```bash
docker login
```

Tag the image:

```bash
docker tag iris-ml-classification <dockerhub-username>/iris-ml-classification:latest
```

Push the image:

```bash
docker push <dockerhub-username>/iris-ml-classification:latest
```

The GitHub Actions workflow can automate this process.

---

# 📁 Project Structure

```text
Iris-ML-classification-with-DVC-and-MLflow/
│
├── .dvc/
│
├── .github/
│   └── workflows/
│       └── ml-ci.yml
│
├── data/
│   ├── iris.csv
│   └── iris.csv.dvc
│
├── src/
│   ├── data_preprocessing.py
│   ├── train.py
│   └── evaluate.py
│
├── tests/
│   └── test_*.py
│
├── Dockerfile
├── dvc.yaml
├── dvc.lock
├── requirements.txt
├── params.yaml
├── .gitignore
├── .dockerignore
└── README.md
```

> The exact filenames may differ depending on the final version of the project.

---

# 🛠️ Technologies Used

| Technology     | Purpose                            |
| -------------- | ---------------------------------- |
| Python         | Programming language               |
| Scikit-learn   | Machine Learning                   |
| Pandas         | Data processing                    |
| NumPy          | Numerical computation              |
| MLflow         | Experiment tracking                |
| DVC            | Data & pipeline versioning         |
| AWS S3         | Remote data storage                |
| AWS IAM        | Cloud authentication & permissions |
| GitHub Actions | CI/CD automation                   |
| Docker         | Containerization                   |
| Docker Hub     | Container image registry           |
| Git            | Version control                    |
| GitHub         | Source code management             |

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd Iris-ML-classification-with-DVC-and-MLflow
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔄 Run the DVC Pipeline

To reproduce the complete ML pipeline:

```bash
dvc repro
```

Check the pipeline status:

```bash
dvc status
```

Run DVC data pull if the dataset is stored remotely:

```bash
dvc pull
```

---

# 📊 MLflow

Start the MLflow UI:

```bash
mlflow ui
```

Then open the MLflow interface in your browser.

The MLflow interface allows you to inspect:

* Experiments
* Runs
* Parameters
* Metrics
* Models

---

# ☁️ DVC + AWS S3

If the DVC remote is configured with AWS S3, data can be pushed using:

```bash
dvc push
```

And downloaded using:

```bash
dvc pull
```

This separates:

```text
Git → Source Code
DVC → Dataset & ML artifacts
AWS S3 → Remote Storage
```

---

# 🧪 Testing

Run the test suite using:

```bash
pytest
```

Tests can also be executed automatically inside the GitHub Actions CI/CD pipeline.

---

# 🔐 CI/CD Configuration

The GitHub Actions workflow uses secure credentials and authentication mechanisms.

For AWS authentication, GitHub OIDC is used with an AWS IAM role.

For Docker Hub authentication, GitHub repository variables and secrets are used.

Typical configuration includes:

```text
GitHub Variables
└── DOCKERHUB_USERNAME

GitHub Secrets
└── DOCKERHUB_TOKEN
```

AWS-related configuration is handled through the GitHub Actions environment and IAM/OIDC setup.

> Never commit AWS access keys, Docker Hub passwords, tokens, or other secrets directly into the repository.

---

# 🔁 Complete MLOps Workflow

The complete workflow implemented in this project is:

```text
                    ┌─────────────┐
                    │   GitHub    │
                    └──────┬──────┘
                           │
                         Push
                           │
                           ▼
                  ┌─────────────────┐
                  │ GitHub Actions  │
                  └────────┬────────┘
                           │
                    AWS OIDC Login
                           │
                           ▼
                  ┌─────────────────┐
                  │     AWS IAM     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │     AWS S3      │
                  │   DVC Storage   │
                  └────────┬────────┘
                           │
                       DVC Pull
                           │
                           ▼
                  ┌─────────────────┐
                  │  DVC Pipeline   │
                  │    dvc repro    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Model Training  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │     MLflow      │
                  │ Experiment Track│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Docker Build   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   Docker Hub    │
                  └─────────────────┘
```

---

# 🎯 What I Learned

Through this project, I learned how to build an end-to-end MLOps workflow instead of only training a machine learning model.

### Machine Learning

* Data preprocessing
* Classification
* Model training
* Model evaluation
* Model saving

### MLOps

* Experiment tracking with MLflow
* Dataset versioning with DVC
* Pipeline automation with DVC
* Reproducible ML workflows
* Remote storage using AWS S3

### Cloud & DevOps

* AWS S3
* AWS IAM
* GitHub OIDC
* GitHub Actions
* CI/CD pipelines
* Docker
* Docker Hub

---

# 🚀 Future Improvements

The project can be extended with:

* Model deployment using AWS
* MLflow Model Registry
* Automated model deployment
* Model monitoring
* Data validation
* Model performance monitoring
* REST API using FastAPI
* Kubernetes deployment
* AWS ECR
* AWS ECS
* Cloud-based MLflow tracking server
* Automated retraining pipeline

---

# 👨‍💻 Author

**Amit Kumar Singh**

Computer Science Student | Aspiring GenAI / ML Engineer

Interested in:

* Machine Learning
* Generative AI
* MLOps
* AI Automation
* Cloud Computing
* DevOps

---

# ⭐ If You Like This Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📌 Project Summary

This project demonstrates a complete **MLOps lifecycle**:

```text
Data
 ↓
DVC
 ↓
AWS S3
 ↓
Data Processing
 ↓
Model Training
 ↓
MLflow
 ↓
Testing
 ↓
GitHub Actions
 ↓
Docker
 ↓
Docker Hub
```

The main objective is to create a **reproducible, automated, version-controlled, and containerized machine learning pipeline** using modern MLOps practices.