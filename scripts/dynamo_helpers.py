import boto3, json, time, os

dynamodb = boto3.resource("dynamodb")

def log_deployment(commit, env, url, model):
    table = dynamodb.Table("DeploymentTracking")
    table.put_item(Item={
        "commit_sha": commit,
        "environment": env,
        "status": "SUCCESS",
        "s3_url": url,
        "model_used": model,
        "timestamp": int(time.time())
    })

def save_analytics(resume_id):
    table = dynamodb.Table("ResumeAnalytics")
    data = json.load(open("analysis.json"))
    data["resume_id"] = resume_id
    table.put_item(Item=data)
