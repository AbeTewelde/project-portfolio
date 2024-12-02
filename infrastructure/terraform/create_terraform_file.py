def create_terraform_file(provider, config):
    if provider.lower() == "aws":
        terraform_content = f"""
        provider "aws" {{
          region = "{config['region']}"
        }}

        resource "aws_instance" "{config['instance_name']}" {{
          ami           = "{config['ami_id']}"
          instance_type = "{config['instance_type']}"

          tags = {{
            Name = "{config['instance_name']}"
          }}
        }}

        resource "aws_security_group" "{config['instance_name']}_sg" {{
          name_prefix = "{config['instance_name']}-sg"
          
          ingress {{
            from_port   = 22
            to_port     = 22
            protocol    = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
          }}

          ingress {{
            from_port   = 80
            to_port     = 80
            protocol    = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
          }}

          egress {{
            from_port   = 0
            to_port     = 0
            protocol    = "-1"
            cidr_blocks = ["0.0.0.0/0"]
          }}
        }}

        output "instance_id" {{
          value = aws_instance.{config['instance_name']}.id
        }}

        output "instance_public_ip" {{
          value = aws_instance.{config['instance_name']}.public_ip
        }}
        """
    elif provider.lower() == "azure":
        terraform_content = f"""
        provider "azurerm" {{
          features {{}}
        }}

        resource "azurerm_resource_group" "{config['resource_group']}" {{
          name     = "{config['resource_group']}"
          location = "{config['location']}"
        }}

        resource "azurerm_virtual_network" "{config['vnet_name']}" {{
          name                = "{config['vnet_name']}"
          address_space       = ["10.0.0.0/16"]
          location            = "{config['location']}"
          resource_group_name = azurerm_resource_group.{config['resource_group']}.name
        }}

        resource "azurerm_subnet" "{config['subnet_name']}" {{
          name                 = "{config['subnet_name']}"
          resource_group_name  = azurerm_resource_group.{config['resource_group']}.name
          virtual_network_name = azurerm_virtual_network.{config['vnet_name']}.name
          address_prefixes     = ["10.0.1.0/24"]
        }}

        resource "azurerm_linux_virtual_machine" "{config['instance_name']}" {{
          name                = "{config['instance_name']}"
          resource_group_name = azurerm_resource_group.{config['resource_group']}.name
          location            = "{config['location']}"
          size                = "{config['vm_size']}"

          admin_username = "adminuser"
          disable_password_authentication = true

          network_interface_ids = [
            azurerm_network_interface.{config['instance_name']}_nic.id,
          ]

          os_disk {{
            caching              = "ReadWrite"
            storage_account_type = "Standard_LRS"
          }}

          source_image_reference {{
            publisher = "Canonical"
            offer     = "UbuntuServer"
            sku       = "20_04-lts"
            version   = "latest"
          }}

          admin_ssh_key {{
            username   = "adminuser"
            public_key = file("{config['ssh_key_path']}")
          }}
        }}
        """
    elif provider.lower() == "gcp":
        terraform_content = f"""
        provider "google" {{
          project = "{config['project_id']}"
          region  = "{config['region']}"
        }}

        resource "google_compute_instance" "{config['instance_name']}" {{
          name         = "{config['instance_name']}"
          machine_type = "{config['machine_type']}"
          zone         = "{config['zone']}"

          boot_disk {{
            initialize_params {{
              image = "{config['image']}"
            }}
          }}

          network_interface {{
            network = "default"
            access_config {{
            }}
          }}

          tags = ["web", "ssh"]

          metadata_startup_script = <<-EOT
            #!/bin/bash
            sudo apt-get update
            sudo apt-get install -y nginx
          EOT
        }}
        """
    else:
        raise ValueError("Unsupported provider! Use 'aws', 'azure', or 'gcp'.")

    # Save Terraform configuration to a file
    file_name = f"{provider}_main.tf"
    with open(file_name, "w") as file:
        file.write(terraform_content.strip())
    
    print(f"Terraform configuration file '{file_name}' has been created successfully!")

# Example usage
aws_config = {
    "region": "us-east-1",
    "instance_name": "my-aws-instance",
    "instance_type": "t2.micro",
    "ami_id": "ami-0c55b159cbfafe1f0",
}

azure_config = {
    "location": "East US",
    "resource_group": "my-resource-group",
    "vnet_name": "my-vnet",
    "subnet_name": "my-subnet",
    "instance_name": "my-azure-vm",
    "vm_size": "Standard_B1s",
    "ssh_key_path": "~/.ssh/id_rsa.pub",
}

gcp_config = {
    "project_id": "my-gcp-project",
    "region": "us-central1",
    "zone": "us-central1-a",
    "instance_name": "my-gcp-instance",
    "machine_type": "e2-micro",
    "image": "projects/debian-cloud/global/images/family/debian-10",
}

# Uncomment one of the following lines to generate the corresponding configuration file
create_terraform_file("aws", aws_config)
# create_terraform_file("azure", azure_config)
# create_terraform_file("gcp", gcp_config)






#How It Works
#AWS Configuration:

#Creates an EC2 instance and a security group.
#Outputs instance ID and public IP.
#Azure Configuration:

#Creates a resource group, virtual network, subnet, and a Linux virtual machine.
#Sets up an SSH key for login.
#GCP Configuration:

#Creates a Compute Engine instance.
#Uses a startup script to install Nginx.