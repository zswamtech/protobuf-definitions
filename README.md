# messages.proto
syntax = "proto3";  package example;  message ExampleMessage {     google.protobuf.StringValue fetcher = 130;     google.protobuf.StringValue proxy_enabled = 131;     google.protobuf.StringValue proxy_auth = 132; }
