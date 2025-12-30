Vagrant.configure("2") do |config|
  config.vm.network :forwarded_port, guest: 5900, host: 5900
  config.vm.box = "bento/ubuntu-24.04"

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

wget https://nightlies.tbb.torproject.org/nightly-builds/tor-browser-builds/tbb-nightly.20xx.xx.xx/nightly-linux-aarch64/tor-browser-linux-aarch64-tbb-nightly.20xx.xx.xx.tar.xz
tar -xf tor-browser-linux-aarch64-tbb-nightly.20xx.xx.xx.tar.xz
=end