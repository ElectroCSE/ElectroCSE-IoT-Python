# ElectroCSE IoT — Python

Python client for the [ElectroCSE IoT dashboard](https://iot.electrocse.com),
for Raspberry Pi and anything else running CPython.

> **Status: scaffold.** The package boundary and the wire contract are settled;
> the client itself is not written yet. Nothing here is usable so far.

## Why this is not in the Arduino repository

The Arduino Library Manager indexes a repository as **one** library: it reads
`library.properties` at the root and expects `src/` and `examples/` beside it.
A `python/` folder inside [ElectroCSE-IoT](https://github.com/electrocse/ElectroCSE-IoT)
would be shipped inside every ZIP an Arduino user downloads, and the registry
offers no way to exclude it.

They would also be the wrong shape for each other. The C++ library is built
around a microcontroller with tens of kilobytes of RAM and no operating system
— fixed-size tables, no `malloc`, a hand-rolled check-in loop. None of those
constraints exist on a Pi, and a Python client that inherited them would be a
transliterated header file rather than Python.

## What the two DO share

The wire protocol, which belongs to the dashboard rather than to either client:

```http
POST {server}/api/v1/sync
Authorization: Bearer ecse_iot_{id}|{secret}
Content-Type: application/json

{"readings": [{"channel": "temperature", "value": 21.5, "unit": "C"}],
 "state": {"relay1": 1}}
```

```json
{"commands": {"relay1": 1}, "next_poll_ms": 1000}
```

Three things about that exchange are easy to get wrong, and the C++ client
documents each at the point it handles it:

- **`state` is the echo that clears the dashboard's "Pending" badge.** A client
  that applies a command and never reports the applied value leaves the card
  pending for ever, with nothing wrong anywhere else.
- **`next_poll_ms` is the server's instruction, not a suggestion.** It is how a
  fleet is retuned without reflashing — 1s while somebody is watching, 30s when
  nobody is.
- **`commands` is an object, never an array.** An empty one is `{}`.

## Layout

```
ElectroCSE-IoT-Python/
├── electrocse/
│   └── __init__.py     the wire constants, and the reasoning
├── setup.py
├── README.md
└── LICENSE
```

## Licence

MIT — see [LICENSE](LICENSE).
