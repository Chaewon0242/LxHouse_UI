import pynecone as pc

class PyneconedemoConfig(pc.Config):
    pass

config = PyneconedemoConfig(
    app_name="pynecone_demo",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)