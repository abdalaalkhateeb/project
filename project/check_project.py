import os
import importlib.util

print(" Project Verification Script Running...\n")

errors = []
project_root = os.getcwd()

#  Step 1: Check required folders and files
required_paths = [
    "core",
    "core/models.py",
    "core/views.py",
    "core/serializers",
    "core/urls",        
    "project/settings.py",
    "project/urls.py",
]

print(" Project structure check:")
for path in required_paths:
    full_path = os.path.join(project_root, path)
    if os.path.exists(full_path):
        print(f" Found: {path}")
    else:
        print(f" Missing: {path}")
        errors.append(f"Missing: {path}")

#  Step 2: Check database engine
print("\n Database engine configuration:")
try:
    spec = importlib.util.spec_from_file_location("settings", "tourism_guide/settings.py")
    settings_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(settings_module)
    db = settings_module.DATABASES["default"]
    if "mssql" in db.get("ENGINE", ""):
        print(" Using SQL Server via mssql.")
    else:
        print(" Wrong or missing database engine.")
        errors.append("Invalid DB engine")
except Exception as e:
    print(f" Error loading settings.py: {e}")
    errors.append("settings.py error")

#  Step 3: Check if JWT is included
print("\n JWT Authentication check:")
try:
    if "rest_framework_simplejwt" in settings_module.INSTALLED_APPS:
        print(" JWT is configured in INSTALLED_APPS.")
    else:
        print(" JWT is missing from INSTALLED_APPS.")
        errors.append("JWT missing")
except Exception as e:
    print(f" Error reading INSTALLED_APPS: {e}")
    errors.append("JWT error")


print("\n Final Report:")
if not errors:
    print(" Project structure and configuration look GOOD.")
else:
    print(" Detected problems:")
    for err in errors:
        print("-", err) 