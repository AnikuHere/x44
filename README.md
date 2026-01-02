# x44
X44: Advanced coding made easier


🛸 X44 Master Specification
X44 is a high-performance, prefix-routed systems language designed to map instructions directly to hardware components.
1. Syntax Anatomy
Every line in X44 follows a strict hardware-dispatch format:
[Prefix][Command] (Parameters) [LogicBlock]
2. The Prefix Periodic Table
The prefix determines which hardware bus the instruction travels on.
🧠 Logic & Execution (CPU)
 * + Action: Arithmetic, logic gates, and flow control.
 * * Meta: Macros and code-generation templates.
 * % Bitwise: Raw binary manipulation at the bit level.
 * !! Guard: Error handling and system crash prevention.
 * & Async: Multi-threading and parallel tasking.
💾 Memory & Storage (RAM)
 * # Variable: Fast local stack memory.
 * ### Complex: Dynamic heap memory for large objects.
 * $ Constant: Immutable global system values.
 * | Type: Strict data enforcement (int, str, float, bin).
 * @ Pointer: Direct memory address referencing.
 * : Ownership: Safe data transfer between scopes.
🎨 Interface & Output (GPU/IO)
 * - Visual: Rendering shapes, text, and media to the buffer.
 * ~ Frame: The high-speed (60fps) execution heartbeat.
 * ! Event: User interrupts (Keyboard, Mouse, Touch).
 * < Sensor: Input from hardware (Camera, Mic, GPS).
🌐 Environment & System (Kernel)
 * _ System: Kernel commands, Filesystem, and Networking.
 * ^ Env: Compiler targets (PC-x64, Mobile-ARM, Web-WASM).
 * / Namespace: Directory structure and library paths.
 * > Bridge: External library linking (.dll, .so, .cpp).
3. Hardware Routing Map
| Component | Assigned Prefixes |
|---|---|
| CPU (Logic) | +, *, %, !!, & |
| RAM (Memory) | #, ###, $, |, @, : |
| GPU (Graphics) | -, ~ |
| Kernel (OS) | _, ^, /, >, !, < |
4. Standard Data Types
Use the | prefix to enforce these types:
 * |int| : 32/64 bit integers
 * |str| : UTF-8 Character strings
 * |float| : Floating point decimals
 * |bin| : Binary data
 * |hex| : Hexadecimal values
 * |obj| : Complex JSON-like structures
5. Core System Commands (_)
 * _terminate (target) : Safely kills a process or connection.
 * _say-terms (msg) : Standard output to the system console.
 * _file-write (path)(data) : Atomic write to local storage.
 * _file-read (path)(target) : Load data into a variable.
 * _lock (resource) : Prevents other processes from touching a resource.
🚀 Implementation Status
 * [x] Lexer: Prefix identification logic.
 * [x] Parser: Parameter extraction ( ).
 * [x] Memory Manager: Stack and Heap allocation.
 * [x] Renderer: Pygame-based GPU simulation.
 * [ ] Bridge: External C++ linking logic.