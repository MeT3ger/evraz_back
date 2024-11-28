# ======================= #
#      deploy SECTION     #
# ======================= #

# MARK: u need to have permissions on yc account. It's need for DevOps tools.

# Build Docker image
docker build -t my-fastapi-app . 

# Tag Docker image
docker tag my-fastapi-app cr.yandex/crp66ciuio69atnlctbc/my-fastapi-app:hello

# Push Docker image to Yandex Container Registry
docker push cr.yandex/crp66ciuio69atnlctbc/my-fastapi-app:hello