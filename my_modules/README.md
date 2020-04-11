# Установка RHVoice: 

sudo add-apt-repository ppa:linvinus/rhvoice

sudo apt-get update

sudo apt-get install rhvoice rhvoice-russian

sudo apt-get install speech-dispatcher-rhvoice

echo "Привет, как дела?" | RHVoice-client -s Anna+CLB | aplay - проверка звучания

echo "Необходимая фраза" | RHVoice-client -s Anna+CLB >./sound.mp3 - запись фразы