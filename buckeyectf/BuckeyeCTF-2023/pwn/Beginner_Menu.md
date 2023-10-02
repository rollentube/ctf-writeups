# Beginner Menu (beginner)
I just made this menu for my coding class. I think I covered all the switch cases.

`nc chall.pwnoh.io 13371`

## Files
* makefile
* beginner-menu.c
* menu

## Solution
The provided application takes a number as input and prints some text depending on the user input:
```
$ nc chall.pwnoh.io 13371
Enter the number of the menu item you want:
1: Hear a joke
2: Tell you the weather
3: Play the number guessing game
4: Quit
```

In the source code we can see a function `print_flag`:
```c
void print_flag(void) {
    FILE* fp = fopen("flag.txt", "r");
    char flag[100];
    fgets(flag, sizeof(flag), fp);
    puts(flag);
}
```

This function is called in the main function, but the program exits before its execution based on those if-conditions:
```c
    if(strcmp(buf, "0\n")==0){
        printf("That's not an option\n");
        exit(0);
    }
    

	if(atoi(buf) ==1){
	    printf(joke[(rand()%5)]);
	    exit(0);
    }
	else if(atoi(buf) == 2){
	    printf(weather[(rand()%5)]);
	    exit(0);
    }
	else if(atoi(buf) ==3){
        while(num!=atoi(guess)){
	        printf("Guess the number I'm thinking of: ");
            fgets(guess, 50, stdin);
            if(atoi(guess)<num){
                printf("Guess higher!\n");
            }
            else if(atoi(guess)>num){
                printf("Guess lower!\n");
            }
        }
	    exit(0);
    }
	else if(atoi(buf)==4){
	    exit(0);
    }
	else if(atoi(buf)>4){
	    printf("That's not an option\n");
	    exit(0);
    }

    print_flag();

    return 0;
```

But those conditions are only checking for `0`, `1`, `2`, `3`, `4` and `>4`. But not `<0`. So if we enter a negative number, the function `print_flag` will be called:
```
$ nc chall.pwnoh.io 13371
Enter the number of the menu item you want:
1: Hear a joke
2: Tell you the weather
3: Play the number guessing game
4: Quit
-1
bctf{y0u_ARe_sNeaKy}
$
```