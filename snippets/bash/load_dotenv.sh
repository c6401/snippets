export $(cat .env | sed 's/#.*//g' | xargs)
