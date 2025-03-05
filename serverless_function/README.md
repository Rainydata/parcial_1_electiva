# parcial_1_electiva

to use serveless-offline you need to install node.js, then run this command for create the project 

serverless create --template aws-python3 --path serverless_function

then you have to access at project directory and add this command and add plugins

npm install
npm install serverless-offline --save-dev

then you have to configure the serverless.yml and create the function in handler.py

def hello:

after taht, run this command to start the local server

npx serverless offline

