Vagrant.configure("2") do |config|
  config.vm.network :forwarded_port, guest: 5900, host: 5900
  config.vm.box = "perk/ubuntu-24.04-arm64"

  # config.vm.provider "qemu" do |qemu|
  #   qemu.memory = 4096
  #   qemu.cpus = 1
  # end
end

=begin
exit
vagrant destroy -f
pkill -f qemu
vagrant up
vagrant ssh

sudo apt-get update
sudo apt-get install -y gnome-session x11vnc dbus-x11 xvfb
Xvfb :99 -screen 0 1024x768x24 &
sudo passwd vagrant
<secret>
export DISPLAY=:99
x11vnc -display :99 -bg -forever -shared -passwd <secret>
exec dbus-launch --exit-with-session gnome-session &
=end