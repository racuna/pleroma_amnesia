import requests
import json
import datetime

# Autenticación en Pleroma
headers = {
    "Authorization": "Bearer <TU_ACCESS_TOKEN>",
    "Content-Type": "application/json"
}

# Obtener todas las publicaciones
response = requests.get("https://<pleroma.instance>/api/v1/timelines/home", headers=headers)
posts = response.json()

# Calcular un año antes de la fecha actual
current_date = datetime.datetime.now()
year_ago = current_date - datetime.timedelta(days=365)

# Eliminar publicaciones antiguas de más de un año
for post in posts:
    post_date = datetime.datetime.strptime(post["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    if post_date < year_ago:
        post_id = post["id"]
        requests.delete("https://<pleroma.instance>/api/v1/statuses/" + post_id, headers=headers)
