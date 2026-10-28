# MLOps Lab & Practice Repository (U23ADP17)

This repository contains an end-to-end hands-on laboratory course and practice suite covering the entire Machine Learning Operations (MLOps) lifecycle, trained, tested, and validated using the `IRIS.csv` dataset.

---

## 📂 Project Structure

```
mlops/
├── IRIS.csv                        # Raw dataset (SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species)
├── MLOps_Lab_Notebook.ipynb        # Main laboratory notebook with all executed outputs & plots
├── .gitignore                      # Git ignore file
└── mlops_lab/                      # Generated MLOps pipeline components & artifacts
    ├── data/                       # Tracked datasets (DVC versioned: v1 and v2)
    ├── models/                     # Serialized models (.joblib and portable .onnx)
    ├── tests/                      # Automated CI unit tests (test_pipeline.py)
    ├── docker_demo/                # Dockerfile and containerized training script
    ├── airflow_dags/               # Apache Airflow workflow DAG definition
    ├── iac/                        # Infrastructure as Code (Terraform & Ansible playbooks)
    ├── .github/workflows/          # CI pipeline definition (ci.yml)
    ├── serve.py                    # Flask microservice model inference API
    ├── model_monitor.log           # Production prediction logs and drift alerts
    └── mlflow.db                   # MLflow SQLite tracking database
```

---

## 🚀 Course Units & Covered Concepts

### 1. Introduction to MLOps (Unit I)
* Differences between standard DevOps and MLOps.
* Live demonstration of **model decay** caused by data drift.
* Scalability and training time benchmarking across expanding dataset sizes.

### 2. Data & Model Management (Unit II)
* **Data Versioning (DVC)**: Tracking datasets with pointer files, saving versions `v1` and `v2`, and verifying time-travel checkout.
* **Feature Store**: Centralized feature computation and retrieval service (`MiniFeatureStore`).
* **Experiment Tracking & Model Registry (MLflow)**: Tracking hyperparameters (`n_estimators`, `max_depth`), metrics (`accuracy`), and registering production models.
* **Reproducibility with Docker**: Containerized environment packaging.

### 3. Continuous Integration & Continuous Deployment (Unit III)
* **CI Quality Testing**: Automated unit tests for data integrity and model performance thresholds using `pytest`.
* **CI/CD Workflows**: GitHub Actions CI workflow configuration (`ci.yml`).
* **Model Packaging**: Portable export with **Joblib** and **ONNX** (`skl2onnx` + `onnxruntime`).
* **Deployment Strategies**: A/B testing traffic routing simulation and canary/rolling updates (10% $\rightarrow$ 100%).
* **Orchestration & IaC**: Airflow pipeline orchestration and declarative cloud provisioning with Terraform and Ansible.

### 4. Monitoring & Maintenance (Unit IV)
* **Drift Detection**: Kolmogorov-Smirnov (KS) test and Population Stability Index (PSI) tracking feature distributions.
* **Concept Drift Simulation**: Handling label relationships changing over time.
* **Alerting**: Logging prediction inputs and raising alerts when drift thresholds are breached.
* **Retraining Strategies**: Event-driven vs. scheduled retraining triggers.
* **Fairness & Cost Optimization**: Subgroup parity evaluation and serverless vs. dedicated infrastructure break-even analysis.

### 5. Advanced Topics & End-to-End Capstone (Unit V & Day 4)
* **Scaling**: Microservice API serving (`Flask`) and multi-core parallel batch predictions.
* **Privacy & Security**: Multi-client Federated Learning (`FedAvg`) and Differential Privacy (`Laplace` noise mechanism).
* **Edge ML & Explainability**: ONNX Runtime inference latency benchmarking and Permutation Feature Importance analysis.
* **Capstone Pipeline**: Unified 7-step autonomous pipeline validating data, tracking runs with MLflow, enforcing quality gates, packaging to ONNX, monitoring live drift, and triggering retraining.

---

## 🛠️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kavibalan-png/MLOPS_PRACTICE.git
   cd MLOPS_PRACTICE
   ```

2. **Install required dependencies:**
   ```bash
   pip install scikit-learn pandas numpy scipy matplotlib joblib mlflow dvc skl2onnx onnxruntime pytest flask
   ```

3. **Run the unit tests:**
   ```bash
   pytest mlops_lab/tests -v
   ```

4. **Launch Jupyter and explore the notebook:**
   ```bash
   jupyter notebook MLOps_Lab_Notebook.ipynb
   ```
