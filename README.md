# grpc-dc examples — the catalog

Every runnable example in the grpc-over-datachannels project,
indexed by language and scenario. This repository is a
**generated catalog** (version v0.47.2): it copies no code, so it
cannot drift — each entry links to the example in the main
repo at this release's tag, where it is tested by the same
CI that tests the runtimes.

New here? Run your first RPC in the browser, no install:
[live generator](https://browser-grpc.github.io/grpc-over-datachannels/app/).

## Scenarios

- **Echo in every language** — the same unary / server-streaming /
  client-streaming / bidi service in all sixteen languages:
  [gallery](https://browser-grpc.github.io/grpc-over-datachannels/gallery.html).
- **Event bus** — publish/subscribe as a gRPC service:
  [browser-grpc/eventbus](https://github.com/browser-grpc/eventbus).
- **Kafka clients** — produce/consume through the Rust proxy:
  [browser-grpc/kafka-proxy](https://github.com/browser-grpc/kafka-proxy).
- **Browser starter** — browser client ↔ Node server with
  WebSocket signaling: [`examples/starter`](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/examples/starter).
- **WebRTC-Direct** — signaling-free Echo in every language
  (direct, TURN, and STUN peer modes, compose included):
  [`examples/direct`](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/examples/direct).
- **VoxelSeed** — the procgen voxel dashboard (WebGPU):
  [play it](https://voxelseed.lunchgamer.com/) ·
  [source](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/examples/browser/voxelseed).

## Examples by language (438 files)

| Language | Example files | In the main repo | First run |
|---|---|---|---|
| C | 21 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/c/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/c/README.md) | `docker build -f docker/c.Dockerfile -t grpc-dc-c . && docker run --rm grpc-dc-c` |
| C++ | 31 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/cpp/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/cpp/README.md) | `docker build -f docker/cpp.Dockerfile -t grpc-dc-cpp . && docker run --rm grpc-dc-cpp` |
| C# | 58 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/csharp/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/csharp/README.md) | `cd csharp && dotnet run --project tests -- TestEcho` |
| Dart | 27 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/dart/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/dart/README.md) | `docker build -f docker/dart.Dockerfile -t grpc-dc-dart . && docker run --rm grpc-dc-dart` |
| Go | 16 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/go/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/go/README.md) | `cd go && go test ./...` |
| Java | 50 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/java/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/java/README.md) | `docker build -f docker/java.Dockerfile -t grpc-dc-java . && docker run --rm grpc-dc-java` |
| JavaScript | 19 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/js/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/js/README.md) | `node js/examples/echo_demo.js   # all four method shapes, in-memory pair` |
| Kotlin | 24 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/kotlin/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/kotlin/README.md) | `docker build -f docker/kotlin.Dockerfile -t grpc-dc-kotlin . && docker run --rm grpc-dc-kotlin` |
| Lua | 31 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/lua/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/lua/README.md) | `docker build -f docker/lua.Dockerfile -t grpc-dc-lua . && docker run --rm grpc-dc-lua` |
| PHP | 21 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/php/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/php/README.md) | `docker build -f docker/php.Dockerfile -t grpc-dc-php . && docker run --rm grpc-dc-php` |
| Python | 21 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/python/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/python/README.md) | `cd python && python3 -m unittest discover -s tests` |
| Ruby | 21 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/ruby/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/ruby/README.md) | `docker build -f docker/ruby.Dockerfile -t grpc-dc-ruby . && docker run --rm grpc-dc-ruby` |
| Rust | 15 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/rust/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/rust/README.md) | `cd rust && cargo test` |
| Scala | 23 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/scala/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/scala/README.md) | `docker build -f docker/scala.Dockerfile -t grpc-dc-scala . && docker run --rm grpc-dc-scala` |
| Swift | 26 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/swift/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/swift/README.md) | `cd swift && mkdir -p build && swiftc -swift-version 5 -O -L ../rust/target/release -lgrpc_dc -Xlinker -rpath -Xlinker $PWD/../rust/target/release grpcdc/*.swift examples/Pb.swift examples/EchoMessages.swift examples/EchoRequestStruct.swift examples/EchoResponseStruct.swift examples/StructDcBridge.swift examples/EchoGrpcDc.swift examples/EchoServiceImpl.swift examples/StdioTransport.swift examples/DynamicEchoService.swift examples/interop/*.swift $(ls tests/*.swift | grep -v TestKafkaNative.swift) -o build/tests && ./build/tests TestEcho` |
| Zig | 34 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.47.2/zig/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.47.2/zig/README.md) | `cd zig && zig build tests` |

Generated code may be used without restriction (see
GENERATED-CODE-LICENSE.md); everything else is Apache-2.0
(see LICENSE). Background and design posts:
[project blog](https://c100k.blogspot.com/).
