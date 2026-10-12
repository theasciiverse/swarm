"""smoke.py SWARM_BINARY: start the game in a pseudo-terminal for a few
seconds, from another directory, and fail if it cannot find its data.

The release archive puts data/ next to the binary; this proves the binary
finds it there rather than in a build-tree or XDG path."""
import os, pty, select, signal, sys, tempfile, time

binary = os.path.abspath(sys.argv[1])
os.chdir(tempfile.mkdtemp())
pid, fd = pty.fork()
if pid == 0:
    os.environ.update(TERM="xterm-256color", COLUMNS="100", LINES="30")
    os.execv(binary, [binary, "--scenario", "Tutorials/move", "--autoplay", "--hide-goal"])
out, end = b"", time.time() + 8
while time.time() < end:
    r, _, _ = select.select([fd], [], [], 0.5)
    if r:
        try:
            out += os.read(fd, 65536)
        except OSError:
            break
os.kill(pid, signal.SIGKILL)
text = out.decode("utf-8", "replace")
print(f"{len(out)} bytes of output")
for bad in ("DoesNotExist", "AssetNotLoaded", "not found", "Could not"):
    if bad in text:
        print(text[-2000:])
        sys.exit(f"smoke test failed: {bad!r} in output")
if len(out) < 2000:
    print(text)
    sys.exit("smoke test failed: the game drew almost nothing")
print("ok: the game started and found its data")
