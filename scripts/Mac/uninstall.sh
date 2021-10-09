

# Check if ~/.pdl directory exists
if [[ -e "$HOME/.pdl" ]]; then
    echo "Removing .pdl directory"
    rm -rf "$HOME/.pdl"
else
    echo "~/.pdl does not exists"
fi


echo "Done"