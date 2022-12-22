# install mongodb community version
# MacOS M1 version
xcode-select --install
brew tap mongodb/brew
brew update
brew install mongodb-community@6.0

# run mongodb community version
brew services start mongodb-community@6.0

# stop mongodb
brew services stop mongodb-community@6.0

# On a different terminal, connect to the running instance
mongosh
