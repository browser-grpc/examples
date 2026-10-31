# grpc-dc examples — the catalog

Every runnable example in the grpc-over-datachannels project,
indexed by language and scenario. This repository is a
**generated catalog** (version v0.35.13): it copies no code, so it
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
  WebSocket signaling: [`examples/starter`](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/examples/starter).
- **VoxelSeed** — the procgen voxel dashboard (WebGPU):
  [play it](https://voxelseed.lunchgamer.com/) ·
  [source](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/examples/browser/voxelseed).

## Examples by language (387 files)

| Language | Example files | In the main repo | First run |
|---|---|---|---|
| C | 19 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/c/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/c/README.md) | `docker build -f docker/c.Dockerfile -t grpc-dc-c . && docker run --rm grpc-dc-c` |
| C++ | 25 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/cpp/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/cpp/README.md) | `docker build -f docker/cpp.Dockerfile -t grpc-dc-cpp . && docker run --rm grpc-dc-cpp` |
| C# | 53 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/csharp/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/csharp/README.md) | `docker build -f docker/csharp.Dockerfile -t grpc-dc-csharp . && docker run --rm grpc-dc-csharp` |
| Dart | 21 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/dart/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/dart/README.md) | `docker build -f docker/dart.Dockerfile -t grpc-dc-dart . && docker run --rm grpc-dc-dart` |
| Go | 11 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/go/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/go/README.md) | `cd go && go test ./...` |
| Java | 47 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/java/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/java/README.md) | `docker build -f docker/java.Dockerfile -t grpc-dc-java . && docker run --rm grpc-dc-java` |
| JavaScript | 18 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/js/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/js/README.md) | `node js/examples/echo_demo.js   # all four method shapes, in-memory pair` |
| Kotlin | 21 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/kotlin/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/kotlin/README.md) | `docker build -f docker/kotlin.Dockerfile -t grpc-dc-kotlin . && docker run --rm grpc-dc-kotlin` |
| Lua | 26 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/lua/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/lua/README.md) | `docker build -f docker/lua.Dockerfile -t grpc-dc-lua . && docker run --rm grpc-dc-lua` |
| PHP | 20 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/php/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/php/README.md) | `docker build -f docker/php.Dockerfile -t grpc-dc-php . && docker run --rm grpc-dc-php` |
| Python | 21 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/python/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/python/README.md) | `cd python && python3 -m unittest discover -s tests` |
| Ruby | 20 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/ruby/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/ruby/README.md) | `docker build -f docker/ruby.Dockerfile -t grpc-dc-ruby . && docker run --rm grpc-dc-ruby` |
| Rust | 16 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/rust/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/rust/README.md) | `cd rust && cargo test` |
| Scala | 20 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/scala/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/scala/README.md) | `docker build -f docker/scala.Dockerfile -t grpc-dc-scala . && docker run --rm grpc-dc-scala` |
| Swift | 21 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/swift/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/swift/README.md) | `docker build -f docker/swift.Dockerfile -t grpc-dc-swift . && docker run --rm grpc-dc-swift` |
| Zig | 28 | [examples](https://github.com/browser-grpc/grpc-over-datachannels/tree/v0.35.13/zig/examples) · [readme](https://github.com/browser-grpc/grpc-over-datachannels/blob/v0.35.13/zig/README.md) | `docker build -f docker/zig.Dockerfile -t grpc-dc-zig . && docker run --rm grpc-dc-zig` |

Generated code may be used without restriction (see
GENERATED-CODE-LICENSE.md); everything else is Apache-2.0
(see LICENSE). Background and design posts:
[project blog](https://c100k.blogspot.com/).
