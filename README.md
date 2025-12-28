# AI-Powered Resume CI/CD Pipeline

This project demonstrates a **complete DevOps pipeline** that automatically converts a Markdown resume into a professional HTML website using AI, analyzes it for ATS (Applicant Tracking System) readiness, and deploys it to AWS S3 with full tracking in DynamoDB.

The pipeline is **GitHub-based**, uses **CloudFormation for infrastructure as code**, and includes **beta → production deployment flow**. This project is ideal for showcasing **AWS, Python, CI/CD, and automation skills**.

---

## 🔹 Project Features

- Converts `resume.md` into a professional HTML website using AI
- Analyzes resume for **ATS readiness**
- Stores **structured analytics in DynamoDB**
- Deploys HTML website to **S3 bucket** with separate environments:
  - Pull Requests → `beta/`
  - Merges to main → `prod/`
- Tracks all deployments in DynamoDB for **auditability**
- Infrastructure defined in **CloudFormation**
- Full **CI/CD automation using GitHub Actions**

---

## 🗂 Project Structure

