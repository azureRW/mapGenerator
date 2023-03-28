import mod.TestModel;
import service.OutputService;

public class MapGenerator {

    public static void main(String[] args) {
        TestModel testModel = TestModel.builder()
                .name("Eric")
                .num(999)
                .position("x=1,y=2")
                .build();
        OutputService.out(testModel);

    }
}
