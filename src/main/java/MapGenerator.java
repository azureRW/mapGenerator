import service.CallPython;
import service.OutputService;
import service.PerlinNoise;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class MapGenerator {

    public static void main(String[] args) throws IOException {

        double[][] Z = PerlinNoise.noise(1,0.6);
        Map<String,Object> map = new HashMap<>();
        map.put("map",Z);
        OutputService.out(map);
        CallPython.call();
    }
}
