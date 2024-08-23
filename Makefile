gen-clients:
	openapi-generator-cli generate -i data/openapi-spec.yaml -g javascript -o ./ui/canvas-client

build:
	docker compose build api-deploy ui-deploy provisioner-deploy

tag:
	docker tag cloud-canvas-api-deploy:latest us-central1-docker.pkg.dev/rad-containers-hmed/cloud-canvas/api:latest
	docker tag cloud-canvas-ui-deploy:latest us-central1-docker.pkg.dev/rad-containers-hmed/cloud-canvas/ui:latest
	docker tag cloud-canvas-provisioner-deploy:latest us-central1-docker.pkg.dev/rad-containers-hmed/cloud-canvas/provisioner:latest

upload: build tag
	docker push us-central1-docker.pkg.dev/rad-containers-hmed/cloud-canvas/api:latest
	docker push us-central1-docker.pkg.dev/rad-containers-hmed/cloud-canvas/ui:latest
	docker push us-central1-docker.pkg.dev/rad-containers-hmed/cloud-canvas/provisioner:latest


deploy: build tag upload
	gcloud run deploy ui \
		--image=us-central1-docker.pkg.dev/rad-containers-hmed/cloud-canvas/ui:latest \
		--execution-environment=gen2 \
		--region=us-central1 \
		--project=rad-dev-canvas-kwm6 \
		&& gcloud run services update-traffic ui --to-latest --region us-central1 --project=rad-dev-canvas-kwm6


# gcloud run deploy api \
# 		--image=us-central1-docker.pkg.dev/rad-containers-hmed/cloud-canvas/api:latest \
# 		--execution-environment=gen2 \
# 		--region=us-central1 \
# 		--project=rad-dev-canvas-kwm6 \
# 		&& gcloud run services update-traffic api --to-latest --region us-central1 --project=rad-dev-canvas-kwm6 && \
