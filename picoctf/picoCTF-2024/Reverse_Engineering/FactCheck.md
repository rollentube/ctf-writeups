# FactCheck (200 points)
This binary is putting together some important piece of information... Can you uncover that information?

Examine this file. Do you understand its inner workings?

## Data
* bin

## Solution
The code seems to be a bit chaotic, but is actually pretty straight forward. I anlysed it with IDA, but the approach in Ghidra would be the same. I will remove lines of the decompiled code that is not relevant for the understanding. Also I renamed some variables.

The first interesting part is the allocation of several characters:
```c++
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(
    flag_str,
    "picoCTF{wELF_d0N3_mate_",
    &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v23, "4", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v24, "5", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v25, "6", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v26, "3", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v27, "e", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v28, "5", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v29, "a", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v30, "e", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v31, "e", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v32, "d", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v33, "b", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v34, "f", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v35, "6", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v36, "e", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v37, "d", &v21);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v38, "8", &v21);
```

We got the beginning of our flag in the variable `flag_str`: `picoCTF{wELF_d0N3_mate_`

Afterwards there are several characters initialized into the variables `v23` - `v38`. You can see the explicit characters in the code.

After the initialization the program is working through some conditions:
```c++
if ( *(char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](v24, 0LL) <= 65 )
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v34);

if ( *(_BYTE *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](v35, 0LL) != 65 )
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v37);

if ( "Hello" == "World" )
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v25);

v19 = *(char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](v26, 0LL);
if ( v19 - *(char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](v30, 0LL) == 3 )
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v26);

std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v25);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v28);

if ( *(_BYTE *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](v29, 0LL) == 71 )
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v29);

std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v27);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v36);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v23);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, v31);
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(flag_str, 125LL);
```

For example the first condition checks if `v24` ("5") is lower equal to 65 ("A"). If that is the case the program would append `v34` ("f") to the flag string. The second condition checks `v35` ("6") for unequality to 65 ("A") and so on.

Than we have also a few lines that appends the flag without any condition. 

If try to translate it into some kind of pseudo code, we get the following lines:
```python
if v24 ("5") <= 65 ("A"):	# TRUE
	flag_str += v34 ("f")

if v35 ("6") != 65 ("A"):	# TRUE
	flag_str += v37 ("d")

if "Hello" == "World":		# FALSE
	flag_str += v25 ("6")

v19 = v26 ("3")
if v19 ("3") - v30 ("e") == 3:	# FALSE
	flag_str += v26 ("3")

flag_str += v25 ("6")
flag_str += v28 ("5")

if v29 ("a") == 71 ("G"):	# FALSE
	flag_str += v29 ("a")

flag_str += v27 ("e")
flag_str += v36 ("e")
flag_strv += v23 ("4")
flag_strv += v31 ("e")
flag_strv += 125 ("}")
```

The appendings in the TRUE conditions and those without condition would add the string `fd65ee4e}` to the flag.

So our flag is:
```
picoCTF{wELF_d0N3_mate_fd65ee4e}
```
