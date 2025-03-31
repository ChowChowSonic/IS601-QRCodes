"""Testing app"""
from main import main

def test_main():
    """Tests main"""
    with open("app.log", 'r', encoding='utf-8') as file:
        pass
    main(["main.py", "www.google.com"])
    with open("app.log", 'r', encoding='utf-8') as file:
        lines = file.readlines()
        assert 'Successfully created image' in ''.join(x for x in lines)
        assert 'Successfully saved image to' in ''.join(x for x in lines)
