IronPython 3
============
**There is still much that needs to be done to support Python 3.x. We are working on it, albeit slowly. We welcome all those who would like to help!**

The current target a Python 3.4 compatible release, although features and behaviors from later versions may be included.

[Official Website](http://ironpython.net)

IronPython is an open-source implementation of the Python programming language which is tightly integrated with the .NET Framework. IronPython can use the .NET Framework and Python libraries, and other .NET languages can use Python code just as easily.

| **What?** | **Where?** |
| --------: | :------------: |
| **Windows/Linux/macOS Builds** | [![Build status](https://dotnet.visualstudio.com/IronLanguages/_apis/build/status/ironpython3)](https://dotnet.visualstudio.com/IronLanguages/_build/latest?definitionId=43) [![Github build status](https://github.com/IronLanguages/ironpython3/workflows/CI/badge.svg)](https://github.com/IronLanguages/ironpython3/actions?workflow=CI) |
| **Downloads** | No releases |
| **Help** | [![Gitter chat](https://badges.gitter.im/IronLanguages/ironpython.svg)](https://gitter.im/IronLanguages/ironpython) [![StackExchange](https://img.shields.io/stackexchange/stackoverflow/t/ironpython.svg)](http://stackoverflow.com/questions/tagged/ironpython) |


Comparison of IronPython vs. C# for 'Hello World'

C#:

```cs
using System;
class Hello
{
    static void Main() 
    {
        Console.WriteLine("Hello World");
    }
}
```

IronPython:

```py
print("Hello World")
```

IronPython 3 targets Python 3, including the re-organized standard library, Unicode strings, and all of the other new features.

## Code of Conduct
This project has adopted the code of conduct defined by the Contributor Covenant to clarify expected behavior in our community.
For more information see the [.NET Foundation Code of Conduct](https://dotnetfoundation.org/code-of-conduct).

## Installation
Builds of IronPython 3 are not yet provided.

## Build
See the [building document](Documentation/building.md)

Since the main development is on Windows, Mono bugs may inadvertantly be introduced
- please report them!

## Supported Platforms
IronPython 3 targets .NET Framework 4.6, .NET Core 2.1/3.1 and .NET 5.0. The support for .NET Core and .NET 5 will follow the lifecycle defined on [.NET Core and .NET 5 Support Policy](https://dotnet.microsoft.com/platform/support/policy/dotnet-core).
