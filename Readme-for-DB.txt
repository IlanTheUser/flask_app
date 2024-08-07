clone from repo
git clone https://github.com/IlanTheUser/flask_app.git

steps:

sudo yum update -y
sudo yum install python3 python3-pip mariadb105-server -y

sudo systemctl start mariadb
sudo systemctl enable mariadb

sudo mysql_secure_installation

sudo mysql -u root -p

then in the prompt:

CREATE DATABASE userregistration;
CREATE USER 'flaskuser'@'%' IDENTIFIED BY 'Aa123456';
GRANT ALL PRIVILEGES ON userregistration.* TO 'flaskuser'@'%';
FLUSH PRIVILEGES;
USE userregistration;
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,
  age INT NOT NULL,
  email VARCHAR(100) NOT NULL,
  city VARCHAR(100) NOT NULL
);
EXIT;
