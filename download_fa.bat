@echo off
mkdir myproject\static\webfonts
curl.exe -L -o myproject\static\css_js\font-awesome.min.css https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css
curl.exe -L -o myproject\static\webfonts\fa-brands-400.woff2 https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-brands-400.woff2
curl.exe -L -o myproject\static\webfonts\fa-brands-400.ttf https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-brands-400.ttf
curl.exe -L -o myproject\static\webfonts\fa-regular-400.woff2 https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-regular-400.woff2
curl.exe -L -o myproject\static\webfonts\fa-regular-400.ttf https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-regular-400.ttf
curl.exe -L -o myproject\static\webfonts\fa-solid-900.woff2 https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-solid-900.woff2
curl.exe -L -o myproject\static\webfonts\fa-solid-900.ttf https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-solid-900.ttf
curl.exe -L -o myproject\static\webfonts\fa-v4compat.woff2 https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-v4compat.woff2
curl.exe -L -o myproject\static\webfonts\fa-v4compat.ttf https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-v4compat.ttf
echo "Done."
