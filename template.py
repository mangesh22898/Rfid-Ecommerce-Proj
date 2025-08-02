import os
from pathlib import Path

project_name = "rfid-ecommerce-system"

list_of_paths = [
    "frontend/Dockerfile",
    "frontend/package.json",
    "frontend/src/.placeholder",

    "services/catalog/Dockerfile",
    "services/catalog/manage.py",
    "services/catalog/catalog/.placeholder",
    "services/catalog/requirements.txt",

    "services/cart/Dockerfile",
    "services/cart/manage.py",
    "services/cart/cart/.placeholder",
    "services/cart/requirements.txt",

    "services/checkout/Dockerfile",
    "services/checkout/manage.py",
    "services/checkout/checkout/.placeholder",
    "services/checkout/requirements.txt",

    "services/orders/Dockerfile",
    "services/orders/manage.py",
    "services/orders/orders/.placeholder",
    "services/orders/requirements.txt",

    "services/email/Dockerfile",
    "services/email/email_worker.py",
    "services/email/requirements.txt",

    "mongodb/init.js",

    "manifests/ingress.yaml",
    "manifests/namespace.yaml",

    "manifests/frontend/deployment.yaml",
    "manifests/frontend/service.yaml",

    "manifests/catalog/deployment.yaml",
    "manifests/catalog/service.yaml",

    "manifests/cart/deployment.yaml",
    "manifests/cart/service.yaml",

    "manifests/checkout/deployment.yaml",
    "manifests/checkout/service.yaml",

    "manifests/orders/deployment.yaml",
    "manifests/orders/service.yaml",

    "manifests/email/deployment.yaml",
    "manifests/email/service.yaml",

    "manifests/mongodb/pvc.yaml",
    "manifests/mongodb/deployment.yaml",
    "manifests/mongodb/service.yaml",

    "manifests/config/mongo-secret.yaml",
    "manifests/config/backend-env.yaml",
    "manifests/config/email-secret.yaml",

    "argocd/app.yaml",
    "argocd/project.yaml",

    ".github/workflows/build.yml",
    ".github/workflows/deploy.yml",

    "docker-compose.yaml",
    "README.md",
]

for path_str in list_of_paths:
    full_path = Path(project_name) / Path(path_str)
    filedir = full_path.parent
    os.makedirs(filedir, exist_ok=True)
    # Skip actual files that are meant to be folders
    if not str(full_path).endswith(".placeholder"):
        with open(full_path, "w") as f:
            pass
