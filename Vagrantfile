Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.hostname = "dev-vm"
  config.vm.network "private_network", type: "dhcp"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/playbook.yml"
    ansible.inventory_path = "ansible/inventory"
  end
  
  config.vm.provision "shell", inline: <<-SHELL
	sudo apt-get update
	sudo apt-get install -y ansible python3-pip docker.io
	cd /vagrant/ansible
	ansible-playbook -i inventory.ini playbook.yml
	SHELL
  end
end