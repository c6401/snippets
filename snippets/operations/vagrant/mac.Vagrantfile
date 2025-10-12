Vagrant.configure("2") do |config|
  config.vm.network :forwarded_port, guest: 5900, host: 5900
  config.vm.box = "perk/ubuntu-24.04-arm64"

  # config.vm.provider "qemu" do |qemu|
  #   qemu.memory = 4096
  #   qemu.cpus = 1
  # end
end
