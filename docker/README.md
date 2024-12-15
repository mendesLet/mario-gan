Running mario-gpt environment with Docker
===

This implementation uses a image from [Colab Runtime](https://research.google.com/colaboratory/local-runtimes.html) Since we started developing in colab, then it was needed to migrate quickly to local resources.

### - Docker Compose:
1. Up the compose (`-d` is for detaching from the application):
    ```sh
    docker compose -f docker/docker-compose.yaml up -d
    ```
2. Now you must be able to access the *jupyter notebook environment* via:  
    http://localhost:8181/