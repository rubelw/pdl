which -s gcc
if [[ $? != 0 ]]; then
   echo "Installing xcode"
   xcode-select --install
else
  echo "Xcode already installed"
fi



which -s brew
if [[ $? != 0 ]]; then
    echo "Installing Homebrew"
    cd ~ && mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
    eval "$(homebrew/bin/brew shellenv)"
    brew update --force --quiet
    chmod -R go-w "$(brew --prefix)/share/zsh"
else
    echo "Updating Homebrew"
    brew update
fi


which -s python3
if [[ $? != 0 ]]; then
   echo "Installing python3"
   brew install python3
   brew postinstall python3
else
   echo "Python3 already installed"
fi


which -s pip3
if [[ $? != 0 ]]; then
   echo "Installing pip3"
   brew postinstall python3
else
   echo "pip3 already installed"
fi


which -s virtualenv
if [[ $? != 0 ]]; then
   echo "Installing virtualenv"
   brew install virtualenv
else
   echo "virtualenv already installed"
fi


# Check if virtual environment for peopledatalabs has been created
if [[ ! -e "$HOME/.pdl" ]]; then
    echo "Creating .pdl directory"
    mkdir "$HOME/.pdl"
else
    echo "~/.pdl directory already exists"
fi


# Check if config file exists
if [[ ! -e "$HOME/.pdl/config" ]]; then
   echo "Enter the People Data Labs API Key"
   read varname
   echo "[data]" > "$HOME/.pdl/config"
   echo "api_key=${varname}" >> "$HOME/.pdl/config"
else
   echo "Config file already created"
fi


# Check if virtual environment has been created
if [[ ! -e "$HOME/.pdl/env" ]]; then
   echo "Creating virtual environment"
   python3_path=`which python3`
   cd $HOME/.pdl && virtualenv --python=$python3_path env

else
   echo "Virtual environment already created"
fi


# Check if pdl installed in virtual environment
if [[ ! -e "$HOME/.pdl/env/bin/pdl" ]]; then
   echo "installing pdl python package"
   source "$HOME/.pdl/env/bin/activate"
   pip install pip install peopledatalabs

else
   echo "pdl python package already installed"
fi






echo "Done"