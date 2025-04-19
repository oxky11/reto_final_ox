Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.hostname = "dev-vm"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  
  config.vm.provision "shell", env: {
    "ECR_URL" => ENV["ECR_URL"],
	"DOCKER_TAG" => ENV["DOCKER_TAG"]
  }, run: "always", inline: <<-SHELL
	  sudo apt-get update
	  sudo apt-get install -y ansible python3-pip docker.io
	  cd /vagrant/ansible
	  
	  # Renombrar el archivo inventory y quitarle el permiso de ejecución
	  sudo mv inventory inventory.ini
	  sudo chmod -x inventory.ini

	  # Ejecutar el playbook
	  ansible-playbook playbook.yml -i inventory.ini -e "ecr_url=$ECR_URL tag=$TAG"
	SHELL
end