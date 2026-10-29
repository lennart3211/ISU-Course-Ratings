class DBConnection:

  def __init__(self, host: str, port: int, databaseName: str):
    self.host: str = host
    self.port: int = port
    self.databaseName: str = databaseName

  def connect(self) -> None:
    pass

  def disconnect(self) -> None:
    pass

  def commit(self) -> None:
    pass

  def rollback(self) -> None:
    pass