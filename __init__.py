def create_app():
    app = ...
    # existing code omitted

    from . import app
    app.init_app(app)

    return app