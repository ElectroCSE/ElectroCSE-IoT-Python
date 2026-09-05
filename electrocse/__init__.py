"""
ElectroCSE IoT — Python client.

Nothing here yet beyond the boundary. The transport, the check-in loop and the
handler registration all still have to be written; what this package fixes now
is WHERE they go.

WHY THIS IS A SEPARATE REPOSITORY FROM ElectroCSE-IoT
-----------------------------------------------------
The Arduino Library Manager indexes a repository by its `library.properties`
and expects the whole repository to BE one Arduino library: `src/` at the root,
`examples/` beside it, and nothing that looks like a second project. A `python/`
directory inside ElectroCSE-IoT would ship inside every ZIP an Arduino user
downloads, and the registry has no way to say "ignore that half".

The two also have nothing to share. The C++ side exists because a
microcontroller has 40KB of RAM and no operating system; the Python side will
run on a Raspberry Pi with neither constraint, so it should use requests or
aiohttp and look like Python rather than like a transliterated header file. A
shared repository would invite exactly that transliteration.

WHAT THE TWO MUST AGREE ON is the wire protocol, not the code:

    POST {server}/api/v1/sync
    Authorization: Bearer ecse_iot_{id}|{secret}
    {"readings": [{"channel": ..., "value": ...}], "state": {...}}

    -> {"commands": {...}, "next_poll_ms": 1234}

That contract is owned by the dashboard, and both clients are readers of it.
See the ElectroCSE-IoT README for the C++ implementation of the same exchange.
"""

__version__ = "0.0.1"

# The dashboard this client talks to unless told otherwise. Deliberately the
# same default the Arduino header carries, for the same reason: the address is
# not one of the things somebody should have to know to get started.
DEFAULT_SERVER = "https://iot.electrocse.com"

# Owned by the dashboard, not by this package. The older
# /api/device/telemetry route also accepts readings and would appear to work,
# but drops `value_string` silently - so a text reading arrives with no value
# and nothing anywhere says why.
DEFAULT_PATH = "/api/v1/sync"

__all__ = ["DEFAULT_SERVER", "DEFAULT_PATH", "__version__"]
