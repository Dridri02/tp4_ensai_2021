#pip install Pyinquirer
#depuis la racine lancer python -m view.test
from view.liste_view import CheckBoxExampleView

def main():
    test = CheckBoxExampleView()
    test.display_info()
    test.make_choice()

main()
