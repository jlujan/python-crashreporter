README
------

This is a simple example to parse and read
[PLCrashReporter](https://www.plcrashreporter.org) reports using Python. The
crash report files have an 8 byte header that needs to be stripped before using
protobuf to access the crash data.

**From the command line:**

`python -m crashreporter.main /path/to/crash/report.crash`

**Output:**

```

	Processing /path/to/crash/report.crash

	{'Application Info': {'identifier': u'<REDACTED>',
	                      'version': u'1.0'},
	 'Excpetion Info': {'name': u'NSUnknownKeyException',
	                    'reason': u'[<SOSettingsViewController 0x9beefd0> setValue:forUndefinedKey:]: this class is not key value coding-compliant for the key lblOs.'},
	 'Signal Info': {'address': 51738962L, 'code': u'#0', 'name': u'SIGABRT'},
	 'System Info': {'architecture': 0,
	                 'operating_system': 2,
	                 'os_build': u'13C1021',
	                 'os_version': u'7.1',
	                 'timestamp': 1399235657L}}
```

Re-Generate Python Protocol Buffer Binding
------------------------------------------

The crashreporter/crash_report_pb2.py file is auto-generated protobuf binding.

You will need Google's Protocol Buffers installed. `brew install protobuf
--universal --with-python`. From the [PLCrashReporter zip
distribution](https://www.plcrashreporter.org/download),

```
protoc --proto_path=./ --python_out=build/proto_gen
Resources/crash_report.proto
```

The generated binding will be in build/proto_gen/Resources/crash_report_pb2.py
