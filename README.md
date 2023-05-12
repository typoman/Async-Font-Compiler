# Async Font Compiler
An asynchronous font compiler based on FontGoggles for RoboFont.

Read more about FontGoggles here on the website
[
FontGoggles — Interactive Previewing and Comparing
](https://fontgoggles.org).


# How?
You can use the following example to comiple a font to a byte string without
interrupting RoboFont.

```py
import asyncio
from asyncFontCompiler.compile.compilerPool import compileUFOToBytes
from mojo.UI import Message

f = CurrentFont()

async def getFontData():
    fontData = await compileUFOToBytes(f.path, None)
    print(fontData)
    Message("Done")

asyncio.create_task(getFontData())
```

