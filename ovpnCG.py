#!/usr/bin/env python
from urllib.parse import urlparse
from jinja2 import Template


class Address:
    adress = None
    port = 1194

    def __init__(self, string):
        parsed = urlparse('//{}'.format(string))
        self.adress = parsed.hostname
        if parsed.port is not None:
            self.port = parsed.port


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser()

    parser.add_argument("--remote", "-r", default="0.0.0.0",
                        help="Remote address. If no port is specified, use port 1194")

    pg_cert = parser.add_argument_group("Certificates")
    pg_cert.add_argument("--dh", default=None, type=argparse.FileType('r'),
                         help="Diffie-Hellman parameters file")
    pg_cert.add_argument("--tls", type=argparse.FileType('r'),
                         help="TLS Key to use")
    pg_cert.add_argument("--ca", type=argparse.FileType('r'),
                         help="Certificate Authority file")
    pg_cert.add_argument("--cert", type=argparse.FileType('r'),
                         help="Certificate file")
    pg_cert.add_argument("--key", type=argparse.FileType('r'), help="Key file")

    pg_files = parser.add_argument_group("Files")

    pg_files.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                          default=sys.stdin)
    pg_files.add_argument('outfile', nargs="?", type=argparse.FileType('w'),
                          default=sys.stdout)

    args = parser.parse_args()

    template = Template(args.infile.read())

    dh = None
    if args.dh is not None:
        dh = args.dh.read()

    ca = args.ca.read() if args.ca is not None else None
    tls = args.tls.read() if args.tls is not None else None
    cert = args.cert.read() if args.cert is not None else None
    key = args.key.read() if args.key is not None else None

    args.outfile.write(template.render(dh=dh, ca=ca,
                                       tls=tls,
                                       cert=cert,
                                       key=key,
                                       remote=Address(args.remote)))
