# Cyber Attack
```php
        // Check if the user's IP is local
        const isLocalIP = (ip) => {
            return ip === "127.0.0.1" || ip === "::1" || ip.startsWith("192.168.");
        };

        // Get the user's IP address
        const userIP = "<?php echo $_SERVER['REMOTE_ADDR']; ?>";

        // Enable/disable the "Attack IP" button based on the user's IP
        const attackIPButton = document.getElementById("attack-ip");

        // Enable buttons if required fields are filled
        const enableButtons = () => {
            const playerName = document.getElementById("user-name").value;
            const target = document.getElementById("target").value;
            const attackDomainButton = document.getElementById("attack-domain");
            const attackIPButton = document.getElementById("attack-ip");

            if (playerName && target) {
                attackDomainButton.disabled = false;
                attackDomainButton.removeAttribute("data-hover");
                if (isLocalIP(userIP)) {
                    attackIPButton.disabled = false;
                }
            } else {
                attackDomainButton.disabled = true;
                attackIPButton.disabled = true;
            }
        };
```

Goal is to change this part `<?php echo $_SERVER['REMOTE_ADDR']; ?>` to a local address. This will unlock the attack IP button.