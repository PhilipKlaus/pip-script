class PipScriptError(Exception):
    pass


class PipUnexpectedError(PipScriptError):
    pass


class PipMalformedOutputError(PipScriptError):
    pass


class PipProcessError(PipScriptError):
    pass
