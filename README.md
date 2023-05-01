# Environment Setup
conda create -n standard-api python=3.9
conda activate standard-api
pip install -r requirements.txt 

# Setup pre-commit (To avoid pre-commit hooks use: git commit -m "my message" --no-verify)
put 'pre-commit' in requirements.txt 
pip install -r requirements.txt 
pre-commit install
create and config file .pre-commit-config.yaml

# Run docker
cd docker
docker-compose up

# Run project
sh bin/run.sh
