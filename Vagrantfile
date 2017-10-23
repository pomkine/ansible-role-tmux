#$VM_BOX = "jhcook/osx-elcapitan-10.11"
$VM_BOX = "ubuntu/trusty64"

Vagrant.configure("2") do |config|
  config.vm.box = $VM_BOX
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--usb", "on"]
    vb.customize ["modifyvm", :id, "--usbehci", "off"]
  end
  config.vm.provision "ansible" do |ansible|
    ansible.extra_vars = { ansible_ssh_user: 'vagrant', vagrant: true, zsh_user: 'vagrant' }
    #ansible.verbose = "vv"
    ansible.playbook = "tests/vagrant.yml"
  end
end

