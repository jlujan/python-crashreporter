#!/usr/bin/env python

from six import print_
from pprint import pprint
import argparse

from crashreporter.crash_report_pb2 import CrashReport

CRASH_REPORT_HEADER_LENGTH = 8


def load_crash_report(data):
    #load the crash report data
    cr = CrashReport()
    cr.ParseFromString(data)
    return cr


def pb_fields_to_dict(obj, ignore=None):
    if not hasattr(obj, "ListFields"):
        raise Exception("Object not a ProtoBuf Object.")

    ignore = list() if ignore is None else ignore
    fields = []
    for desc, val in obj.ListFields():
        if desc.enum_type is not None:
            val = desc.enum_type.values_by_number[val].name
        fields.append((desc.name, val))
    return {k: v for k, v in fields if k not in ignore}


def get_summary(report):
    return {"System Info": pb_fields_to_dict(report.system_info),
            "Application Info": pb_fields_to_dict(report.application_info),
            "Signal Info": pb_fields_to_dict(report.signal),
            "Excpetion Info": pb_fields_to_dict(report.exception, ignore=['frames']),
            }


def print_summary(report):
    """ Print simple crash information
    """
    pprint(get_summary(report))
    print_()


def build_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("crash_reports", nargs="*", type=str,
                        help="One or more crash files.")

    return parser


def main(cr_file):
    cr = ""
    print_("Processing {}\n".format(cr_file))
    with open(cr_file, 'rb') as fp:
        #eat the header
        fp.read(CRASH_REPORT_HEADER_LENGTH)
        cr = load_crash_report(fp.read())

    print_summary(cr)


def run():
    parser = build_arg_parser()
    args = parser.parse_args()

    if len(args.crash_reports) == 0:
        parser.print_help()
        raise SystemExit("\nError: Must provide path to crash report!")

    for cr_file in args.crash_reports:
        main(cr_file)

if __name__ == "__main__":
    run()
