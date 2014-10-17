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
	                      'version': u'1000'},
	 'Excpetion Info': {'name': u'NSInvalidArgumentException',
	                    'reason': u'*** -[NSURL initFileURLWithPath:]: nil string parameter'},
	 'Signal Info': {'address': 51755346L, 'code': u'#0', 'name': u'SIGABRT'},
	 'System Info': {'architecture': 'X86_32',
	                 'operating_system': 'IPHONE_SIMULATOR',
	                 'os_build': u'13E28',
	                 'os_version': u'7.1',
	                 'timestamp': 1405366563L}}
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
