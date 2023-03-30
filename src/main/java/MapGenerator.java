import mod.TestModel;
import service.OutputService;
import service.PerlinNoise;

import java.util.HashMap;
import java.util.Map;

public class MapGenerator {

    public static void main(String[] args) {

        double Z[][] = PerlinNoise.noise(3,1);
        Map<String,Object> map = new HashMap<>();
        map.put("array",Z);
        OutputService.out(map);

    }
}
