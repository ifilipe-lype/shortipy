class AppError(BaseException):
    def __init__(self, msg: str, code: int = 400) -> None:
        super().__init__(msg)

        self.msg = msg
        self.code = code
