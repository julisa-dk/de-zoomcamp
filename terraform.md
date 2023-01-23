GCP and Terraform on MacOS

1. Google Cloud Platform
   - Ubuntu as environment
   - Create new project (+generate unique ID)
   - Go to Service Account(IAM and admin): Manage keys - create new key(save .json locally)

2. Google Cloud SDK
   - Create Google Cloud Storage: Data Lake
   - BigQuery: Data Warehouse

   - Go to IAM and edit permissions for account: add role Storage Admin, Storage Object Admin and BigQuery Admin

3. Enable API for project
4. Setup (VM instance + SSH) : Compute Engine
   - Generate SSH key:

    cd ./ssh
    ssh-keygen -t rsa -f ~/.ssh gcp -c juliakhalina -b 2048
    
5. We need to put our public key to GC for share to everyone:
   - go to Metadata
   - add SSH key
   - cat gcp.pub

6. Create the instance and copy External IP
7. Connect to gcp:
    ssh -i ~/.ssh gcp juliakhalina@<External IP>

8. Install Anaconda3: wget <link to the file>
9. Connect to VM : ssh <name-vm>
10. Setup Docker on VM:
    - sudo apt-get update
    - sudo apt install docker.io
11. VCode connect to VM: 
    - add instance "Remote SSH"
    - command pallette - Connect to host (choose <name-vm>)
    - add 3 ports : 5432, 8080, 8888 (jupyter)

12. Run the docker-compose 
    docker-compose up -d

13. Install/run jupyter notebook

14. Go to Terrafor folder on VM:
    - mkdir terraform
    - open folder with generated key .json locally in terminal
    - type: sftp <name-vm> 
    - Connecting...
    - mkdir .gc
    - cd .gc
    - put .json

15. Google Cloud SDK Authentication
    - Set GOOGLE_APPLICATION_CREDENTIALS to point to the file

export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/ny-rides.json

Now authenticate:

gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

16. Terraform

    - Download Terraform
    - Put it to a folder in PATH (https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7)
    - Go to the location with Terraform files and initialize it:

        - terraform init

        Optionally we can configure your terraform files (variables.tf) to include your project id:

        variable "project" {
        description = "Your GCP Project ID"
        default = "name-project"
        type = string
        }

        - Run : terraform plan
        - Next, run terraform apply