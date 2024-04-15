# Use the official miniconda base image
FROM continuumio/miniconda3:latest

# Set environment variables
ENV MLFLOW_HOME /mlflow
ENV MLFLOW_VERSION=1.20.2

# Install MLflow and dependencies
RUN pip install mlflow==$MLFLOW_VERSION

# Expose port 8080
EXPOSE 8080

# Start MLflow server
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "8080", "--backend-store-uri", "sqlite:///mlflow.db", "--default-artifact-root", "/mlflow"]
