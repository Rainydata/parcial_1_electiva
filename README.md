# parcial_1_electiva


# Clone the repository
git clone https://github.com/Rainydata/parcial_1_electiva.git
cd C:\Users\benav\OneDrive\Documentos\GitHub\parcial_1_electiva

# create a docker-compose.yml file with confs and  a folder called Mysql with a Dockerfile file

configure the 

# Build and start containers
docker-compose up -d --build

# Check running containers
docker ps

# Connect to MySQL from CLI
mysql -h 127.0.0.1 -P 4500 -u Bryan -p  
# Enter password: root  

# Access Adminer
# Open a browser and go to http://localhost:8080  
# Use the following credentials:  
# Server: database_electiva  
# Username: Bryan  
# Password: root  
# Database: electiva_parical_eam  


# Stop and remove containers
docker-compose down

## Reset MySQL Data

# Stop and remove containers with volumes
docker-compose down -v  

# Rebuild and start containers
docker-compose up -d --build
