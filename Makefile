# Terslation - Terminal Translator
# git clone https://github.com/denstiny/Terslation.git

install:
	cp -f translation/fanyi.sh /bin/terlat
	chmod +x /bin/terlat
	mkdir -p /usr/local/src/fanyi
	mkdir ~/.terlist
	chmod 777 /usr/local/src/fanyi
	cp -f translation/fanyi.py /usr/local/src/fanyi/fanyi.py
	@echo "Install successful."

uninstall:
	rm /usr/bin/terlat
	rm -r /usr/local/src/fanyi
	@echo "Uninstall successful."
