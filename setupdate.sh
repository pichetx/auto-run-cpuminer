#!/bin/sh

apt-get update -y
apt-get upgrade -y
apt-get install libcurl4-openssl-dev -y
apt-get install libssl-dev -y
apt-get install libjansson-dev -y
apt-get install automake -y
apt-get install autotools-dev -y  
apt-get install build-essential -y
apt-get install nano -y
apt-get install autoconf -y
apt-get install pkg-config -y
apt-get install libgmp-dev -y
apt-get install zlib1g-dev -y
apt-get install make -y
apt-get install g++ -y
apt-get install libtool -y

chmod +x edit-miner
chmod +x run-miner
chmod +x add-ip
chmod +x update
chmod +x up-grade

apt-get install python3 -y
apt-get install pip -y
apt-get install wget -y
apt-get install figlet -y
apt-get install python3-progress -y
apt-get install python3-requests -y


mv mobile-mining ../../etc
mv edit-miner ../../bin
mv run-miner ../../bin
mv add-ip ../../bin
mv update ../../bin
mv up-grade ../../bin

run-miner


cd && cd ../etc/mobile-mining/cpuminer-multi
chmod +x build.sh
./build.sh

chmod +x cpuminer-multi

run-miner
