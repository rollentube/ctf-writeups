# timer
You will find the flag after analysing this apk (100 Points)
Download here.

## Files
- timer.apk

## Solution
Reversed with jadx-gui. In the AndroidManifest.xml we can see, that the file 'com.example.time.MainActivity' is the main file of the APK. Reversing the bringst no flag. Its just some timer and GUI parameters. But if we take a look at the 'BuildConfig' we can find the flag:
```java
public final class BuildConfig {
    public static final String APPLICATION_ID = "com.example.timer";
    public static final String BUILD_TYPE = "debug";
    public static final boolean DEBUG = Boolean.parseBoolean("true");
    public static final int VERSION_CODE = 1;
    public static final String VERSION_NAME = "picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}";
}
```

The flag is: picoCTF{t1m3r\_r3v3rs3d\_succ355fully\_17496}
