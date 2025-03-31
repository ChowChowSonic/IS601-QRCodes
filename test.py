"""Testing app"""
from main import main

def test_main(caplog):
    """Tests main"""
    caplog.set_level("INFO")
    main(["main.py", "www.google.com"])
    err = ''.join(x[2] for x in caplog.record_tuples)
    assert 'Successfully created image' in err
    assert 'Successfully saved image to' in err
def test_err(caplog):
    """Tests error logging"""
    main([])
    err = ''.join(x[2] for x in caplog.record_tuples)
    assert 'Please provide a url' in err
