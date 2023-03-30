package service;

import java.io.IOException;

public class CallPython {
    public static void call() throws IOException {
        String str = "python3 -u /Users/azmac/Desktop/code/game/mapGenerator/parse.py";
        Runtime.getRuntime().exec(str);
    }
}
