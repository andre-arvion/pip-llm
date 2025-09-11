import pytest

def test_import_flask_app():
    # Ensures the module imports (Flask 0.9 presence not enforced here)
    import insecure_llm_tester.web.flask_app as flask_app
    assert hasattr(flask_app, "app")
