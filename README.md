# SSH-Tunnel-VPN-Server

full automated vpn server

<h3>Instructions to deploy vpn server</h3>
<ol>
    <li>Install <code>ufw</code> by this command:
    <code>sudo apt install ufw</code>
    </li>
    <li>Allow your vpn ports, and your specific root ssh port
    by this commands:
        <br>
        <code>sudo ufw allow 2200:2230/tcp</code>
        <br>
        <code>sudo ufw allow 2200:2230/udp</code>
        <br>
        for your ssh: <code>sudo ufw allow 2280</code>
        <br>
        for server ui: <code>sudo ufw allow 80</code> 
</li>
<li>Enable ufw by <code>sudo ufw enable</code></li>
<li>Install git by <code>sudo apt install git</code></li>
<li>Clone code by <code>git clone https://github.com/MMDBadCoder/SSH-Tunnel-VPN-Server.git</code></li>
<li>Go to project's Directory by <code>cd SSH-Tunnel-VPN-Server/</code></li>
<li>Install MMD-VPV by <code>chmod +x install.sh ; ./init.sh</code></li>
<li>Add an superuser by <code>./adduser.sh</code></li>
<li>Tune your customized settings in VpnServer/settings by <code>vim VpnServer/settings.py</code></li>
<li>Add your webhook address to Idpay webhook field, idpay webhook should be filled by <code>yourhost/payment/webhook</code></li>
<li>Reboot your machine to starts automatically <code>sudo reboot</code></li>
</ol>